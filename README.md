# testGitCC

Python notebooks and scripts for organizing, visualizing, and exploring experimental data across domains: hue/light sensor data, behavioral ("knobs") data, EEG, lux, and standardized scores.

## Project structure

```
data/<type>/raw/      raw data, not tracked in git
src/<type>/           reusable loading, analysis, and plotting functions
notebooks/<type>/     exploratory notebooks built on top of src/<type>
scripts/<type>/       standalone scripts
docs/<type>.md        description of each data type, its modules, and its notebooks
```

See [PLAN.md](PLAN.md) for the phased rollout plan and current progress.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) as its only package manager.

```
uv sync
```

Run notebooks with `uv run jupyter lab`, or execute one non-interactively with:

```
uv run jupyter nbconvert --to notebook --execute --inplace notebooks/<type>/<name>.ipynb
```

## Data domains

### hue

Hue sensor (TCS34725) data from a 10 Hz red+green vs. fixed-yellow flicker experiment, used to identify metamers — red/green LED combinations perceptually indistinguishable from the fixed yellow. See [docs/hue.md](docs/hue.md) for the module and notebook reference.

- `notebooks/hue/explore_flash_RGY.ipynb` — single-condition walkthrough
- `notebooks/hue/explore_conditions.ipynb` — raw and derived plots per condition
- `notebooks/hue/compare_conditions.ipynb` — cross-condition feature, channel, and baseline comparisons
- `notebooks/hue/grid_plots.ipynb` — red x green stimulus grid heatmaps
- `notebooks/hue/metamer_analysis.ipynb` — baseline-referenced vs. yellow-flash-referenced distance models

### beh

Behavioral "knobs" test: a participant adjusts red/green knobs to match a fixed yellow at 10 Hz flicker. See [docs/beh.md](docs/beh.md) for the module and notebook reference.

- `notebooks/beh/beh_analysis.ipynb` — single-session cloud of points with mean/median
- `notebooks/beh/compare_sessions.ipynb` — per-session plots, a combined comparison plot, and pairwise distance quantification across sessions

### eeg, lux, standardized scores

Scaffolding in place (`data/`, `src/`, `notebooks/`, `docs/` folders); exploration pipelines not yet built.

## Status

hue (Phases 1-4) and beh (Phases 5-6) have working data pipelines and notebooks. See [PLAN.md](PLAN.md) for phase-by-phase detail and [open issues](https://github.com/zevaz13/testGitCC/issues).
