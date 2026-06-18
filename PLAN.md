# Plan

Tracks the current plan of action for scaffolding the data visualization project. Update checkboxes as phases complete.

## Phase 1: Project scaffolding

- [ ] Create folder structure: `data/`, `src/`, `notebooks/`, `scripts/`, `docs/` with subfolders per data type (eeg, hue, lux, beh, standardized scores)
- [ ] Add `data/<type>/raw/` for each data type
- [ ] Add `.gitignore` (env files, caches, raw data, notebook checkpoints, OS files)
- [ ] Initialize `uv` project (`pyproject.toml`) with data analysis dependencies: pandas, numpy, matplotlib, seaborn, jupyter
- [ ] Add `docs/<type>.md` stub for each data type

**Success criteria:** running `uv sync` creates a working environment; folder structure matches CLAUDE.md spec; `.gitignore` keeps raw data and secrets out of git.

## Phase 2: Exploration scaffolding

- [ ] Add one example notebook per data type under `notebooks/<type>/` that loads and visualizes sample data
- [ ] Expose reusable loading/plotting functions in `src/<type>/`
- [ ] Document each module's public functions in `docs/<type>.md`

**Success criteria:** a user can open a notebook, call functions from `src/<type>`, and produce a plot without writing boilerplate.

## Phase 3: Testing

- [ ] Add unit tests for `src/<type>` modules
- [ ] Configure test runner (pytest) via `uv`

**Success criteria:** `uv run pytest` passes and covers core data loading/transform functions.

## Phase 4: Integration testing

- [ ] Carry out integration testing (e.g. Playwright or similar) for any interactive/visual outputs
- [ ] Fix defects found

**Success criteria:** integration tests pass; defects logged as GitHub issues and resolved.

## Notes

- Package manager: `uv` only.
- Issues are created at Claude's discretion; commit/push always requires explicit user permission.
