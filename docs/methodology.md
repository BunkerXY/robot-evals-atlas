# Methodology

## What gets in

An entry belongs in the Atlas if it meets **at least one** of these:

- It's a model, agent, benchmark, simulator, dataset or tool that other work uses widely (papers report it, or the repo is actively used).
- It introduced an idea that changed how people evaluate robots (for example real-to-sim correlation, crowd-sourced pairwise evals, or standardized response-robot test methods).
- It fills a gap in the [Disaster-Response Eval Gap Map](../README.md#-disaster-response-eval-gap-map).

Every entry links to a primary source: the paper, an official project page, the official code or official weights. We don't use secondary blog posts.

## Rules for scores

1. **Cited or blank.** A number goes into `data/scores.yaml` only with a `source` that points to a specific table or README. If there's no source, the cell stays blank.
2. **Copied, not re-run.** We record numbers exactly as their source published them. We don't normalize them.
3. **Settings travel with the number.** The `setting` field records anything that changes comparability.
4. **Conflicting sources are both shown.** For example, π0 on LIBERO appears as `94.2 / 86.0`, from the [OpenVLA-OFT](https://arxiv.org/abs/2502.19645) and [SmolVLA](https://arxiv.org/abs/2506.01844) papers.

## Stars, licenses and freshness

`scripts/fetch_stars.py` pulls the star count, SPDX license, last push date and archived flag for every repo-root GitHub link through the GitHub API. A scheduled workflow refreshes them weekly and opens a pull request. Stars are only a rough popularity signal, not a measure of quality. Links that point to a subfolder of a monorepo, like SayCan inside `google-research`, don't get a star count, because the count would be for the whole monorepo.

## Link health

There are two layers. `scripts/check_links.py` (Python stdlib) checks every URL in `data/`, and [lychee](https://github.com/lycheeverse/lychee) checks the rendered Markdown. Some sites block automated checkers (they return 403 or 429). Those are allow-listed as "soft" only after someone confirms them by hand in a browser.

## Gap Map coverage ratings

- 🔴 **none**: no open learning benchmark tests the task.
- 🟡 **partial**: related skills are tested, but the hazard, the scale or the physical demands aren't.
- 🟢 **good**: an open benchmark tests the task under realistic conditions.

These are editorial judgements. If you disagree, open a PR with your reasoning and links.
