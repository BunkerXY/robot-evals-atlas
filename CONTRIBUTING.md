# Contributing

Thanks for helping make robot evaluation more honest! 🎉

## Add or fix an entry

1. Edit `data/entries.yaml`. Copy an existing block and keep it in the right section.
   - Required fields are `id` (kebab-case and unique), `name`, `section`, `summary` (160 characters or fewer, factual, no hype) and at least one of `paper` / `project` / `code` / `weights`.
   - Use **primary sources only**: arXiv/DOI, the official project page, the official repo, or official weights.
2. Run:
   ```bash
   pip install pyyaml
   python scripts/validate.py
   python scripts/build_readme.py
   python scripts/check_links.py   # optional locally; CI runs it
   ```
3. Commit both `data/` and the regenerated `README.md` / `data/atlas.csv`.

## Add a benchmark score

Add one line to `data/scores.yaml`:

```yaml
- {entry: my-model, bench: libero_avg, value: 91.2, source: my_source, setting: "fine-tuned, wrist cam"}
```

…and if it's a new source, add it under `sources:` with the URL **of the paper or leaderboard that holds the table**. Numbers that don't have a specific citable source will be rejected.

## Propose a Gap Map change

Edit `data/responder_tasks.yaml`. If you think a task's coverage should go up, link the benchmark that you think tests it under realistic conditions.

## Style

- Neutral wording. Don't call anything "SOTA" or "best" unless you're quoting a cited number.
- One entry per artifact. If a paper releases a model *and* a dataset, list each in its own section only when both are widely used on their own.
- Contributors are expected to follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
