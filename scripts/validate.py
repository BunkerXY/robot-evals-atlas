#!/usr/bin/env python3
"""Schema + integrity checks for data/*.yaml. Exit 1 on any problem."""
import pathlib, sys, re
import yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
E = yaml.safe_load((ROOT / "data/entries.yaml").read_text())
S = yaml.safe_load((ROOT / "data/scores.yaml").read_text())
R = yaml.safe_load((ROOT / "data/responder_tasks.yaml").read_text())
SECTIONS = {"vla", "policy", "agent", "humanoid", "world_model", "bench_manip", "bench_embodied", "bench_real",
            "responder", "simulator", "dataset", "tooling"}
ALLOWED = {"id", "name", "section", "year", "org", "summary", "paper", "project", "code", "weights", "tags"}
errs = []
ids = [e.get("id") for e in E]
for e in E:
    where = e.get("id", "?")
    for k in ("id", "name", "section", "summary"):
        if not e.get(k): errs.append(f"{where}: missing {k}")
    if e.get("section") not in SECTIONS: errs.append(f"{where}: bad section {e.get('section')}")
    if set(e) - ALLOWED: errs.append(f"{where}: unknown fields {set(e) - ALLOWED}")
    if not any(e.get(k) for k in ("paper", "project", "code", "weights")): errs.append(f"{where}: needs at least one link")
    for k in ("paper", "project", "code", "weights"):
        if e.get(k) and not re.match(r"https?://", e[k]): errs.append(f"{where}: {k} is not a URL")
    if len(e.get("summary", "")) > 160: errs.append(f"{where}: summary > 160 chars")
dups = {i for i in ids if ids.count(i) > 1}
if dups: errs.append(f"duplicate ids: {dups}")
for s in S["scores"]:
    if s["entry"] not in ids: errs.append(f"score for unknown entry {s['entry']}")
    if s["bench"] not in S["benchmarks"]: errs.append(f"score uses unknown bench {s['bench']}")
    if s["source"] not in S["sources"]: errs.append(f"score uses unknown source {s['source']}")
for k, b in S["benchmarks"].items():
    if b["entry"] not in ids: errs.append(f"benchmark {k} -> unknown entry")
for t in R["tasks"]:
    for i in [t["origin"], *t["proxies"]]:
        if i not in ids: errs.append(f"responder task '{t['task']}' -> unknown id {i}")
print("\n".join(errs) or f"OK: {len(E)} entries, {len(S['scores'])} scores, {len(R['tasks'])} responder tasks")
sys.exit(1 if errs else 0)
