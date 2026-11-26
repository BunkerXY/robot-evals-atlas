#!/usr/bin/env python3
"""Weekly digest: GitHub releases published in the last N days across every tracked repo.
Writes Markdown to stdout (CI posts it as an issue so maintainers can update the atlas)."""
import json, os, re, sys, pathlib, datetime, urllib.request
import yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
DAYS = int(os.environ.get("DAYS", "7"))
since = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=DAYS)
H = {"Accept": "application/vnd.github+json", "User-Agent": "robot-agents-evals-atlas"}
if os.environ.get("GITHUB_TOKEN"):
    H["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
entries = yaml.safe_load((ROOT / "data/entries.yaml").read_text())
rows = []
for e in entries:
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)/?$", e.get("code") or "")
    if not m:
        continue
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{m.group(1)}/{m.group(2)}/releases?per_page=5", headers=H)
        for r in json.load(urllib.request.urlopen(req, timeout=30)):
            ts = datetime.datetime.fromisoformat((r.get("published_at") or r["created_at"]).replace("Z", "+00:00"))
            if ts >= since:
                rows.append(f"| {e['name']} | [{r['tag_name']}]({r['html_url']}) | {ts:%Y-%m-%d} |")
    except Exception as ex:  # keep going; report at the end
        print(f"<!-- {e['id']}: {ex} -->", file=sys.stderr)
print(f"## New releases in tracked repos (last {DAYS} days)\n")
print("\n".join(["| Project | Release | Date (UTC) |", "|---|---|---|", *rows]) if rows else "_No new releases._")
print("\nCheck whether any of these change a model, score or license in `data/`.")
