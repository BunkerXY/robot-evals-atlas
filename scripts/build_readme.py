#!/usr/bin/env python3
"""Generate README.md and data/atlas.csv from data/*.yaml + data/stars.json.
Run: python scripts/build_readme.py   (CI fails if the committed README is stale)."""
import csv, json, pathlib, re, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
entries = yaml.safe_load((D / "entries.yaml").read_text())
scores = yaml.safe_load((D / "scores.yaml").read_text())
responder = yaml.safe_load((D / "responder_tasks.yaml").read_text())
stars = json.loads((D / "stars.json").read_text()) if (D / "stars.json").exists() else {"repos": {}, "fetched_at": "n/a"}
by_id = {e["id"]: e for e in entries}

SECTIONS = [
    ("vla", "🧠 Vision-Language-Action & Robot Foundation Models"),
    ("policy", "🦾 Visuomotor Policies & Learning Methods"),
    ("agent", "🗺️ LLM/VLM Agents, Planners & Embodied Reasoners"),
    ("humanoid", "🚶 Humanoid & Legged Whole-Body Control"),
    ("world_model", "🌍 World Models"),
    ("bench_manip", "📏 Manipulation Benchmarks"),
    ("bench_embodied", "🏠 Embodied Reasoning, Navigation & Household Benchmarks"),
    ("bench_real", "🏟️ Real-World & Distributed Evaluation"),
    ("responder", "🚒 First-Responder & Disaster-Robotics Evals"),
    ("simulator", "🧪 Simulators & Physics Engines"),
    ("dataset", "📦 Datasets"),
    ("tooling", "🛠️ Tooling, Frameworks & Data-Collection Hardware"),
]

def repo_of(url):
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)/?$", url or "")
    return f"{m.group(1)}/{m.group(2)}" if m else None

def star_info(e):
    r = repo_of(e.get("code"))
    return stars["repos"].get(r.lower()) if r else None

def fmt_stars(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)

def slug(s):
    # GitHub anchor rules: lowercase, drop punctuation/emoji, spaces -> hyphens (leading hyphen kept).
    s = re.sub(r"[^\w\- ]", "", s.lower())
    return s.replace(" ", "-")

def links(e):
    out = []
    for k, label in (("paper", "Paper"), ("project", "Site"), ("code", "Code"), ("weights", "Weights/Data")):
        if e.get(k):
            out.append(f"[{label}]({e[k]})")
    return " · ".join(out)

def section_table(sec):
    rows = [e for e in entries if e["section"] == sec]
    rows.sort(key=lambda e: (-(star_info(e) or {}).get("stars", -1), -int(e.get("year") or 0)))
    lines = ["| Name | Year | Who | What it is | Links | ⭐ | License |", "|---|---|---|---|---|---|---|"]
    for e in rows:
        si = star_info(e) or {}
        st = fmt_stars(si["stars"]) if "stars" in si else ""
        if si.get("archived"):
            st += " 🗄️"
        lic = si.get("license") or ""
        lic = "" if lic == "NOASSERTION" else lic
        lines.append(f"| **{e['name']}** | {e.get('year','')} | {e.get('org','')} | {e['summary']} | {links(e)} | {st} | {lic} |")
    return "\n".join(lines), len(rows)

def matrix():
    benches = scores["benchmarks"]; srcs = scores["sources"]
    keys = list(benches)
    foot, foot_ids = [], {}
    def ref(src):
        if src not in foot_ids:
            foot_ids[src] = len(foot_ids) + 1
            foot.append(f"<sup>[{foot_ids[src]}]</sup> [{srcs[src]['title']}]({srcs[src]['url']}) — {srcs[src]['note']}")
        return foot_ids[src]
    cells = {}
    for s in scores["scores"]:
        txt = f"{s['value']}<sup>[{ref(s['source'])}]({srcs[s['source']]['url']})</sup>"
        if s.get("setting"):
            txt = f"<span title=\"{s['setting']}\">{txt}</span>"
        cells.setdefault(s["entry"], {}).setdefault(s["bench"], []).append(txt)
    order = [e["id"] for e in entries if e["id"] in cells]
    head = "| Model | " + " | ".join(f"[{benches[k]['name']}]({by_id[benches[k]['entry']]['paper']})" for k in keys) + " |"
    lines = [head, "|---|" + "---|" * len(keys)]
    for i in order:
        e = by_id[i]
        row = [" / ".join(cells[i].get(k, [])) or "—" for k in keys]
        lines.append(f"| [{e['name']}]({e.get('paper') or e.get('project') or e.get('code')}) | " + " | ".join(row) + " |")
    return "\n".join(lines), "\n\n".join(foot), len(scores["scores"])

def responder_map():
    icon = {"none": "🔴 none", "partial": "🟡 partial", "good": "🟢 good"}
    lines = ["| Real-world task | Where it is tested today | Closest learning benchmarks | Coverage | Notes |", "|---|---|---|---|---|"]
    for t in responder["tasks"]:
        o = by_id[t["origin"]]
        prox = ", ".join(f"[{by_id[p]['name']}]({by_id[p].get('project') or by_id[p].get('paper') or by_id[p].get('code')})" for p in t["proxies"]) or "—"
        lines.append(f"| {t['task']} | [{o['name']}]({o.get('project') or o.get('paper') or o.get('code')}) | {prox} | {icon[t['coverage']]} | {t['note']} |")
    return "\n".join(lines)

def main():
    tpl = (ROOT / "templates/README.template.md").read_text()
    body, toc, counts = [], [], {}
    for sec, title in SECTIONS:
        tbl, n = section_table(sec)
        counts[sec] = n
        body.append(f"## {title}\n\n{tbl}\n\n<sub>[↑ back to top](#contents)</sub>\n")
        toc.append(f"- [{title}](#{slug(title)}) ({n})")
    mtx, foot, nscores = matrix()
    total = len(entries)
    n_repos = sum(1 for e in entries if star_info(e))
    stats = (f"**{total}** curated entries · **{len(SECTIONS)}** categories · **{nscores}** cited benchmark scores · "
             f"**{n_repos}** open-source repos tracked · stars refreshed **{stars['fetched_at']}**")
    out = (tpl.replace("{{STATS}}", stats).replace("{{TOC}}", "\n".join(toc)).replace("{{MATRIX}}", mtx)
              .replace("{{MATRIX_FOOTNOTES}}", foot).replace("{{RESPONDER_MAP}}", responder_map())
              .replace("{{SECTIONS}}", "\n".join(body)).replace("{{TOTAL}}", str(total)))
    (ROOT / "README.md").write_text(out)
    with open(D / "atlas.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "section", "year", "org", "summary", "paper", "project", "code", "weights", "stars", "license", "last_push", "tags"])
        for e in entries:
            si = star_info(e) or {}
            w.writerow([e["id"], e["name"], e["section"], e.get("year", ""), e.get("org", ""), e["summary"], e.get("paper", ""),
                        e.get("project", ""), e.get("code", ""), e.get("weights", ""), si.get("stars", ""), si.get("license", "") or "",
                        si.get("pushed_at", ""), ";".join(e.get("tags", []))])
    print(f"README.md written: {total} entries, {nscores} scores", counts)

if __name__ == "__main__":
    main()
