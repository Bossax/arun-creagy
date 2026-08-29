"""The miss register -- append-only history for the style loop.

Two things are recorded, and they answer different questions.

  candidates : patterns you corrected by hand that are NOT yet in the pack.
               This is what drives promotion. Learning 2026-06-27 fixed the
               threshold at two: when the same pattern has been corrected twice,
               it stops being a local edit and becomes a rule.

  runs/misses: which pack rules actually fire, on which drafts. A rule already
               in the lexicon does not need promoting, so this does not feed the
               trigger -- it tells you whether a rule earns its place, and lets
               you replay today's ruleset over older drafts.

Nothing is ever deleted. Promotion marks a candidate, it does not remove it.

Usage:
    register.py init
    register.py observe "<pattern>" --source <file> [--note "..."] [--fix "..."]
    register.py ready [--threshold 2]
    register.py promoted "<pattern>"
    register.py stats
    register.py export [--out <path>]
"""
import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent


def repo_root():
    for parent in SKILL_ROOT.parents:
        if (parent / "AGENTS.md").exists() and (parent / "ψ").is_dir():
            return parent
    return None


def db_path():
    override = os.environ.get("WRITING_TH_REGISTER")
    if override:
        return Path(override)
    root = repo_root()
    if root is None:
        return SKILL_ROOT / "miss_register.db"
    return root / "ψ" / "memory" / "style" / "miss_register.db"


SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    ts       TEXT NOT NULL,
    pattern  TEXT NOT NULL,
    source   TEXT,
    fix      TEXT,
    note     TEXT,
    layer    TEXT DEFAULT 'lexical'
);
CREATE TABLE IF NOT EXISTS promotions (
    pattern  TEXT PRIMARY KEY,
    ts       TEXT NOT NULL,
    layer    TEXT DEFAULT 'lexical'
);
CREATE TABLE IF NOT EXISTS runs (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    ts        TEXT NOT NULL,
    draft     TEXT NOT NULL,
    lexicon   TEXT,
    scope     TEXT,
    tokens    INTEGER,
    sentences INTEGER,
    verdict   TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS misses (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id  INTEGER NOT NULL,
    rule    TEXT NOT NULL,
    kind    TEXT NOT NULL,
    FOREIGN KEY (run_id) REFERENCES runs(id)
);
CREATE INDEX IF NOT EXISTS idx_candidates_pattern ON candidates(pattern);
CREATE INDEX IF NOT EXISTS idx_misses_rule ON misses(rule);
"""


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect(create=False):
    p = db_path()
    if not p.exists() and not create:
        return None
    p.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(p)
    con.executescript(SCHEMA)
    # Lightweight schema migration for existing DB
    try:
        con.execute("ALTER TABLE candidates ADD COLUMN layer TEXT DEFAULT 'lexical'")
    except sqlite3.OperationalError:
        pass
    try:
        con.execute("ALTER TABLE promotions ADD COLUMN layer TEXT DEFAULT 'lexical'")
    except sqlite3.OperationalError:
        pass
    return con


# ---------- write side ----------

def cmd_init(_ns):
    con = connect(create=True)
    con.commit()
    print(f"register ready at {db_path()}")
    con.close()


def cmd_observe(ns):
    con = connect(create=True)
    layer = getattr(ns, "layer", "lexical") or "lexical"
    con.execute(
        "INSERT INTO candidates (ts, pattern, source, fix, note, layer) VALUES (?,?,?,?,?,?)",
        (now(), ns.pattern, ns.source, ns.fix, ns.note, layer))
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM candidates WHERE pattern=?", (ns.pattern,)).fetchone()[0]
    promoted = con.execute("SELECT 1 FROM promotions WHERE pattern=?", (ns.pattern,)).fetchone()
    con.close()

    print(f"observed: {ns.pattern!r} (layer: {layer})")
    print(f"  seen {n} time(s)" + ("  [already promoted]" if promoted else ""))
    if n >= 2 and not promoted:
        target = "STRUCTURAL_RULES_TH.json" if layer == "structural" else "LEXICON_TH.json / STYLE_PACK_TH.md"
        print(f"  >> AT THRESHOLD -- promote this into {target}, then:")
        print(f"     register.py promoted \"{ns.pattern}\" --layer {layer}")


def log_run(draft, lexicon, scope, tokens, sentences, verdict, misses):
    """Called by the linter. Never raises -- a logging failure must not block a gate."""
    try:
        con = connect(create=True)
        cur = con.execute(
            "INSERT INTO runs (ts, draft, lexicon, scope, tokens, sentences, verdict) "
            "VALUES (?,?,?,?,?,?,?)",
            (now(), str(draft), lexicon, scope, tokens, sentences, verdict))
        run_id = cur.lastrowid
        con.executemany("INSERT INTO misses (run_id, rule, kind) VALUES (?,?,?)",
                        [(run_id, r, k) for r, k in misses])
        con.commit()
        con.close()
        return run_id
    except Exception:
        return None


def cmd_promoted(ns):
    con = connect()
    if con is None:
        print("no register yet -- run: register.py init")
        sys.exit(1)
    layer = getattr(ns, "layer", "lexical") or "lexical"
    con.execute("INSERT OR REPLACE INTO promotions (pattern, ts, layer) VALUES (?,?,?)", (ns.pattern, now(), layer))
    con.commit()
    con.close()
    print(f"marked promoted: {ns.pattern!r} (layer: {layer})")


# ---------- read side ----------

def cmd_ready(ns):
    con = connect()
    if con is None:
        print("no register yet -- run: register.py init")
        sys.exit(0)
    
    where_clause = "WHERE p.pattern IS NULL"
    params = []
    if getattr(ns, "layer", None):
        where_clause += " AND c.layer = ?"
        params.append(ns.layer)
    params.append(ns.threshold)

    rows = con.execute(f"""
        SELECT c.pattern, COUNT(*) AS n, MIN(c.ts), MAX(c.ts), c.layer
        FROM candidates c
        LEFT JOIN promotions p ON p.pattern = c.pattern
        {where_clause}
        GROUP BY c.pattern
        HAVING n >= ?
        ORDER BY n DESC, MAX(c.ts) DESC
    """, params).fetchall()

    if not rows:
        pending = con.execute("""
            SELECT COUNT(DISTINCT c.pattern) FROM candidates c
            LEFT JOIN promotions p ON p.pattern = c.pattern
            WHERE p.pattern IS NULL""").fetchone()[0]
        layer_txt = f" [{ns.layer}]" if getattr(ns, "layer", None) else ""
        print(f"nothing at threshold {ns.threshold}{layer_txt}. "
              f"{pending} unpromoted pattern(s) seen fewer times.")
        con.close()
        sys.exit(0)

    print(f"{len(rows)} pattern(s) at or above threshold {ns.threshold} -- promote these:\n")
    for pattern, n, first, last, layer in rows:
        print(f"  [{n}x] [{layer or 'lexical'}]  {pattern}")
        print(f"         first {first[:10]}   last {last[:10]}")
        for (src, fix) in con.execute(
                "SELECT source, fix FROM candidates WHERE pattern=? ORDER BY ts", (pattern,)):
            if src or fix:
                print(f"         - {src or '?'}" + (f"  ->  {fix}" if fix else ""))
        print()
    con.close()


def cmd_stats(_ns):
    con = connect()
    if con is None:
        print("no register yet -- run: register.py init")
        sys.exit(0)
    def q(sql, *args):
        return con.execute(sql, args).fetchone()[0]

    runs = q("SELECT COUNT(*) FROM runs")
    failed = q("SELECT COUNT(*) FROM runs WHERE verdict = ?", "fail")

    print(f"register  : {db_path()}")
    print(f"runs      : {runs} ({failed} failed)")
    print(f"misses    : {q('SELECT COUNT(*) FROM misses')}")
    print(f"candidates: {q('SELECT COUNT(*) FROM candidates')} observations "
          f"across {q('SELECT COUNT(DISTINCT pattern) FROM candidates')} pattern(s)")
    print(f"promoted  : {q('SELECT COUNT(*) FROM promotions')}")

    rows = con.execute("""SELECT rule, COUNT(*) n FROM misses
                          GROUP BY rule ORDER BY n DESC LIMIT 8""").fetchall()
    if rows:
        print("\nrules firing most often:")
        for rule, n in rows:
            print(f"  {n:4}x  {rule[:64]}")
    con.close()


def cmd_export(ns):
    con = connect()
    if con is None:
        print("no register yet -- run: register.py init")
        sys.exit(0)
    con.row_factory = sqlite3.Row
    data = {t: [dict(r) for r in con.execute(f"SELECT * FROM {t} ORDER BY 1")]
            for t in ("candidates", "promotions", "runs", "misses")}
    con.close()
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if ns.out:
        Path(ns.out).write_text(text, encoding="utf-8")
        print(f"exported to {ns.out}")
    else:
        print(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(fn=cmd_init)

    o = sub.add_parser("observe", help="record a hand-correction of a not-yet-a-rule pattern")
    o.add_argument("pattern")
    o.add_argument("--source", help="file or evidence log the correction came from")
    o.add_argument("--fix", help="what it was changed to")
    o.add_argument("--layer", choices=["lexical", "regex", "structural"], default="lexical", help="rule layer (lexical, regex, structural)")
    o.add_argument("--note")
    o.set_defaults(fn=cmd_observe)

    r = sub.add_parser("ready", help="patterns that have crossed the promotion threshold")
    r.add_argument("--threshold", type=int, default=2)
    r.add_argument("--layer", choices=["lexical", "regex", "structural"], help="filter by layer")
    r.set_defaults(fn=cmd_ready)

    p = sub.add_parser("promoted", help="mark a candidate as now living in the pack or structural rules")
    p.add_argument("pattern")
    p.add_argument("--layer", choices=["lexical", "regex", "structural"], default="lexical")
    p.set_defaults(fn=cmd_promoted)

    sub.add_parser("stats").set_defaults(fn=cmd_stats)

    e = sub.add_parser("export", help="dump the whole register as readable JSON")
    e.add_argument("--out")
    e.set_defaults(fn=cmd_export)

    ns = ap.parse_args()
    ns.fn(ns)


if __name__ == "__main__":
    main()
