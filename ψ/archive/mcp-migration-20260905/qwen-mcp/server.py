# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp[cli]>=2,<3",
#     "openai>=1.40.0",
# ]
# ///
"""MCP server exposing Alibaba DashScope's Qwen models as tools.

Run as an MCP stdio server (how Claude Code launches it):
    uv run server.py

Run a one-shot check that the key, endpoint and model all work:
    uv run server.py --selftest "say hello"
    uv run server.py --list-models

Configuration comes from the environment:
    DASHSCOPE_API_KEY   required
    DASHSCOPE_BASE_URL  optional; defaults to the international endpoint.
                        Keys issued on the mainland-China console return 401
                        against this host and need the mainland URL instead.
"""

import os
import sys

from mcp.server.mcpserver import MCPServer
from openai import OpenAI

INTL_BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"

DEFAULT_MODEL = "qwen3.7-flash-2026-07-15"

# Visible in the tool docstring so a caller can pick a model without first
# paying for a round-trip to qwen_list_models().
KNOWN_MODELS = [
    "qwen3.7-flash-2026-07-15",
    "qwen3.7-plus",
    "qwen3.6-plus",
    "qwen3.7-max",
]

mcp = MCPServer("qwen")

_client: OpenAI | None = None


def client() -> OpenAI:
    """Build the client lazily so a missing key fails at call time, not import."""
    global _client
    if _client is None:
        api_key = os.environ.get("DASHSCOPE_API_KEY")
        if not api_key:
            raise RuntimeError(
                "DASHSCOPE_API_KEY is not set in this process's environment."
            )
        _client = OpenAI(
            api_key=api_key,
            base_url=os.environ.get("DASHSCOPE_BASE_URL", INTL_BASE_URL),
        )
    return _client


@mcp.tool()
def qwen_ask(
    prompt: str,
    model: str = DEFAULT_MODEL,
    system: str | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
) -> str:
    """Ask a Qwen model a question via Alibaba DashScope and return its reply.

    Each call is stateless — pass any conversation history inside `prompt`.

    Known models: qwen3.7-flash-2026-07-15 (default, fastest),
    qwen3.7-plus, qwen3.6-plus, qwen3.7-max (strongest).
    Call qwen_list_models() for the live roster this account can reach.
    """
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    kwargs = {}
    if temperature is not None:
        kwargs["temperature"] = temperature
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens

    response = client().chat.completions.create(
        model=model,
        messages=messages,
        **kwargs,
    )
    return response.choices[0].message.content or ""


@mcp.tool()
def qwen_list_models() -> str:
    """List the models this DashScope account can actually reach, newline separated.

    Queries the endpoint live rather than returning a baked-in list, since
    Alibaba's roster changes and date-pinned snapshots get retired.
    """
    models = sorted(m.id for m in client().models.list())
    return "\n".join(models) if models else "(endpoint returned no models)"


def selftest(argv: list[str]) -> int:
    """Exercise the API directly, bypassing MCP, so failures are readable."""
    base_url = os.environ.get("DASHSCOPE_BASE_URL", INTL_BASE_URL)
    print(f"endpoint: {base_url}")
    print(f"key set:  {bool(os.environ.get('DASHSCOPE_API_KEY'))}")

    try:
        if "--list-models" in argv:
            print("\n--- models ---")
            print(qwen_list_models())
        else:
            prompt = next(
                (a for a in argv[1:] if not a.startswith("--")),
                "Reply with exactly: ok",
            )
            model = DEFAULT_MODEL
            print(f"model:    {model}")
            print(f"prompt:   {prompt}")
            print("\n--- reply ---")
            print(qwen_ask(prompt, model=model))
    except Exception as exc:  # surfaced verbatim; 401 vs 404 is the useful signal
        print(f"\nFAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    print("\nOK")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--list-models" in sys.argv:
        sys.exit(selftest(sys.argv))
    mcp.run()
