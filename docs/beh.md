# beh

## Description

Behavioral "knobs" test: a participant adjusts red/green knobs per run to find a perceptual metamer of a fixed yellow at 10 Hz flicker, then presses a button to log the settled values. `data/beh/beh.md` (gitignored, not in the repo) has the full field-level description; only `red`/`green` (and the fixed `Amber`) are of interest.

A single participant/session lives in one folder under `data/beh/raw/` (e.g. `testUpstairs_18_JUN_26/`) and contains one file per run, named `S00_VarTimPots__R<run>.txt`. Each file has 9 redundant data rows; the 4th is used as the representative settled value.

## Raw data location

`data/beh/raw/<session>/S00_VarTimPots__R<run>.txt`

## Modules (`src/beh/`)

- `io.py`
  - `load_run(path)` — load one run file, returning its settled `red`/`green`/`Amber` values (4th data row).
  - `load_session(session_dir)` — load every run file in a session directory into one row per run (`run`, `red`, `green`, `Amber`).
- `analysis.py`
  - `compute_session_summary(session_df)` — mean and median `red`/`green` across all runs in a session.
- `plotting.py`
  - `plot_session_cloud(session_df, summary=None)` — scatter of `(red, green)` per run (fixed axes `[0,3200] x [0,2400]`), with mean/median overlaid if a summary is given.

## Notebooks (`notebooks/beh/`)

- `beh_analysis.ipynb` — loads one session, computes the mean/median summary, and plots the cloud of points with both highlighted.
