import re
from pathlib import Path

import pandas as pd

_SETTLED_ROW_INDEX = 3  # 4th data row (1-indexed), per data/beh/beh.md
_RUN_NUMBER_PATTERN = re.compile(r"R(\d+)\.txt$")


def load_run(path: str | Path) -> pd.Series:
    """Load one run file, returning its settled (red, green, Amber) values.

    Per data/beh/beh.md, all data rows in a run file are redundant; the 4th
    data row is used as the representative settled value.
    """
    df = pd.read_csv(path, sep=r"\s+")
    return df.iloc[_SETTLED_ROW_INDEX][["red", "green", "Amber"]]


def load_session(session_dir: str | Path) -> pd.DataFrame:
    """Load every run file in a participant/session directory.

    Returns one row per run, with columns run (parsed from the filename's
    R<n>), red, green, Amber, sorted by run number.
    """
    rows = []
    for path in Path(session_dir).glob("*.txt"):
        match = _RUN_NUMBER_PATTERN.search(path.name)
        run = load_run(path)
        rows.append({"run": int(match.group(1)), "red": run["red"], "green": run["green"], "Amber": run["Amber"]})
    return pd.DataFrame(rows).sort_values("run").reset_index(drop=True)
