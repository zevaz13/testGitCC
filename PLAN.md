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
- [x] Read hueexperiment.md for task context and exploration requirements. ask questions as needed. Add this file to gitignore (added to `.gitignore`)
- [x] Carry out integration exploratory analysis for finding the appropiate metamer (`compute_reference`, `compute_distance_to_reference` in `src/hue/analysis.py` — Model B, yellow-flash-referenced distance, using `RG` vs `Y` per the chosen approach)
- [x] produce plots for this analysis (`notebooks/hue/metamer_analysis.ipynb` — Model A vs Model B grid heatmaps)

**Success criteria:** integration tests pass; defects logged as GitHub issues and resolved.

## Phase 5: Behavioral data. 1 participant/session
- [x] Read beh.md for task context and exploration requirements. ask questions as needed. Add this file to gitignore, and ensure that the data in data/beh/raw is also ignored (`data/beh/beh.md` added to `.gitignore`; `data/beh/raw` already covered by existing rules)
- [x] Carry out integration exploratory analysis for loading the data for a participant, extracting the right cloud of points, plotting the information, and finding the median/mean point (`src/beh/io.py`, `analysis.py`, `plotting.py`)
- [x] produce plots for this analysis (`notebooks/beh/beh_analysis.ipynb`)

## Phase 6: Behavioral data. multiple participant/sessions
- [x] New data has been added to the raw folder. EAch of these is a different session of behavioral data. Plot the results for each session independently (`notebooks/beh/compare_sessions.ipynb`, section 2, reusing `plot_session_cloud`)
- [x] Plot the results for the 3 sessions in the same plot. Find creative ways of showing them. (`plot_sessions_comparison` — colored scatter + median/mean markers + 1-std covariance ellipse per session)
- [x] Quantify the difference between the distributions. (`compute_centroid_distance`, `compute_mahalanobis_distance`, `compute_session_distances` in `src/beh/analysis.py`)

## Notes

- Package manager: `uv` only.
- Issues are created at Claude's discretion; commit/push always requires explicit user permission.
