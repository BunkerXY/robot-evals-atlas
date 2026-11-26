<!-- ⚠️ GENERATED FILE. Edit templates/README.template.md or data/*.yaml, then run: python scripts/build_readme.py -->
<div align="center">

# 🤖 Robot Agents & Evals Atlas

**Every robot foundation model, agent and benchmark that matters — with links, live GitHub stars, and benchmark scores that each cite their source.**
<br>Includes the **Disaster-Response Eval Gap Map**, a list of first-responder tasks that today's robot benchmarks don't measure yet.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Links](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/links.yml/badge.svg)](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/links.yml)
[![Build](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/build.yml/badge.svg)](https://github.com/BunkerXY/awesome-robot-agents-evals/actions/workflows/build.yml)
[![Entries](https://img.shields.io/badge/entries-162-blue)](data/atlas.csv)
[![License: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE-CODE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**162** curated entries · **12** categories · **26** cited benchmark scores · **115** open-source repos tracked · stars refreshed **2026-11-26**

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
- [🧠 Vision-Language-Action & Robot Foundation Models](#-vision-language-action--robot-foundation-models) (33)
- [🦾 Visuomotor Policies & Learning Methods](#-visuomotor-policies--learning-methods) (11)
- [🗺️ LLM/VLM Agents, Planners & Embodied Reasoners](#-llmvlm-agents-planners--embodied-reasoners) (18)
- [🚶 Humanoid & Legged Whole-Body Control](#-humanoid--legged-whole-body-control) (9)
- [🌍 World Models](#-world-models) (4)
- [📏 Manipulation Benchmarks](#-manipulation-benchmarks) (15)
- [🏠 Embodied Reasoning, Navigation & Household Benchmarks](#-embodied-reasoning-navigation--household-benchmarks) (10)
- [🏟️ Real-World & Distributed Evaluation](#-real-world--distributed-evaluation) (5)
- [🚒 First-Responder & Disaster-Robotics Evals](#-first-responder--disaster-robotics-evals) (13)
- [🧪 Simulators & Physics Engines](#-simulators--physics-engines) (17)
- [📦 Datasets](#-datasets) (12)
- [🛠️ Tooling, Frameworks & Data-Collection Hardware](#-tooling-frameworks--data-collection-hardware) (15)
- [🤝 Contributing](#-contributing) · [📚 Citation](#-citation) · [About](#about)

---

## 📊 Scoreboard with receipts

Reported numbers only. Each superscript links to its source, and you can hover over a cell to see the setting. **Don't compare across columns or across sources without reading the protocol.** π0 on LIBERO, for example, is reported as **94.2** in one paper and **86.0** in another, because the training data, number of trials and fine-tuning recipe were different. See [docs/methodology.md](docs/methodology.md).

| Model | [LIBERO avg SR (%)](https://arxiv.org/abs/2306.03310) | [CALVIN ABC→D Avg. Len.](https://arxiv.org/abs/2112.03227) | [SimplerEnv Google Robot VM avg (%)](https://arxiv.org/abs/2405.05941) | [SimplerEnv WidowX VM avg (%)](https://arxiv.org/abs/2405.05941) | [Meta-World MT50 avg SR (%)](https://arxiv.org/abs/1910.10897) |
|---|---|---|---|---|---|
| [RT-1](https://arxiv.org/abs/2212.06817) | — | — | 52.4<sup>[5](https://arxiv.org/abs/2411.19650)</sup> | — | — |
| [RT-1-X / RT-2-X (Open X-Embodiment)](https://arxiv.org/abs/2310.08864) | — | — | <span title="RT-2-X (RT-1-X: 42.4)">46.3<sup>[5](https://arxiv.org/abs/2411.19650)</sup></span> | <span title="RT-1-X">1.1<sup>[5](https://arxiv.org/abs/2411.19650)</sup></span> | — |
| [Octo](https://arxiv.org/abs/2405.12213) | <span title="fine-tuned, 3rd-person image">75.1<sup>[1](https://arxiv.org/abs/2502.19645)</sup></span> | — | <span title="Octo-Base">11.0<sup>[5](https://arxiv.org/abs/2411.19650)</sup></span> | <span title="Octo-Base (Octo-Small: 26.7)">17.5<sup>[5](https://arxiv.org/abs/2411.19650)</sup></span> | — |
| [OpenVLA](https://arxiv.org/abs/2406.09246) | <span title="fine-tuned, 3rd-person image">76.5<sup>[1](https://arxiv.org/abs/2502.19645)</sup></span> | — | 34.3<sup>[5](https://arxiv.org/abs/2411.19650)</sup> | 4.2<sup>[5](https://arxiv.org/abs/2411.19650)</sup> | — |
| [OpenVLA-OFT](https://arxiv.org/abs/2502.19645) | <span title="+ wrist cam + proprio, filtered data">97.1<sup>[1](https://arxiv.org/abs/2502.19645)</sup></span> | — | — | — | — |
| [π0 (pi-zero)](https://arxiv.org/abs/2410.24164) | <span title="fine-tuned; baseline as cited in OFT Table I">94.2<sup>[1](https://arxiv.org/abs/2502.19645)</sup></span> / <span title="3.3B, re-trained by SmolVLA authors">86.0<sup>[2](https://arxiv.org/abs/2506.01844)</sup></span> | — | — | — | <span title="3.5B with robot pretraining">47.9<sup>[2](https://arxiv.org/abs/2506.01844)</sup></span> |
| [π0-FAST](https://arxiv.org/abs/2501.09747) | <span title="fine-tuned">85.5<sup>[1](https://arxiv.org/abs/2502.19645)</sup></span> | — | — | — | — |
| [π0.5](https://arxiv.org/abs/2504.16054) | <span title="fine-tuned 30k steps">96.85<sup>[3](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)</sup></span> | — | — | — | — |
| [SmolVLA](https://arxiv.org/abs/2506.01844) | <span title="0.45B, no robot pretraining">87.3<sup>[2](https://arxiv.org/abs/2506.01844)</sup></span> | — | — | — | <span title="0.45B">57.3<sup>[2](https://arxiv.org/abs/2506.01844)</sup></span> |
| [CogACT](https://arxiv.org/abs/2411.19650) | — | — | 74.8<sup>[5](https://arxiv.org/abs/2411.19650)</sup> | 51.3<sup>[5](https://arxiv.org/abs/2411.19650)</sup> | — |
| [TinyVLA](https://arxiv.org/abs/2409.12514) | — | — | — | — | 31.6<sup>[2](https://arxiv.org/abs/2506.01844)</sup> |
| [RoboFlamingo](https://arxiv.org/abs/2311.01378) | — | 2.47<sup>[4](https://arxiv.org/abs/2412.15109)</sup> | — | — | — |
| [GR-1](https://arxiv.org/abs/2312.13139) | — | 3.06<sup>[4](https://arxiv.org/abs/2412.15109)</sup> | — | — | — |
| [Diffusion Policy](https://arxiv.org/abs/2303.04137) | <span title="scratch, 3rd-person image">72.4<sup>[1](https://arxiv.org/abs/2502.19645)</sup></span> | — | — | — | 10.5<sup>[2](https://arxiv.org/abs/2506.01844)</sup> |
| [3D Diffuser Actor](https://arxiv.org/abs/2402.10885) | — | 3.27<sup>[4](https://arxiv.org/abs/2412.15109)</sup> | — | — | — |
| [Seer](https://arxiv.org/abs/2412.15109) | — | <span title="Seer (standard); Seer-Large reports 4.28">3.98<sup>[4](https://arxiv.org/abs/2412.15109)</sup></span> | — | — | — |

<details><summary>Sources & protocols</summary>

<sup>[1]</sup> [OpenVLA-OFT paper (Kim et al., 2025), Table I](https://arxiv.org/abs/2502.19645) — Baselines from original papers or Kim et al. 2024; 500 trials per suite for OpenVLA variants; modified (filtered) LIBERO training data.

<sup>[2]</sup> [SmolVLA paper (Shukor et al., 2025), Table 2](https://arxiv.org/abs/2506.01844) — Multi-task training; 10 trials per task; π0 numbers here are re-trained by the SmolVLA authors.

<sup>[3]</sup> [openpi LIBERO example README (Physical Intelligence)](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md) — π0.5 fine-tuned 30k steps on LIBERO, checkpoint pi05_libero.

<sup>[4]</sup> [Seer paper (Tian et al., 2024), CALVIN ABC→D table](https://arxiv.org/abs/2412.15109) — Average number of consecutively completed tasks out of 5 (Avg. Len.), 1000 rollouts.

<sup>[5]</sup> [CogACT paper (Li et al., 2024), Tables 1–2](https://arxiv.org/abs/2411.19650) — SIMPLER Visual Matching averages; all models trained on Open X-Embodiment except RT-1.

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

| Real-world task | Where it is tested today | Closest learning benchmarks | Coverage | Notes |
|---|---|---|---|---|
| Drive a utility vehicle, then egress | [DARPA Robotics Challenge (DRC)](https://www.darpa.mil/research/programs/darpa-robotics-challenge) | — | 🔴 none | No learning benchmark covers vehicle driving + whole-body egress for a humanoid; DRC remains the reference. |
| Open a door and pass through | [DARPA Robotics Challenge (DRC)](https://www.darpa.mil/research/programs/darpa-robotics-challenge) | [HumanoidBench](https://humanoid-bench.github.io/), [ManiSkill3](https://www.maniskill.ai/), [BEHAVIOR-1K](https://behavior.stanford.edu/), [RoboCasa](https://robocasa.ai/) | 🟡 partial | Sim benchmarks include articulated doors/cabinets, but not heavy, spring-loaded or jammed full-size doors. |
| Turn an industrial valve | [DARPA Robotics Challenge (DRC)](https://www.darpa.mil/research/programs/darpa-robotics-challenge) | [RLBench](https://sites.google.com/view/rlbench), [NIST Standard Test Methods for Response Robots](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) | 🟡 partial | RLBench has tap-turning; NIST has standardized dexterity test methods. Torque-heavy valves are untested in VLA benchmarks. |
| Use a power tool (cut a hole in a wall) | [DARPA Robotics Challenge (DRC)](https://www.darpa.mil/research/programs/darpa-robotics-challenge) | [FurnitureBench](https://clvrai.github.io/furniture-bench/) | 🔴 none | Tool-use with reaction forces is essentially absent from current VLA evals. |
| Cross rubble / uneven terrain | [DARPA Robotics Challenge (DRC)](https://www.darpa.mil/research/programs/darpa-robotics-challenge) | [legged_gym](https://arxiv.org/abs/2109.11978), [HumanoidBench](https://humanoid-bench.github.io/), [NIST Standard Test Methods for Response Robots](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots), [RoboCup Rescue Robot League](https://rrl.robocup.org/) | 🟡 partial | Terrain curricula exist in sim; NIST/RoboCup lanes are the physical standard. |
| Climb stairs and ladders | [DARPA Robotics Challenge (DRC)](https://www.darpa.mil/research/programs/darpa-robotics-challenge) | [HumanoidBench](https://humanoid-bench.github.io/), [legged_gym](https://arxiv.org/abs/2109.11978), [NIST Standard Test Methods for Response Robots](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) | 🟡 partial | Stairs are common in sim curricula; ladders are rarely benchmarked. |
| Explore & map GPS/comms-denied structures, find victims and artifacts | [DARPA Subterranean (SubT) Challenge](https://www.darpa.mil/research/challenges/subterranean) | [SubT Virtual Competition (simulator & worlds)](https://github.com/osrf/subt), [Habitat Navigation Challenge](https://aihabitat.org/challenge/), [VLN-CE](https://jacobkrantz.github.io/vlnce/) | 🟡 partial | SubT Virtual is the closest open eval; household ObjectNav lacks smoke, darkness and comms loss. |
| Detect and prioritise casualties (triage) | [DARPA Triage Challenge](https://triagechallenge.darpa.mil/) | — | 🔴 none | Only the DARPA Triage Challenge measures this; no open robot-learning benchmark does. |
| Locate and suppress a fire | [MBZIRC](https://www.ku.ac.ae/using-drones-to-fight-high-rise-building-fires-presents-a-real-challenge-in-the-mohamed-bin-zayed-international-robotics-challenge-2020) | — | 🔴 none | MBZIRC 2020 Challenge 3 is the main public reference; no open learning benchmark models fire, heat or smoke. |
| Coordinate many responders (multi-agent) | [RoboCup Rescue Simulation League](https://rescuesim.robocup.org/) | [RoboCup Rescue Simulation League](https://rescuesim.robocup.org/) | 🟡 partial | Agent-level simulation only; no embodied multi-robot manipulation benchmark for disaster scenes. |
| Perceive through smoke, dust and darkness | [NIST Standard Test Methods for Response Robots](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) | [NIST Standard Test Methods for Response Robots](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) | 🟡 partial | NIST sensor test methods exist; VLA/VLM benchmarks are almost entirely clean, well-lit scenes. |

**Open call:** if you build an open benchmark for any 🔴 row, open a PR and we'll feature it at the top of this section.

---

## 🧠 Vision-Language-Action & Robot Foundation Models

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **SmolVLA** | 2025 | Hugging Face | 450M-parameter VLA trained on community LeRobot datasets; runs on consumer hardware. | [Paper](https://arxiv.org/abs/2506.01844) · [Code](https://github.com/huggingface/lerobot) · [Weights/Data](https://huggingface.co/lerobot/smolvla_base) | 29.1k | Apache-2.0 |
| **π0-FAST** | 2025 | Physical Intelligence | Autoregressive π0 variant using the FAST DCT-based action tokenizer. | [Paper](https://arxiv.org/abs/2501.09747) · [Site](https://www.physicalintelligence.company/research/fast) · [Code](https://github.com/Physical-Intelligence/openpi) | 14.8k | Apache-2.0 |
| **π0.5** | 2025 | Physical Intelligence | Co-trained VLA aimed at open-world generalization (cleaning unseen homes); weights released in openpi. | [Paper](https://arxiv.org/abs/2504.16054) · [Site](https://www.physicalintelligence.company/blog/pi05) · [Code](https://github.com/Physical-Intelligence/openpi) | 14.8k | Apache-2.0 |
| **π0 (pi-zero)** | 2024 | Physical Intelligence | PaliGemma-based VLA with a flow-matching action expert for high-frequency dexterous control. | [Paper](https://arxiv.org/abs/2410.24164) · [Site](https://www.physicalintelligence.company/blog/pi0) · [Code](https://github.com/Physical-Intelligence/openpi) | 14.8k | Apache-2.0 |
| **GR00T N1 / N1.5** | 2025 | NVIDIA | Open humanoid foundation model with a VLM "System 2" and diffusion-transformer "System 1". | [Paper](https://arxiv.org/abs/2503.14734) · [Site](https://developer.nvidia.com/isaac/gr00t) · [Code](https://github.com/NVIDIA/Isaac-GR00T) · [Weights/Data](https://huggingface.co/nvidia/GR00T-N1.5-3B) | 8.4k | Apache-2.0 |
| **OpenVLA** | 2024 | Stanford, UC Berkeley, TRI, Google DeepMind | 7B open VLA (Llama 2 + DINOv2/SigLIP) trained on 970k OXE episodes; the de-facto open baseline. | [Paper](https://arxiv.org/abs/2406.09246) · [Site](https://openvla.github.io/) · [Code](https://github.com/openvla/openvla) · [Weights/Data](https://huggingface.co/openvla/openvla-7b) | 7.3k | MIT |
| **GO-1 (Genie Operator-1)** | 2025 | AgiBot, Shanghai AI Lab | Generalist policy with latent action planner trained on the AgiBot World dataset. | [Paper](https://arxiv.org/abs/2503.06669) · [Code](https://github.com/OpenDriveLab/AgiBot-World) | 3.2k |  |
| **RT-1-X / RT-2-X (Open X-Embodiment)** | 2023 | Open X-Embodiment Collaboration | RT-1/RT-2 trained on the pooled 22-embodiment Open X-Embodiment dataset to test cross-robot transfer. | [Paper](https://arxiv.org/abs/2310.08864) · [Site](https://robotics-transformer-x.github.io/) · [Code](https://github.com/google-deepmind/open_x_embodiment) | 2.1k | Apache-2.0 |
| **Magma** | 2025 | Microsoft Research | Multimodal foundation model for both digital (UI) and physical (robot) agents. | [Paper](https://arxiv.org/abs/2502.13130) · [Site](https://microsoft.github.io/Magma/) · [Code](https://github.com/microsoft/Magma) | 1.9k | MIT |
| **Octo** | 2024 | UC Berkeley, Stanford, CMU | Open-source transformer diffusion policy pretrained on 800k OXE episodes; small enough to fine-tune on one GPU. | [Paper](https://arxiv.org/abs/2405.12213) · [Site](https://octo-models.github.io/) · [Code](https://github.com/octo-models/octo) · [Weights/Data](https://huggingface.co/rail-berkeley/octo-base-1.5) | 1.9k | MIT |
| **RDT-1B** | 2024 | Tsinghua University | 1.2B diffusion transformer foundation model for bimanual manipulation. | [Paper](https://arxiv.org/abs/2410.07864) · [Site](https://rdt-robotics.github.io/rdt-robotics/) · [Code](https://github.com/thu-ml/RoboticsDiffusionTransformer) · [Weights/Data](https://huggingface.co/robotics-diffusion-transformer/rdt-1b) | 1.8k | MIT |
| **RT-1** | 2022 | Google | Robotics Transformer that tokenizes images + language into discrete actions; trained on 130k real demos. | [Paper](https://arxiv.org/abs/2212.06817) · [Site](https://robotics-transformer1.github.io/) · [Code](https://github.com/google-research/robotics_transformer) | 1.7k 🗄️ | Apache-2.0 |
| **OpenVLA-OFT** | 2025 | Stanford | Optimized fine-tuning recipe (parallel decoding, action chunking, continuous L1 actions) for OpenVLA. | [Paper](https://arxiv.org/abs/2502.19645) · [Site](https://openvla-oft.github.io/) · [Code](https://github.com/moojink/openvla-oft) | 1.5k | MIT |
| **UniVLA** | 2025 | OpenDriveLab (HKU) | Learns task-centric latent actions from videos to train cross-embodiment policies. | [Paper](https://arxiv.org/abs/2505.06111) · [Code](https://github.com/OpenDriveLab/UniVLA) | 1.1k | Apache-2.0 |
| **VIMA** | 2022 | Stanford, NVIDIA | Multimodal-prompt manipulation agent with its own VIMA-Bench. | [Paper](https://arxiv.org/abs/2210.03094) · [Site](https://vimalabs.github.io/) · [Code](https://github.com/vimalabs/VIMA) | 857 | MIT |
| **SpatialVLA** | 2025 | Shanghai AI Lab | Adds ego-centric 3D position encoding and adaptive spatial action grids to a VLA. | [Paper](https://arxiv.org/abs/2501.15830) · [Code](https://github.com/SpatialVLA/SpatialVLA) | 737 |  |
| **HPT (Heterogeneous Pre-trained Transformers)** | 2024 | MIT, Meta | Shared trunk with embodiment-specific stems/heads to pretrain across heterogeneous robots. | [Paper](https://arxiv.org/abs/2409.20537) · [Site](https://liruiw.github.io/hpt/) · [Code](https://github.com/liruiw/HPT) | 547 | MIT |
| **RoboFlamingo** | 2023 | ByteDance Research | Adapts the OpenFlamingo VLM to language-conditioned manipulation on CALVIN. | [Paper](https://arxiv.org/abs/2311.01378) · [Site](https://roboflamingo.github.io/) · [Code](https://github.com/RoboFlamingo/RoboFlamingo) | 439 | MIT |
| **CogACT** | 2024 | Microsoft Research Asia, Tsinghua | VLA that conditions a diffusion action transformer on VLM cognition features. | [Paper](https://arxiv.org/abs/2411.19650) · [Site](https://cogact.github.io/) · [Code](https://github.com/microsoft/CogACT) | 435 | MIT |
| **GR-1** | 2023 | ByteDance Research | GPT-style model pretrained on large-scale video generation, then fine-tuned for manipulation. | [Paper](https://arxiv.org/abs/2312.13139) · [Site](https://gr1-manipulation.github.io/) · [Code](https://github.com/bytedance/GR-1) | 309 | Apache-2.0 |
| **CrossFormer** | 2024 | UC Berkeley | One transformer policy controlling arms, quadrupeds, drones and navigation robots. | [Paper](https://arxiv.org/abs/2408.11812) · [Site](https://crossformer-model.github.io/) · [Code](https://github.com/rail-berkeley/crossformer) | 286 | MIT |
| **DexVLA** | 2025 | Midea Group | VLA with a 1B-parameter diffusion expert and embodiment curriculum for cross-embodiment dexterity. | [Paper](https://arxiv.org/abs/2502.05855) · [Site](https://dex-vla.github.io/) · [Code](https://github.com/juruobenruo/DexVLA) | 74 |  |
| **Gemini Robotics / Gemini Robotics-ER** | 2025 | Google DeepMind | Gemini 2.0-based VLA plus an embodied-reasoning (ER) model for spatial understanding. | [Paper](https://arxiv.org/abs/2503.20020) · [Site](https://deepmind.google/models/gemini-robotics/) |  |  |
| **Gemini Robotics 1.5 / ER 1.5** | 2025 | Google DeepMind | Thinking VLA + agentic ER model that plans multi-step tasks and transfers motions across embodiments. | [Paper](https://arxiv.org/abs/2510.03342) · [Site](https://deepmind.google/models/gemini-robotics/) |  |  |
| **Helix** | 2025 | Figure AI | Dual-system VLA controlling a full humanoid upper body, announced via technical blog (no paper or weights). | [Site](https://www.figure.ai/news/helix) |  |  |
| **Large Behavior Models (TRI)** | 2025 | Toyota Research Institute | Careful statistical study of multitask diffusion "LBMs" with blind, randomized real-world evals. | [Paper](https://arxiv.org/abs/2507.05331) · [Site](https://toyotaresearchinstitute.github.io/lbm1/) |  |  |
| **Hi Robot** | 2025 | Physical Intelligence | Hierarchical VLM high-level policy that handles open-ended instructions and corrections for a VLA. | [Paper](https://arxiv.org/abs/2502.19417) |  |  |
| **TinyVLA** | 2024 | Midea Group, East China Normal University | Compact VLA with a diffusion policy decoder designed for fast inference and data efficiency. | [Paper](https://arxiv.org/abs/2409.12514) · [Site](https://tiny-vla.github.io/) |  |  |
| **GR-2** | 2024 | ByteDance Research | Generative video-language-action model pretrained on 38M web video clips. | [Paper](https://arxiv.org/abs/2410.06158) |  |  |
| **RT-2** | 2023 | Google DeepMind | Co-fine-tunes a web-scale VLM to emit actions as text tokens; the paper that popularised the term VLA. | [Paper](https://arxiv.org/abs/2307.15818) · [Site](https://robotics-transformer2.github.io/) |  |  |
| **PaLM-E** | 2023 | Google | 562B embodied multimodal language model feeding sensor tokens into PaLM for planning. | [Paper](https://arxiv.org/abs/2303.03378) · [Site](https://palm-e.github.io/) |  |  |
| **RoboCat** | 2023 | Google DeepMind | Self-improving generalist agent that generates its own training data across arms. | [Paper](https://arxiv.org/abs/2306.11706) |  |  |
| **Gato** | 2022 | DeepMind | Single generalist transformer policy across games, captioning and real-robot stacking. | [Paper](https://arxiv.org/abs/2205.06175) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🦾 Visuomotor Policies & Learning Methods

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **Diffusion Policy** | 2023 | Columbia, MIT, TRI | Models action sequences with denoising diffusion; now a standard visuomotor baseline. | [Paper](https://arxiv.org/abs/2303.04137) · [Site](https://diffusion-policy.cs.columbia.edu/) · [Code](https://github.com/real-stanford/diffusion_policy) | 4.7k | MIT |
| **Mobile ALOHA** | 2024 | Stanford | Whole-body teleop + co-training for bimanual mobile manipulation. | [Paper](https://arxiv.org/abs/2401.02117) · [Site](https://mobile-aloha.github.io/) · [Code](https://github.com/MarkFzp/mobile-aloha) | 4.5k | MIT |
| **ACT / ALOHA** | 2023 | Stanford | Action Chunking with Transformers trained on low-cost bimanual ALOHA teleop data. | [Paper](https://arxiv.org/abs/2304.13705) · [Site](https://tonyzhaozh.github.io/aloha/) · [Code](https://github.com/tonyzhaozh/act) | 2.4k | MIT |
| **HIL-SERL** | 2024 | UC Berkeley | Human-in-the-loop real-world RL reaching near-perfect success on dexterous tasks. | [Paper](https://arxiv.org/abs/2410.21845) · [Site](https://hil-serl.github.io/) · [Code](https://github.com/rail-berkeley/hil-serl) | 1.6k | Apache-2.0 |
| **3D Diffusion Policy (DP3)** | 2024 | Shanghai Qi Zhi, Tsinghua | Diffusion policy over compact point-cloud representations. | [Paper](https://arxiv.org/abs/2403.03954) · [Site](https://3d-diffusion-policy.github.io/) · [Code](https://github.com/YanjieZe/3D-Diffusion-Policy) | 1.5k | MIT |
| **SERL** | 2024 | UC Berkeley | Sample-efficient real-world RL software suite for manipulation. | [Paper](https://arxiv.org/abs/2401.16013) · [Site](https://serl-robot.github.io/) · [Code](https://github.com/rail-berkeley/serl) | 871 | Apache-2.0 |
| **Dobb-E** | 2023 | NYU, Meta | Home-robot framework with a $20 "Stick" data collector and Home Pretrained Representations. | [Paper](https://arxiv.org/abs/2311.16098) · [Site](https://dobb-e.com/) · [Code](https://github.com/notmahi/dobb-e) | 619 | MIT |
| **PerAct** | 2022 | University of Washington, NVIDIA | Perceiver transformer over voxelized observations for 6-DoF keyframe manipulation. | [Paper](https://arxiv.org/abs/2209.05451) · [Site](https://peract.github.io/) · [Code](https://github.com/peract/peract) | 496 | Apache-2.0 |
| **RVT-2** | 2024 | NVIDIA | Multi-view transformer for precise manipulation from few demonstrations. | [Paper](https://arxiv.org/abs/2406.08545) · [Site](https://robotic-view-transformer-2.github.io/) · [Code](https://github.com/NVlabs/RVT) | 408 |  |
| **3D Diffuser Actor** | 2024 | Carnegie Mellon University | 3D scene-token diffusion policy; strong on RLBench and CALVIN. | [Paper](https://arxiv.org/abs/2402.10885) · [Site](https://3d-diffuser-actor.github.io/) · [Code](https://github.com/nickgkan/3d_diffuser_actor) | 396 | MIT |
| **Seer** | 2024 | Shanghai AI Lab | Predictive inverse dynamics model that jointly forecasts future frames and actions. | [Paper](https://arxiv.org/abs/2412.15109) · [Code](https://github.com/Sage-PhysicalAI/Seer) | 315 | Apache-2.0 |

<sub>[↑ back to top](#contents)</sub>

## 🗺️ LLM/VLM Agents, Planners & Embodied Reasoners

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **Voyager** | 2023 | NVIDIA, Caltech | LLM-powered lifelong-learning agent with an ever-growing skill library (in Minecraft). | [Paper](https://arxiv.org/abs/2305.16291) · [Site](https://voyager.minedojo.org/) · [Code](https://github.com/MineDojo/Voyager) | 7.3k | MIT |
| **Eureka** | 2023 | NVIDIA, UPenn, Caltech | LLM-written reward functions evolved to train dexterous RL policies (e.g. pen spinning). | [Paper](https://arxiv.org/abs/2310.12931) · [Site](https://eureka-research.github.io/) · [Code](https://github.com/eureka-research/Eureka) | 3.2k | MIT |
| **ROSA** | 2024 | NASA JPL | LLM agent that lets operators inspect and command ROS 1/2 systems in natural language. | [Code](https://github.com/nasa-jpl/rosa) | 1.7k | Apache-2.0 |
| **ReKep** | 2024 | Stanford | VLM-generated relational keypoint constraints solved as an optimization for manipulation. | [Paper](https://arxiv.org/abs/2409.01652) · [Site](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) | 1.0k |  |
| **Cosmos-Reason1** | 2025 | NVIDIA | Physical-AI reasoning VLM trained for physical common sense and embodied decisions. | [Paper](https://arxiv.org/abs/2503.15558) · [Code](https://github.com/nvidia-cosmos/cosmos-reason1) | 965 | Apache-2.0 |
| **DrEureka** | 2024 | UPenn, NVIDIA | LLM-guided reward and domain-randomization design for sim-to-real. | [Paper](https://arxiv.org/abs/2406.01967) · [Site](https://eureka-research.github.io/dr-eureka/) · [Code](https://github.com/eureka-research/DrEureka) | 947 | MIT |
| **VoxPoser** | 2023 | Stanford | LLM+VLM compose 3D value maps that a motion planner follows zero-shot. | [Paper](https://arxiv.org/abs/2307.05973) · [Site](https://voxposer.github.io/) · [Code](https://github.com/huangwl18/VoxPoser) | 839 | MIT |
| **OK-Robot** | 2024 | NYU, Meta | Open-knowledge modular pick-and-drop system combining open-vocab perception and grasping. | [Paper](https://arxiv.org/abs/2401.12202) · [Site](https://ok-robot.github.io/) · [Code](https://github.com/ok-robot/ok-robot) | 620 | MIT |
| **RoboPoint** | 2024 | University of Washington, NVIDIA | VLM fine-tuned to predict spatial affordance points from language. | [Paper](https://arxiv.org/abs/2406.10721) · [Site](https://robo-point.github.io/) · [Code](https://github.com/wentaoyuan/RoboPoint) | 233 | Apache-2.0 |
| **LLM-Planner** | 2022 | Ohio State University | Few-shot grounded high-level planning with LLMs, evaluated on ALFRED. | [Paper](https://arxiv.org/abs/2212.04088) · [Site](https://dki-lab.github.io/LLM-Planner/) · [Code](https://github.com/OSU-NLP-Group/LLM-Planner) | 226 | MIT |
| **Text2Reward** | 2023 | HKU, Salesforce | Generates dense, shaped reward code from natural-language goals. | [Paper](https://arxiv.org/abs/2309.11489) · [Site](https://text-to-reward.github.io/) · [Code](https://github.com/xlang-ai/text2reward) | 216 |  |
| **MOKA** | 2024 | UC Berkeley | Mark-based visual prompting so a VLM selects keypoints and waypoints for manipulation. | [Paper](https://arxiv.org/abs/2403.03174) · [Site](https://moka-manipulation.github.io/) · [Code](https://github.com/moka-manipulation/moka) | 103 | MIT |
| **AutoRT** | 2024 | Google DeepMind | Foundation-model orchestration of a robot fleet in the wild with a "robot constitution" for safety. | [Paper](https://arxiv.org/abs/2401.12963) · [Site](https://auto-rt.github.io/) |  |  |
| **SpatialVLM** | 2024 | Google DeepMind | Trains VLMs on synthetic 3D spatial VQA for quantitative spatial reasoning. | [Paper](https://arxiv.org/abs/2401.12168) · [Site](https://spatial-vlm.github.io/) |  |  |
| **SayCan** | 2022 | Google | Grounds LLM task plans with learned value functions ("what's useful" × "what's possible"). | [Paper](https://arxiv.org/abs/2204.01691) · [Site](https://say-can.github.io/) · [Code](https://github.com/google-research/google-research/tree/master/saycan) |  |  |
| **Inner Monologue** | 2022 | Google | Closes the loop by feeding success detection and scene feedback back into the LLM planner. | [Paper](https://arxiv.org/abs/2207.05608) · [Site](https://innermonologue.github.io/) |  |  |
| **Code as Policies** | 2022 | Google | LLM writes robot policy code that calls perception and control APIs. | [Paper](https://arxiv.org/abs/2209.07753) · [Site](https://code-as-policies.github.io/) · [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) |  |  |
| **ProgPrompt** | 2022 | NVIDIA, USC | Pythonic program prompts to generate situated robot task plans. | [Paper](https://arxiv.org/abs/2209.11302) · [Site](https://progprompt.github.io/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🚶 Humanoid & Legged Whole-Body Control

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **Unitree RL Gym** | 2024 | Unitree Robotics | Official Isaac Gym → MuJoCo → real pipeline for Unitree G1/H1 locomotion RL. | [Code](https://github.com/unitreerobotics/unitree_rl_gym) | 3.7k | BSD-3-Clause |
| **legged_gym** | 2021 | ETH Zurich (RSL) | Massively parallel locomotion RL in Isaac Gym ("learning to walk in minutes"). | [Paper](https://arxiv.org/abs/2109.11978) · [Code](https://github.com/leggedrobotics/legged_gym) | 3.2k |  |
| **ASAP** | 2025 | CMU, NVIDIA | Aligns simulation and real-world physics with a learned delta-action model for agile humanoid skills. | [Paper](https://arxiv.org/abs/2502.01143) · [Site](https://agile.human2humanoid.com/) · [Code](https://github.com/LeCAR-Lab/ASAP) | 2.1k | MIT |
| **Humanoid-Gym** | 2024 | RobotEra | RL framework for humanoid locomotion with zero-shot sim-to-real verification. | [Paper](https://arxiv.org/abs/2404.05695) · [Code](https://github.com/roboterax/humanoid-gym) | 2.1k |  |
| **HumanPlus** | 2024 | Stanford | Real-time human shadowing and imitation for a full-size humanoid from a single RGB camera. | [Paper](https://arxiv.org/abs/2406.10454) · [Site](https://humanoid-ai.github.io/) · [Code](https://github.com/MarkFzp/humanplus) | 852 |  |
| **HOVER** | 2024 | NVIDIA, CMU | One neural whole-body controller distilled to support many humanoid control modes. | [Paper](https://arxiv.org/abs/2410.21229) · [Site](https://hover-versatile-humanoid.github.io/) · [Code](https://github.com/NVlabs/HOVER) | 769 | Apache-2.0 |
| **BeyondMimic** | 2025 | UC Berkeley | Motion tracking plus guided diffusion for versatile humanoid control. | [Paper](https://arxiv.org/abs/2508.08241) · [Site](https://beyondmimic.github.io/) |  |  |
| **OmniH2O** | 2024 | CMU | Universal whole-body humanoid teleoperation and autonomy via a kinematic-pose interface. | [Paper](https://arxiv.org/abs/2406.08858) · [Site](https://omni.human2humanoid.com/) |  |  |
| **ExBody2** | 2024 | UC San Diego | Expressive whole-body humanoid motion tracking learned in sim and transferred to real. | [Paper](https://arxiv.org/abs/2412.13196) · [Site](https://exbody2.github.io/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🌍 World Models

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **V-JEPA 2** | 2025 | Meta FAIR | Self-supervised video world model; V-JEPA 2-AC plans zero-shot robot manipulation. | [Paper](https://arxiv.org/abs/2506.09985) · [Code](https://github.com/facebookresearch/vjepa2) | 4.9k | MIT |
| **DreamerV3** | 2023 | DeepMind | General model-based RL agent learning a latent world model across 150+ tasks. | [Paper](https://arxiv.org/abs/2301.04104) · [Site](https://danijar.com/project/dreamerv3/) · [Code](https://github.com/danijar/dreamerv3) | 4.0k | MIT |
| **NVIDIA Cosmos (world foundation models)** | 2025 | NVIDIA | Open world foundation models for generating physical-AI training video and synthetic data. | [Paper](https://arxiv.org/abs/2501.03575) · [Site](https://www.nvidia.com/en-us/ai/cosmos/) · [Code](https://github.com/nvidia-cosmos/cosmos-predict2) | 792 🗄️ | Apache-2.0 |
| **UniSim** | 2023 | Google DeepMind, UC Berkeley | Learned interactive real-world simulator from diverse video for training agents. | [Paper](https://arxiv.org/abs/2310.06114) · [Site](https://universal-simulator.github.io/unisim/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 📏 Manipulation Benchmarks

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **ManiSkill3** | 2024 | UC San Diego (Hao Su Lab) | GPU-parallelized simulation and rendering benchmark for generalizable manipulation. | [Paper](https://arxiv.org/abs/2410.00425) · [Site](https://www.maniskill.ai/) · [Code](https://github.com/mani-skill/ManiSkill) | 3.6k | Apache-2.0 |
| **RoboTwin 2.0** | 2025 | HKU, AgileX and others | Scalable bimanual data generator and benchmark with strong domain randomization. | [Paper](https://arxiv.org/abs/2506.18088) · [Site](https://robotwin-platform.github.io/) · [Code](https://github.com/RoboTwin-Platform/RoboTwin) | 3.1k | MIT |
| **LIBERO** | 2023 | UT Austin | 130 language-conditioned tasks in 4 suites (Spatial/Object/Goal/Long); today's most-reported VLA sim benchmark. | [Paper](https://arxiv.org/abs/2306.03310) · [Site](https://libero-project.github.io/) · [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) | 2.6k | MIT |
| **Meta-World** | 2019 | Stanford, UC Berkeley | 50 MuJoCo manipulation tasks for multi-task and meta-RL (MT/ML suites). | [Paper](https://arxiv.org/abs/1910.10897) · [Site](https://meta-world.github.io/) · [Code](https://github.com/Farama-Foundation/Metaworld) | 1.9k | MIT |
| **RoboCasa** | 2024 | UT Austin, NVIDIA | Large-scale simulated kitchens with generative assets for everyday household tasks. | [Paper](https://arxiv.org/abs/2406.02523) · [Site](https://robocasa.ai/) · [Code](https://github.com/robocasa/robocasa) | 1.9k |  |
| **RLBench** | 2019 | Imperial College London | 100 hand-designed manipulation tasks in CoppeliaSim; standard for 3D keyframe policies. | [Paper](https://arxiv.org/abs/1909.12271) · [Site](https://sites.google.com/view/rlbench) · [Code](https://github.com/stepjam/RLBench) | 1.8k |  |
| **robomimic** | 2021 | Stanford, UT Austin | Framework and benchmark of human-demo datasets for offline imitation learning. | [Paper](https://arxiv.org/abs/2108.03298) · [Site](https://robomimic.github.io/) · [Code](https://github.com/ARISE-Initiative/robomimic) | 1.6k | MIT |
| **SimplerEnv** | 2024 | UC San Diego, Stanford, UC Berkeley, Google DeepMind | Sim environments built to correlate with real Google Robot / WidowX policy rankings. | [Paper](https://arxiv.org/abs/2405.05941) · [Site](https://simpler-env.github.io/) · [Code](https://github.com/simpler-env/SimplerEnv) | 1.2k | MIT |
| **Bi-DexHands** | 2022 | Peking University | Bimanual dexterous-hand RL benchmark in Isaac Gym. | [Paper](https://arxiv.org/abs/2206.08686) · [Code](https://github.com/PKU-MARL/DexterousHands) | 1.1k | Apache-2.0 |
| **CALVIN** | 2021 | University of Freiburg | Long-horizon language-conditioned tabletop benchmark; reports average chain length of 5 instructions. | [Paper](https://arxiv.org/abs/2112.03227) · [Code](https://github.com/mees/calvin) | 1.0k | MIT |
| **VLABench** | 2024 | Fudan University | Language-conditioned long-horizon benchmark probing world knowledge and reasoning in VLAs. | [Paper](https://arxiv.org/abs/2412.18194) · [Site](https://vlabench.github.io/) · [Code](https://github.com/OpenMOSS/VLABench) | 482 | MIT |
| **VIMA-Bench** | 2022 | Stanford, NVIDIA | 17 multimodal-prompt task families with 4 levels of systematic generalization. | [Paper](https://arxiv.org/abs/2210.03094) · [Code](https://github.com/vimalabs/VimaBench) | 330 | MIT |
| **FurnitureBench** | 2023 | KAIST, UC Berkeley | Reproducible real-world long-horizon furniture assembly benchmark (with a sim twin). | [Paper](https://arxiv.org/abs/2305.12821) · [Site](https://clvrai.github.io/furniture-bench/) · [Code](https://github.com/clvrai/furniture-bench) | 244 | MIT |
| **ARNOLD** | 2023 | UCLA, BIGAI | Language-grounded task learning with continuous object states in realistic 3D scenes. | [Paper](https://arxiv.org/abs/2304.04321) · [Site](https://arnold-benchmark.github.io/) · [Code](https://github.com/arnold-benchmark/arnold) | 187 | MIT |
| **The Colosseum** | 2024 | University of Washington, NVIDIA | RLBench extension with 14 perturbation axes to measure generalization drops. | [Paper](https://arxiv.org/abs/2402.08191) · [Site](https://robot-colosseum.github.io/) · [Code](https://github.com/robot-colosseum/robot-colosseum) | 162 |  |

<sub>[↑ back to top](#contents)</sub>

## 🏠 Embodied Reasoning, Navigation & Household Benchmarks

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **Habitat 3.0** | 2023 | Meta FAIR | Co-habitat for humans, avatars and robots; social navigation and rearrangement tasks. | [Paper](https://arxiv.org/abs/2310.13724) · [Site](https://aihabitat.org/habitat3/) · [Code](https://github.com/facebookresearch/habitat-lab) | 3.2k | MIT |
| **BEHAVIOR-1K** | 2024 | Stanford | 1,000 everyday activities defined from a survey of human needs, simulated in OmniGibson. | [Paper](https://arxiv.org/abs/2403.09227) · [Site](https://behavior.stanford.edu/) · [Code](https://github.com/StanfordVL/BEHAVIOR-1K) | 1.8k | MIT |
| **VLN-CE** | 2020 | Oregon State, Georgia Tech, Meta | Vision-and-language navigation in continuous environments (Habitat). | [Paper](https://arxiv.org/abs/2004.02857) · [Site](https://jacobkrantz.github.io/vlnce/) · [Code](https://github.com/jacobkrantz/VLN-CE) | 906 | MIT |
| **HumanoidBench** | 2024 | UC Berkeley, Yonsei | 27 simulated humanoid locomotion and whole-body manipulation tasks. | [Paper](https://arxiv.org/abs/2403.10506) · [Site](https://humanoid-bench.github.io/) · [Code](https://github.com/carlosferrazza/humanoid-bench) | 807 |  |
| **ALFRED** | 2020 | University of Washington, AI2 | Language instructions → action sequences for household tasks in AI2-THOR. | [Paper](https://arxiv.org/abs/1912.01734) · [Site](https://askforalfred.com/) · [Code](https://github.com/askforalfred/alfred) | 533 | MIT |
| **OpenEQA** | 2024 | Meta FAIR | Open-vocabulary embodied question answering from episodic memory and active exploration. | [Paper](https://open-eqa.github.io/assets/pdfs/paper.pdf) · [Site](https://open-eqa.github.io/) · [Code](https://github.com/facebookresearch/open-eqa) | 363 🗄️ | MIT |
| **EmbodiedBench** | 2025 | UIUC and others | Evaluates multimodal LLMs as embodied agents from high-level planning to low-level manipulation. | [Paper](https://arxiv.org/abs/2502.09560) · [Site](https://embodiedbench.github.io/) · [Code](https://github.com/EmbodiedBench/EmbodiedBench) | 362 |  |
| **ERQA (Embodied Reasoning QA)** | 2025 | Google DeepMind | Multiple-choice VQA benchmark for embodied spatial and physical reasoning, released with Gemini Robotics. | [Paper](https://arxiv.org/abs/2503.20020) · [Code](https://github.com/embodiedreasoning/ERQA) | 340 | CC-BY-4.0 |
| **Embodied Agent Interface** | 2024 | Stanford | Fine-grained error taxonomy for LLMs on goal interpretation, subgoals, action sequencing and transition modeling. | [Paper](https://arxiv.org/abs/2410.07166) · [Site](https://embodied-agent-interface.github.io/) · [Code](https://github.com/embodied-agent-interface/embodied-agent-interface) | 303 | MIT |
| **Habitat Navigation Challenge** | 2019 | Meta FAIR and partners | Annual ObjectNav / ImageNav challenge with a hosted EvalAI leaderboard. | [Site](https://aihabitat.org/challenge/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🏟️ Real-World & Distributed Evaluation

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **RoboArena** | 2025 | UC Berkeley, Stanford, UW and others | Crowd-sourced, double-blind pairwise real-robot evaluation of generalist policies on DROID setups. | [Paper](https://arxiv.org/abs/2506.18123) · [Site](https://robo-arena.github.io/) |  |  |
| **AutoEval** | 2025 | UC Berkeley | Autonomous real-world evaluation stations (with learned reset and success detection) open to the public. | [Paper](https://arxiv.org/abs/2503.24278) · [Site](https://auto-eval.github.io/) |  |  |
| **RoboChallenge** | 2025 | RoboChallenge | Hosted real-robot benchmark (Table30, Table30 V2, ZERO) where submitted VLA/VLM policies run on physical robots. | [Site](https://robochallenge.ai/) |  |  |
| **YCB Object and Model Set** | 2015 | Yale, CMU, UC Berkeley | Shared physical object set and protocols for reproducible manipulation benchmarking. | [Paper](https://arxiv.org/abs/1502.03143) |  |  |
| **RoboCup@Home** | 2006 | RoboCup Federation | Annual service-robot competition with standardized domestic tasks scored by referees. | [Site](https://athome.robocup.org/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🚒 First-Responder & Disaster-Robotics Evals

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **SubT Virtual Competition (simulator & worlds)** | 2021 | Open Robotics, DARPA | Open-source Gazebo-based SubT simulation, worlds and robot models used in the virtual track. | [Code](https://github.com/osrf/subt) | 372 |  |
| **DARPA Triage Challenge** | 2024 | DARPA | Multi-year challenge on autonomous detection of physiological signatures for mass-casualty triage. | [Site](https://triagechallenge.darpa.mil/) |  |  |
| **CERBERUS (SubT Final winner)** | 2022 | NTNU, ETH Zurich, UC Berkeley and others | Field report of the legged + aerial team that won the SubT Final Event. | [Paper](https://arxiv.org/abs/2207.04914) |  |  |
| **DARPA Subterranean (SubT) Challenge** | 2021 | DARPA | Autonomous robot teams mapping and searching tunnels, urban underground and caves under comms loss. | [Site](https://www.darpa.mil/research/challenges/subterranean) |  |  |
| **NeBula (Team CoSTAR)** | 2021 | NASA JPL, Caltech, MIT, KAIST and others | Uncertainty-aware autonomy architecture for SubT exploration across robot types. | [Paper](https://arxiv.org/abs/2103.11470) |  |  |
| **CENTAURO** | 2019 | EU Horizon 2020 consortium | Centaur-like disaster-response robot evaluated on realistic nuclear/rubble/door/tool tasks. | [Paper](https://arxiv.org/abs/1909.08812) · [Site](https://www.centauro-project.eu/) |  |  |
| **World Robot Summit — Disaster Robotics** | 2018 | METI / NEDO (Japan) | Plant disaster prevention, tunnel disaster response and standard disaster robotics challenges. | [Site](https://worldrobotsummit.org/en/) |  |  |
| **MBZIRC** | 2017 | Khalifa University | International robotics challenge; 2020 Challenge 3 had UAV/UGV teams autonomously extinguish fires in a high-rise mock-up (paper = a team report). | [Paper](https://arxiv.org/abs/2104.01834) · [Site](https://www.ku.ac.ae/using-drones-to-fight-high-rise-building-fires-presents-a-real-challenge-in-the-mohamed-bin-zayed-international-robotics-challenge-2020) |  |  |
| **DARPA Robotics Challenge (DRC)** | 2015 | DARPA | 2012–2015 disaster-response challenge — drive a vehicle, egress, open a door, turn a valve, cut drywall, cross rubble, climb stairs. | [Paper](https://doi.org/10.1002/rob.21683) · [Site](https://www.darpa.mil/research/programs/darpa-robotics-challenge) |  |  |
| **ELROB (European Land Robot Trial)** | 2006 | FKIE / European partners | Field trials for unmanned ground systems including reconnaissance, CBRN and rescue scenarios. | [Site](https://www.elrob.org/) |  |  |
| **NIST Standard Test Methods for Response Robots** | 2005 | NIST | ASTM-standardized test methods (mobility, manipulation, sensors, comms, endurance) for emergency response robots. | [Site](https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots) |  |  |
| **RoboCup Rescue Robot League** | 2001 | RoboCup Federation | Competition using NIST-style test lanes for mobility, dexterity and victim detection. | [Site](https://rrl.robocup.org/) |  |  |
| **RoboCup Rescue Simulation League** | 2001 | RoboCup Federation | Multi-agent simulation of earthquake response (fire brigades, ambulances, police). | [Site](https://rescuesim.robocup.org/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🧪 Simulators & Physics Engines

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **Genesis** | 2024 | Genesis-Embodied-AI | Universal Python physics platform (rigid, soft, fluid) for robotics and embodied AI. | [Site](https://genesis-embodied-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/genesis-world) | 30.3k | Apache-2.0 |
| **AirSim** | 2017 | Microsoft | Unreal Engine-based drone and vehicle simulator widely used for aerial search and inspection research. | [Paper](https://arxiv.org/abs/1705.05065) · [Code](https://github.com/microsoft/AirSim) | 18.6k |  |
| **MuJoCo** | 2012 | Google DeepMind | Fast, accurate contact-rich physics engine; default for policy research. | [Site](https://mujoco.org/) · [Code](https://github.com/google-deepmind/mujoco) | 18.5k | Apache-2.0 |
| **PyBullet** | 2016 | Bullet Physics | Python bindings for the Bullet physics SDK; lightweight and widely used. | [Site](https://pybullet.org/) · [Code](https://github.com/bulletphysics/bullet3) | 14.9k |  |
| **Isaac Lab** | 2023 | NVIDIA | GPU-accelerated robot learning framework on Isaac Sim (successor to Orbit / Isaac Gym envs). | [Paper](https://arxiv.org/abs/2301.04195) · [Site](https://isaac-sim.github.io/IsaacLab/) · [Code](https://github.com/isaac-sim/IsaacLab) | 8.7k |  |
| **Newton** | 2025 | Linux Foundation (NVIDIA, Google DeepMind, Disney Research) | Open-source GPU physics engine built on NVIDIA Warp for robot learning. | [Code](https://github.com/newton-physics/newton) | 6.0k | Apache-2.0 |
| **Webots** | 1998 | Cyberbotics | Open-source multi-platform robot simulator with a large robot library. | [Site](https://cyberbotics.com/) · [Code](https://github.com/cyberbotics/webots) | 4.8k | Apache-2.0 |
| **MuJoCo Menagerie** | 2022 | Google DeepMind | Curated, high-quality robot models (humanoids, quadrupeds, arms, hands) for MuJoCo. | [Code](https://github.com/google-deepmind/mujoco_menagerie) | 4.4k |  |
| **Drake** | 2014 | Toyota Research Institute, MIT | Model-based design, optimization and simulation toolbox with rigorous contact. | [Site](https://drake.mit.edu/) · [Code](https://github.com/RobotLocomotion/drake) | 4.3k |  |
| **Habitat-Sim** | 2019 | Meta FAIR | High-throughput 3D simulator for embodied navigation and rearrangement. | [Paper](https://arxiv.org/abs/1904.01201) · [Site](https://aihabitat.org/) · [Code](https://github.com/facebookresearch/habitat-sim) | 3.8k 🗄️ | MIT |
| **Brax** | 2021 | Google | Differentiable JAX physics for massively parallel RL. | [Paper](https://arxiv.org/abs/2106.13281) · [Code](https://github.com/google/brax) | 3.3k | Apache-2.0 |
| **robosuite** | 2020 | Stanford, UT Austin | Modular MuJoCo-based manipulation simulation framework and benchmark. | [Paper](https://arxiv.org/abs/2009.12293) · [Site](https://robosuite.ai/) · [Code](https://github.com/ARISE-Initiative/robosuite) | 2.7k |  |
| **MuJoCo Playground** | 2025 | Google DeepMind, UC Berkeley and others | GPU (MJX) environments for locomotion and manipulation with sim-to-real recipes. | [Paper](https://arxiv.org/abs/2502.08844) · [Code](https://github.com/google-deepmind/mujoco_playground) | 2.3k | Apache-2.0 |
| **AI2-THOR / ProcTHOR** | 2017 | Allen Institute for AI | Interactive household simulator; ProcTHOR procedurally generates 10k+ houses. | [Paper](https://arxiv.org/abs/1712.05474) · [Site](https://ai2thor.allenai.org/) · [Code](https://github.com/allenai/ai2thor) | 1.8k | Apache-2.0 |
| **Gazebo** | 2004 | Open Robotics | ROS-native robot simulator used by DARPA SubT virtual and many field robots. | [Site](https://gazebosim.org/) · [Code](https://github.com/gazebosim/gz-sim) | 1.6k | Apache-2.0 |
| **SAPIEN** | 2020 | UC San Diego | Physics-rich simulator for articulated objects; backend of ManiSkill. | [Paper](https://arxiv.org/abs/2003.08515) · [Code](https://github.com/haosulab/SAPIEN) | 874 |  |
| **CoppeliaSim** | 2010 | Coppelia Robotics | General-purpose robot simulator (formerly V-REP); backend of RLBench. | [Site](https://www.coppeliarobotics.com/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 📦 Datasets

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **AgiBot World** | 2025 | AgiBot, Shanghai AI Lab | Large-scale humanoid/dual-arm manipulation dataset collected in a dedicated data factory. | [Paper](https://arxiv.org/abs/2503.06669) · [Site](https://agibot-world.com/) · [Code](https://github.com/OpenDriveLab/AgiBot-World) | 3.2k |  |
| **Open X-Embodiment** | 2023 | 21 institutions | 1M+ real trajectories across 22 robot embodiments, pooled in RLDS format. | [Paper](https://arxiv.org/abs/2310.08864) · [Site](https://robotics-transformer-x.github.io/) · [Code](https://github.com/google-deepmind/open_x_embodiment) | 2.1k | Apache-2.0 |
| **MimicGen** | 2023 | NVIDIA, UT Austin | Generates 50k+ demos from ~200 human demos by adapting them to new scenes. | [Paper](https://arxiv.org/abs/2310.17596) · [Site](https://mimicgen.github.io/) · [Code](https://github.com/NVlabs/mimicgen) | 676 |  |
| **DROID** | 2024 | Stanford, UC Berkeley, TRI and others | 76k in-the-wild Franka teleop trajectories across 564 scenes and 86 tasks. | [Paper](https://arxiv.org/abs/2403.12945) · [Site](https://droid-dataset.github.io/) · [Code](https://github.com/droid-dataset/droid) | 474 |  |
| **Language-Table** | 2022 | Google | ~600k language-annotated trajectories for interactive real-time language-guided pushing. | [Paper](https://arxiv.org/abs/2210.06407) · [Site](https://interactive-language.github.io/) · [Code](https://github.com/google-research/language-table) | 368 | Apache-2.0 |
| **EgoDex** | 2025 | Apple | 829 hours of egocentric video with 3D hand/finger tracking for dexterous manipulation. | [Paper](https://arxiv.org/abs/2505.11709) |  |  |
| **PhysicalAI-Robotics-GR00T-X-Embodiment-Sim** | 2025 | NVIDIA | Synthetic humanoid and arm trajectories released alongside GR00T N1. | [Weights/Data](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim) |  |  |
| **LeRobot community datasets** | 2024 | Hugging Face community | Thousands of community-uploaded robot datasets in the LeRobot format on the Hub. | [Site](https://huggingface.co/lerobot) |  |  |
| **BridgeData V2** | 2023 | UC Berkeley | 60k WidowX trajectories across 24 environments for generalizable skills. | [Paper](https://arxiv.org/abs/2308.12952) · [Site](https://rail-berkeley.github.io/bridgedata/) |  |  |
| **RH20T** | 2023 | Shanghai Jiao Tong University | Multi-modal (force, audio, depth) contact-rich manipulation dataset with paired human videos. | [Paper](https://arxiv.org/abs/2307.00595) · [Site](https://rh20t.github.io/) |  |  |
| **Ego4D** | 2021 | Meta-led academic consortium | 3,670 hours of egocentric video; common pretraining source for robot representations. | [Paper](https://arxiv.org/abs/2110.07058) · [Site](https://ego4d-data.org/) |  |  |
| **RoboNet** | 2019 | UC Berkeley, Stanford, UPenn | Early multi-robot dataset (15M frames, 7 platforms) for transferable visual models. | [Paper](https://arxiv.org/abs/1910.11215) · [Site](https://www.robonet.wiki/) |  |  |

<sub>[↑ back to top](#contents)</sub>

## 🛠️ Tooling, Frameworks & Data-Collection Hardware

| Name | Year | Who | What it is | Links | ⭐ | License |
|---|---|---|---|---|---|---|
| **LeRobot** | 2024 | Hugging Face | End-to-end PyTorch library for real-robot datasets, policies (ACT, Diffusion, SmolVLA, π0) and hardware. | [Site](https://huggingface.co/lerobot) · [Code](https://github.com/huggingface/lerobot) | 29.1k | Apache-2.0 |
| **openpi** | 2025 | Physical Intelligence | Code and checkpoints for π0, π0-FAST and π0.5 with fine-tuning examples. | [Code](https://github.com/Physical-Intelligence/openpi) | 14.8k | Apache-2.0 |
| **Rerun** | 2022 | Rerun | Multimodal logging and visualization SDK widely used for robot data. | [Site](https://rerun.io/) · [Code](https://github.com/rerun-io/rerun) | 11.9k | Apache-2.0 |
| **Isaac GR00T** | 2025 | NVIDIA | Fine-tuning and deployment code for GR00T N1.x humanoid models. | [Code](https://github.com/NVIDIA/Isaac-GR00T) | 8.4k | Apache-2.0 |
| **SO-ARM100 / SO-101** | 2024 | The Robot Studio, Hugging Face | Low-cost 3D-printable arm design used widely by the LeRobot community. | [Code](https://github.com/TheRobotStudio/SO-ARM100) | 8.2k | Apache-2.0 |
| **ROS 2** | 2017 | Open Robotics | The standard robotics middleware; real-time-capable successor to ROS. | [Site](https://docs.ros.org/) · [Code](https://github.com/ros2/ros2) | 6.4k |  |
| **Nav2** | 2020 | Open Navigation and community | ROS 2 navigation stack with behavior trees. | [Site](https://docs.nav2.org/) · [Code](https://github.com/ros-navigation/navigation2) | 5.1k |  |
| **dora-rs** | 2022 | dora-rs community | Low-latency dataflow middleware for AI-based robotic applications. | [Site](https://dora-rs.ai/) · [Code](https://github.com/dora-rs/dora) | 4.1k | Apache-2.0 |
| **RSL-RL** | 2022 | ETH Zurich (RSL) | Fast GPU PPO implementation used by legged_gym and Isaac Lab. | [Code](https://github.com/leggedrobotics/rsl_rl) | 3.2k |  |
| **ALOHA hardware** | 2023 | Stanford | Open-source low-cost bimanual teleoperation rig. | [Code](https://github.com/tonyzhaozh/aloha) | 2.4k | MIT |
| **MoveIt 2** | 2019 | PickNik and community | Motion planning, manipulation and collision checking for ROS 2. | [Site](https://moveit.ai/) · [Code](https://github.com/moveit/moveit2) | 2.1k | BSD-3-Clause |
| **UMI (Universal Manipulation Interface)** | 2024 | Stanford, Columbia, TRI | Hand-held gripper data collector whose demos transfer directly to robot policies. | [Paper](https://arxiv.org/abs/2402.10329) · [Site](https://umi-gripper.github.io/) · [Code](https://github.com/real-stanford/universal_manipulation_interface) | 1.6k | MIT |
| **Open-TeleVision** | 2024 | UC San Diego, MIT | Immersive VR teleoperation with active stereo vision for humanoids. | [Paper](https://arxiv.org/abs/2407.01512) · [Site](https://robot-tv.github.io/) · [Code](https://github.com/OpenTeleVision/TeleVision) | 1.3k |  |
| **GELLO** | 2023 | UC Berkeley | Low-cost kinematically-matched teleoperation leader arms. | [Paper](https://arxiv.org/abs/2309.13037) · [Site](https://wuphilipp.github.io/gello_site/) · [Code](https://github.com/wuphilipp/gello_software) | 569 | MIT |
| **RLDS** | 2021 | Google Research | Episode/step dataset format used by Open X-Embodiment. | [Paper](https://arxiv.org/abs/2111.02767) · [Code](https://github.com/google-research/rlds) | 492 🗄️ | Apache-2.0 |

<sub>[↑ back to top](#contents)</sub>


---

## 🤝 Contributing

Add or fix an entry by editing [`data/entries.yaml`](data/entries.yaml), then run `python scripts/validate.py && python scripts/build_readme.py`. Don't edit `README.md` directly. Every entry needs at least one working primary link (paper, project page, code or weights). Every score needs a source URL that points to a specific table. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📚 Citation

If this atlas helps your research, please cite it. GitHub's **"Cite this repository"** button reads [`CITATION.cff`](CITATION.cff).

## About

Maintained by **[Bunker XY](https://bunkerxy.com)**. *Combating death and destruction.* We're building Patriot, a first-responder humanoid robot, and we need honest evals for the places responders actually work. We started this atlas because we needed it ourselves. Inclusion is not an endorsement, and we hold no affiliation with the projects listed unless explicitly stated.

Content is licensed [CC BY 4.0](LICENSE) and scripts are licensed [MIT](LICENSE-CODE).
