## Shell Rules for this repo

1. **Canonical interactive shell**
   - VS Code integrated terminal for this workspace is **Git Bash**.
   - When you run commands manually, assume **bash/MSYS** semantics.

2. **Path separators in commands**
   - In Git Bash, always use **forward slashes** in commands:
     - `tools/gitbash.cmd`
     - `bun tools/recap_src/recap-rich.ts`
   - Avoid backslashes in commands: `tools\gitbash.cmd` is parsed by bash as `toolsgitbash.cmd` (invalid).

3. **Wrappers and when to use them**
   - From **cmd.exe / PowerShell / external tools** that can't run bash reliably:
     - Use [`tools/gitbash.cmd`](tools/gitbash.cmd:1) to run a one-off Git Bash command.
   - From **Git Bash** (VS Code terminal):
     - Prefer direct bash or [`tools/gitbash.ts`](tools/gitbash.ts:1):
       - `bun tools/gitbash.ts "bash tools/pulse.sh"`

4. **Debugging wrapper behavior**
   - Both wrappers support debug logging:
     - `set GITBASH_DEBUG=1` (for [`tools/gitbash.cmd`](tools/gitbash.cmd:1))
     - `GITBASH_DEBUG=1 bun tools/gitbash.ts "echo hi"`
   - Logs normalize paths to forward slashes to keep them shell-agnostic.

