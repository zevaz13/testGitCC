import numpy as np
import pandas as pd

_CHANNELS = ("hue_r", "hue_g", "hue_b")
_DISCARD_LEADING_SAMPLES = 3


def _trial_means(df: pd.DataFrame) -> pd.DataFrame:
    """Mean R/G/B per trCnt, using active-stimulus samples only.

    Per hue.md, only rows where triggerFlag == 1 count, and the first
    `_DISCARD_LEADING_SAMPLES` samples of each trCnt are dropped to let the
    sensor settle after the stimulus switches on.
    """
    active = df[df["triggerFlag"] == 1]
    sample_index_in_trial = active.groupby("trCnt").cumcount()
    trimmed = active[sample_index_in_trial >= _DISCARD_LEADING_SAMPLES]
    means = trimmed.groupby("trCnt")[list(_CHANNELS)].mean()
    return means.rename(columns={"hue_r": "meanHueR", "hue_g": "meanHueG", "hue_b": "meanHueB"})


def compute_baseline(df: pd.DataFrame) -> pd.Series:
    """Mean meanHueR/meanHueG/meanHueB across baseline trials (trCnt > 999)."""
    means = _trial_means(df)
    return means[means.index > 999].mean()


def compute_distance(summary: pd.DataFrame, channels: tuple[str, ...] = ("R", "G", "B")) -> pd.Series:
    """Baseline-corrected distance using a chosen subset of channels.

    `channels` picks which of 'R', 'G', 'B' to include, e.g. ("R", "G") for
    a red-green-only distance, or ("B",) to just look at deltaB. Requires
    `summary` to already have the corresponding delta columns (deltaR,
    deltaG, deltaB), as returned by `compute_trial_summary`.
    """
    delta_cols = [f"delta{c}" for c in channels]
    return np.sqrt(sum(summary[col] ** 2 for col in delta_cols))


def compute_trial_summary(
    df: pd.DataFrame, distance_channels: tuple[str, ...] = ("R", "G", "B")
) -> pd.DataFrame:
    """Per-stimulus summary: mean channel values, baseline-corrected deltas, distance.

    Baseline is the average of all baseline-trial means (trCnt > 999, taken
    before and after the stimulus grid). One row per stimulus trCnt is
    returned, sorted by trCnt.

    `distance_channels` controls which channels feed the default "distance"
    column (see `compute_distance`); deltaR/deltaG/deltaB are always
    included, so other combinations can be computed later by calling
    `compute_distance(summary, channels=...)` directly.
    """
    means = _trial_means(df)
    baseline = compute_baseline(df)
    summary = means[means.index <= 999].sort_index().copy()

    summary["deltaR"] = (summary["meanHueR"] - baseline["meanHueR"]).abs()
    summary["deltaG"] = (summary["meanHueG"] - baseline["meanHueG"]).abs()
    summary["deltaB"] = (summary["meanHueB"] - baseline["meanHueB"]).abs()
    summary["distance"] = compute_distance(summary, channels=distance_channels)
    return summary.reset_index()


def summarize_conditions(
    sessions: dict[str, pd.DataFrame], distance_channels: tuple[str, ...] = ("R", "G", "B")
) -> dict[str, pd.DataFrame]:
    """Apply compute_trial_summary to every condition in a loaded set."""
    return {
        condition: compute_trial_summary(df, distance_channels=distance_channels)
        for condition, df in sessions.items()
    }
