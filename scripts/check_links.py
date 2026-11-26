#!/usr/bin/env python3
"""Check every URL in data/*.yaml (and optionally markdown files). Exit 1 on hard failures.

Usage: python scripts/check_links.py [--md README.md docs/*.md] [--json out.json]
Uses only the standard library + PyYAML so it runs anywhere. CI additionally runs lychee.
"""
import argparse, concurrent.futures as cf, json, re, sys, urllib.request, urllib.error, ssl, pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (robot-agents-evals-atlas link checker; +https://github.com/BunkerXY)"
URL_RE = re.compile(r"https?://[^\s)>\]\"'`|]+")
# Sites that block bots but are known-good when opened in a browser get a soft pass on 403/429.
SOFT = ("doi.org", "physicalintelligence.company", "onlinelibrary.wiley.com", "openai.com", "x.com", "twitter.com", "linkedin.com")

def urls_from_yaml():
    out = {}
    for f in sorted((ROOT / "data").glob("*.yaml")):
        def walk(o, where):
            if isinstance(o, dict):
                for k, v in o.items():
                    walk(v, f"{where}.{k}")
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    walk(v, f"{where}[{i}]")
            elif isinstance(o, str) and o.startswith("http"):
                out.setdefault(o, where)
        walk(yaml.safe_load(f.read_text()), f.name)
    return out

def check(url):
    ctx = ssl.create_default_context()
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 404, 405, 400, 429, 500, 501, 503):
                continue
            return e.code, url
        except Exception as e:  # noqa
            if method == "HEAD":
                continue
            return f"ERR {type(e).__name__}: {e}"[:120], url
    return "ERR", url

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", nargs="*", default=[])
    ap.add_argument("--json")
    a = ap.parse_args()
    urls = urls_from_yaml()
    for m in a.md:
        for u in URL_RE.findall(pathlib.Path(m).read_text()):
            if "github.com/BunkerXY/awesome-robot-agents-evals" in u:
                continue  # our own badges only resolve after publishing
            urls.setdefault(u.rstrip(".,"), m)
    bad, soft, ok = [], [], 0
    with cf.ThreadPoolExecutor(16) as ex:
        for (u, where), (st, final) in zip(urls.items(), ex.map(check, urls)):
            if st == 200 or (isinstance(st, int) and 200 <= st < 400):
                ok += 1
            elif isinstance(st, int) and st in (401, 403, 429, 999) and any(s in u for s in SOFT):
                soft.append((st, u, where))
            else:
                bad.append((st, u, where))
    for st, u, w in bad:
        print(f"BAD  {st}  {u}  ({w})")
    for st, u, w in soft:
        print(f"SOFT {st}  {u}  ({w})")
    print(f"\n{len(urls)} unique URLs: {ok} ok, {len(soft)} soft (bot-blocked), {len(bad)} bad")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps({"total": len(urls), "ok": ok, "soft": soft, "bad": bad}, indent=1))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
