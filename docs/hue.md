# hue

## Description

Hue sensor data logger output (Adafruit TCS34725). See `data/hue/hue.md` for the full field-level description of the dataset and experiment context.

A single experiment session lives in one folder under `data/hue/raw/` (e.g. `data_17JUN26/`) and contains multiple condition files named `flash_<condition>.txt`, one per combination of LEDs flashed (e.g. `flash_R.txt`, `flash_RG.txt`, `flash_RGY.txt`). All files share the same tab-separated column format.

## Raw data location

`data/hue/raw/<session>/flash_<condition>.txt`

## Modules (`src/hue/`)

- `io.py`
  - `load_session(path)` — load one condition file into a tidy DataFrame (renamed columns, adds a `sample` column for acquisition order).
  - `load_condition_set(session_dir)` — load every `flash_*.txt` file in a session directory into `{condition_name: df}`.
  - `is_baseline(df)` — boolean mask for baseline rows (`trCnt > 999`).
- `analysis.py`
  - `compute_baseline(df)` — mean `meanHueR`/`meanHueG`/`meanHueB` across baseline trials.
  - `compute_trial_summary(df, distance_channels=("R","G","B"))` — per-stimulus mean channel values, baseline-corrected deltas, and a distance metric.
  - `compute_distance(summary, channels=...)` — recompute the distance metric from an existing summary using any subset of R/G/B (e.g. just `("R","G")`).
  - `summarize_conditions(sessions, distance_channels=...)` — apply `compute_trial_summary` to every condition in a loaded set.
- `plotting.py`
  - `plot_raw_channels(df)` — raw `hue_r`/`hue_g`/`hue_b` vs sample number.
  - `plot_trial_summary(summary)` — mean channel values and baseline-corrected deltas/distance vs `trCnt`.
  - `plot_feature_across_conditions(summaries, feature, conditions=None)` — overlay one summary column across all or a chosen subset of conditions.
  - `plot_baseline_comparison(baselines, conditions=None)` — grouped bar chart of baseline channel means across conditions.

## Notebooks (`notebooks/hue/`)

- `explore_flash_RGY.ipynb` — single-condition walkthrough: load one file, raw channel plot, derived-value plot, distance for a chosen channel combination.
- `explore_conditions.ipynb` — loads every condition in a session and produces the raw-channel and derived-value plots separately for each condition.
- `compare_conditions.ipynb` — loads every condition in a session and compares a chosen feature (e.g. `distance`, `meanHueR`) and baseline channel means across all or a subset of conditions.
