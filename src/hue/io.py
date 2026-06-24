from pathlib import Path

import pandas as pd

_COLUMN_MAP = {
    "Stim": "trCnt",
    "HueR": "hue_r",
    "HueG": "hue_g",
    "HueB": "hue_b",
    "HueC": "hue_c",
    "HueCT": "hue_colorTemp",
    "HueLux": "hue_lux",
    "Yellow": "currentYellow",
    "Red": "currentRed",
    "Green": "currentGreen",
    "Trig": "triggerFlag",
}

BASELINE_TRCNT_THRESHOLD = 999


def load_session(path: str | Path) -> pd.DataFrame:
    """Load a hue sensor data logger file into a tidy DataFrame.

    Renames columns to match data/hue/hue.md and adds a `sample` column
    giving each row's position in the file (0-based), i.e. acquisition order.
    """
    df = pd.read_csv(path, sep="\t")
    df = df.rename(columns=_COLUMN_MAP)
    df.insert(0, "sample", range(len(df)))
    return df


def is_baseline(df: pd.DataFrame) -> pd.Series:
    """Boolean mask for baseline rows (trCnt > 999, per hue.md)."""
    return df["trCnt"] > BASELINE_TRCNT_THRESHOLD


def load_condition_set(session_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Load every `flash_*.txt` file in a session directory.

    Returns {condition_name: df}, e.g. {"R": ..., "RG": ..., "RGY": ...},
    where condition_name is the filename stem with the "flash_" prefix stripped.
    """
    paths = sorted(Path(session_dir).glob("flash_*.txt"))
    return {path.stem.removeprefix("flash_"): load_session(path) for path in paths}
