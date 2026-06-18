# testGitCC

Tools and notebooks for organizing, visualizing, and exploring experimental data across domains: EEG, hue/light sensor data, lux, behavioral data, and standardized scores.

## Project structure

- `data/<type>/raw/` — raw data, not tracked in git
- `src/<type>/` — reusable loading and processing functions
- `notebooks/<type>/` — exploratory notebooks
- `scripts/<type>/` — standalone scripts
- `docs/<type>.md` — description of each data type

See [PLAN.md](PLAN.md) for the current rollout plan and progress.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python dependency management.

```
uv sync
```

## Status

Project scaffolding is in place. Work is ongoing — see [PLAN.md](PLAN.md) and [open issues](https://github.com/zevaz13/testGitCC/issues).
