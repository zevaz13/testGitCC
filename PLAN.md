# Plan

Tracks the current plan of action for scaffolding the data visualization project. Update checkboxes as phases complete.

## Phase 1: Project scaffolding

- [x] Create folder structure: `data/`, `src/`, `notebooks/`, `scripts/`, `docs/` with subfolders per data type (eeg, hue, lux, beh, standardized scores)
- [x] Add `data/<type>/raw/` for each data type
- [x] Add `.gitignore` (env files, caches, raw data, notebook checkpoints, OS files)
- [x] Initialize `uv` project (`pyproject.toml`) with data analysis dependencies: pandas, numpy, matplotlib, seaborn, jupyter
- [x] Add `docs/<type>.md` stub for each data type
- [x] Fill in `data/hue/hue.md` with real dataset description (fields, experiment context, analysis outputs) — first data type with non-stub documentation

**Success criteria:** running `uv sync` creates a working environment; folder structure matches CLAUDE.md spec; `.gitignore` keeps raw data and secrets out of git.

## Phase 2: Exploration scaffolding

- [x] hue: `src/hue/io.py` (load a session file, identify baseline trials), `src/hue/analysis.py` (per-trCnt means, baseline-corrected deltas, distance metric), `src/hue/plotting.py` (raw channel plot, derived-value plot)
- [x] hue: `notebooks/hue/explore_flash_RGY.ipynb` loads `data/hue/raw/data_17JUN26/flash_RGY.txt`, plots raw `hue_r`/`hue_g`/`hue_b` vs sample number, and plots derived per-trCnt values (means, deltas, distance)
- [x] hue: Create a new notebook that allows the data plotting for each of the experiment conditions. Each in separated plots with the same plots that were created for explore_flash_RGB. one for plotting raw channels, and one for plotting channel derived metrics. (`notebooks/hue/explore_conditions.ipynb`)
- [x] hue: make a new notebook this time with functions that allow comparison of information across different conditions. I want to see the same feature as it changes in all or some of the conditions. (`notebooks/hue/compare_conditions.ipynb`, `plot_feature_across_conditions`)
- [x] hue: make a plot that allows to compare the baselines of all or some conditions (`plot_baseline_comparison`, in `compare_conditions.ipynb`)
- [x] hue: document the information for hue processing so far. (`docs/hue.md`)

**Success criteria:** a user can open a notebook, call functions from `src/<type>`, and produce a plot without writing boilerplate.

## Phase 3: Grid plots

- [x] Create a notebook for plotting the data of each single condition as grid of data with red intensity as x axis and green intensity as y axis (`notebooks/hue/grid_plots.ipynb`, `compute_grid`, `plot_grid_heatmap`)
- [x] This grid could be use for each of the derived features (notebook loops over `meanHueR`, `meanHueG`, `meanHueB`, `distance`; `compute_grid` works for any summary column)

**Success criteria:** `uv run pytest` passes and covers core data loading/transform functions.

## Phase 4: Metamer identification
- [ ] Read hueexperiment.md for task context and exploration requirements. ask questions as needed
- [ ] Carry out integration exploratory analysis for finding the appropiate metamer
- [ ] produce plots for this analysis

**Success criteria:** integration tests pass; defects logged as GitHub issues and resolved.

## Notes

- Package manager: `uv` only.
- Issues are created at Claude's discretion; commit/push always requires explicit user permission.
