#!/usr/bin/env python3
"""Refresh data/stars.json (stars, license, last push) for every GitHub repo linked in data/entries.yaml.
Uses the GitHub Search API with several repo: qualifiers per query. Set GITHUB_TOKEN for higher limits (CI does)."""
import json, os, re, time, pathlib, urllib.request, urllib.parse, datetime
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
entries = yaml.safe_load((ROOT / "data/entries.yaml").read_text())

def repo_of(url):
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", url or "")
    return f"{m.group(1)}/{m.group(2)}".removesuffix(".git") if m else None

repos = sorted({r for e in entries for r in [repo_of(e.get("code"))] if r})
headers = {"Accept": "application/vnd.github+json", "User-Agent": "robot-agents-evals-atlas"}
if os.environ.get("GITHUB_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"

out = {}
batch, batches = [], []
for r in repos:
    if len(" ".join(f"repo:{x}" for x in batch + [r])) > 240:
        batches.append(batch); batch = []
    batch.append(r)
batches.append(batch)
for b in batches:
    q = urllib.parse.quote(" ".join(f"repo:{x}" for x in b))
    req = urllib.request.Request(f"https://api.github.com/search/repositories?q={q}&per_page=100", headers=headers)
    for attempt in range(4):
        try:
            data = json.load(urllib.request.urlopen(req, timeout=30)); break
        except urllib.error.HTTPError as e:
            if e.code in (403, 429): time.sleep(20 * (attempt + 1)); continue
            raise
    for it in data.get("items", []):
        out[it["full_name"].lower()] = {
            "stars": it["stargazers_count"],
            "license": (it.get("license") or {}).get("spdx_id"),
            "pushed_at": it["pushed_at"][:10],
            "archived": it["archived"],
        }
    time.sleep(2 if "Authorization" in headers else 7)

# Search occasionally omits repos; fall back to the repos endpoint (follows renames).
for r in [r for r in repos if r.lower() not in out]:
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{r}", headers=headers)
        it = json.load(urllib.request.urlopen(req, timeout=30))
        out[r.lower()] = {"stars": it["stargazers_count"], "license": (it.get("license") or {}).get("spdx_id"),
                          "pushed_at": it["pushed_at"][:10], "archived": it["archived"],
                          **({"renamed_to": it["full_name"]} if it["full_name"].lower() != r.lower() else {})}
    except Exception as e:
        print("lookup failed", r, e)
missing = [r for r in repos if r.lower() not in out]
result = {"fetched_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"), "repos": out, "not_found": missing}
(ROOT / "data/stars.json").write_text(json.dumps(result, indent=1, sort_keys=True) + "\n")
print(f"{len(out)} repos fetched; not found: {missing}")
