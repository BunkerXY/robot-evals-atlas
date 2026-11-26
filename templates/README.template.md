<!-- ⚠️ GENERATED FILE. Edit templates/README.template.md or data/*.yaml, then run: python scripts/build_readme.py -->
<div align="center">

# 🤖 Robot Agents & Evals Atlas

**Every robot foundation model, agent and benchmark that matters — with links, live GitHub stars, and benchmark scores that each cite their source.**
<br>Includes the **Disaster-Response Eval Gap Map**, a list of first-responder tasks that today's robot benchmarks don't measure yet.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Links](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/links.yml/badge.svg)](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/links.yml)
[![Build](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/build.yml/badge.svg)](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/build.yml)
[![Entries](https://img.shields.io/badge/entries-{{TOTAL}}-blue)](data/atlas.csv)
[![License: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE-CODE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

{{STATS}}

</div>

---

## Why another list?

There are excellent paper lists for [LLM robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics), [embodied AI](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent), [VLAs](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) and [humanoids](https://github.com/YanjieZe/awesome-humanoid-robot-learning). They answer *"what has been published?"* This atlas answers different questions:

1. **"How good is it, really, and according to whom?"** Every score below links to the exact table or README it came from. Blank means nobody has published a comparable number. We don't fill gaps with guesses.
2. **"Which eval should I run?"** There's a [60-second decision guide](docs/which-eval.md) covering sim, real-to-sim, real-world arenas and safety-critical tasks.
3. **"What isn't measured at all?"** The [Disaster-Response Eval Gap Map](#-disaster-response-eval-gap-map) lines up the tasks that matter in fires, collapses and mass-casualty events against what today's benchmarks actually test.
4. **Data, not prose.** Everything lives in [`data/*.yaml`](data/) and is rendered by a script. You can also browse the searchable [`atlas.csv`](data/atlas.csv). Links are checked weekly and stars are refreshed weekly.

## Contents

- [📊 Scoreboard with receipts](#-scoreboard-with-receipts)
- [🧭 Which eval should I use?](#-which-eval-should-i-use)
- [🚨 Disaster-Response Eval Gap Map](#-disaster-response-eval-gap-map)
{{TOC}}
- [🤝 Contributing](#-contributing) · [📚 Citation](#-citation) · [About](#about)

---

## 📊 Scoreboard with receipts

Reported numbers only. Each superscript links to its source, and you can hover over a cell to see the setting. **Don't compare across columns or across sources without reading the protocol.** π0 on LIBERO, for example, is reported as **94.2** in one paper and **86.0** in another, because the training data, number of trials and fine-tuning recipe were different. See [docs/methodology.md](docs/methodology.md).

{{MATRIX}}

<details><summary>Sources & protocols</summary>

{{MATRIX_FOOTNOTES}}

</details>

> Know a properly cited number we're missing? Add one line to [`data/scores.yaml`](data/scores.yaml) with its source URL. PRs that don't cite a source will be closed.

## 🧭 Which eval should I use?

| If you want to know… | Start with | Then confirm with |
|---|---|---|
| Does my VLA fine-tune at all? (quick sanity check) | [LIBERO](https://libero-project.github.io/) | [Meta-World](https://meta-world.github.io/), [CALVIN](https://github.com/mees/calvin) |
| Will sim rankings predict real-robot rankings? | [SimplerEnv](https://simpler-env.github.io/) | [RoboArena](https://robo-arena.github.io/), [AutoEval](https://auto-eval.github.io/) |
| Does it survive distribution shift? | [The Colosseum](https://robot-colosseum.github.io/) | [VLABench](https://vlabench.github.io/), [RoboTwin 2.0](https://robotwin-platform.github.io/) |
| Can it handle long-horizon household tasks? | [BEHAVIOR-1K](https://behavior.stanford.edu/) | [RoboCasa](https://robocasa.ai/), [ALFRED](https://askforalfred.com/) |
| Is my LLM/VLM a good embodied planner? | [EmbodiedBench](https://embodiedbench.github.io/) | [Embodied Agent Interface](https://embodied-agent-interface.github.io/), [ERQA](https://github.com/embodiedreasoning/ERQA) |
| Humanoid whole-body control? | [HumanoidBench](https://humanoid-bench.github.io/) | [Isaac Lab](https://isaac-sim.github.io/IsaacLab/), [MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground) |
| Is it ready for a disaster site? | [NIST Response-Robot Test Methods](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) | [RoboCup Rescue](https://rrl.robocup.org/), [SubT Virtual](https://github.com/osrf/subt) |

The full flowchart and pitfalls are in **[docs/which-eval.md](docs/which-eval.md)**.

## 🚨 Disaster-Response Eval Gap Map

Robot learning is measured almost entirely in clean, well-lit kitchens and on tabletops. Responders work in smoke, rubble, darkness and heat, often with no comms. This table maps real tasks from the [DARPA Robotics Challenge](https://www.darpa.mil/research/programs/darpa-robotics-challenge), [SubT](https://www.darpa.mil/research/challenges/subterranean), the [Triage Challenge](https://triagechallenge.darpa.mil/), MBZIRC and the [NIST test methods](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) to the closest open learning benchmarks. Coverage is our editorial judgement, and we welcome PRs that challenge it.

{{RESPONDER_MAP}}

**Open call:** if you build an open benchmark for any 🔴 row, open a PR and we'll feature it at the top of this section.

---

{{SECTIONS}}

---

## 🤝 Contributing

Add or fix an entry by editing [`data/entries.yaml`](data/entries.yaml), then run `python scripts/validate.py && python scripts/build_readme.py`. Don't edit `README.md` directly. Every entry needs at least one working primary link (paper, project page, code or weights). Every score needs a source URL that points to a specific table. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📚 Citation

If this atlas helps your research, please cite it. GitHub's **"Cite this repository"** button reads [`CITATION.cff`](CITATION.cff).

## About

Maintained by **[Bunker XY](https://bunkerxy.com)**. *Combating death and destruction.* We're building Patriot, a first-responder humanoid robot, and we need honest evals for the places responders actually work. We started this atlas because we needed it ourselves. Inclusion is not an endorsement, and we hold no affiliation with the projects listed unless explicitly stated.

Content is licensed [CC BY 4.0](LICENSE) and scripts are licensed [MIT](LICENSE-CODE).
