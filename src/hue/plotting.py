import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_raw_channels(df: pd.DataFrame, ax: plt.Axes | None = None) -> plt.Axes:
    """Plot sample number vs hue_r/hue_g/hue_b on one figure."""
    if ax is None:
        _, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df["sample"], df["hue_r"], color="red", label="hue_r", linewidth=0.8)
    ax.plot(df["sample"], df["hue_g"], color="green", label="hue_g", linewidth=0.8)
    ax.plot(df["sample"], df["hue_b"], color="blue", label="hue_b", linewidth=0.8)
    ax.set_xlabel("sample")
    ax.set_ylabel("raw ADC count")
    ax.legend()
    return ax


def plot_trial_summary(summary: pd.DataFrame, axes: tuple[plt.Axes, plt.Axes] | None = None):
    """Plot per-trCnt derived values: mean channels and baseline-corrected deltas/distance."""
    if axes is None:
        _, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    mean_ax, delta_ax = axes
    mean_ax.plot(summary["trCnt"], summary["meanHueR"], color="red", label="meanHueR")
    mean_ax.plot(summary["trCnt"], summary["meanHueG"], color="green", label="meanHueG")
    mean_ax.plot(summary["trCnt"], summary["meanHueB"], color="blue", label="meanHueB")
    mean_ax.set_ylabel("mean raw count")
    mean_ax.legend()

    delta_ax.plot(summary["trCnt"], summary["deltaR"], color="red", label="deltaR")
    delta_ax.plot(summary["trCnt"], summary["deltaG"], color="green", label="deltaG")
    delta_ax.plot(summary["trCnt"], summary["deltaB"], color="blue", label="deltaB")
    delta_ax.plot(summary["trCnt"], summary["distance"], color="black", label="distance")
    delta_ax.set_xlabel("trCnt")
    delta_ax.set_ylabel("baseline-corrected")
    delta_ax.legend()

    return axes


def plot_feature_across_conditions(
    summaries: dict[str, pd.DataFrame],
    feature: str,
    conditions: list[str] | None = None,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Overlay one line per condition for the chosen feature (e.g. 'distance', 'meanHueR') vs trCnt."""
    if ax is None:
        _, ax = plt.subplots(figsize=(12, 4))
    for condition in conditions if conditions is not None else summaries:
        summary = summaries[condition]
        ax.plot(summary["trCnt"], summary[feature], label=condition)
    ax.set_xlabel("trCnt")
    ax.set_ylabel(feature)
    ax.legend(title="condition")
    return ax


def plot_baseline_comparison(
    baselines: dict[str, pd.Series],
    conditions: list[str] | None = None,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Grouped bar chart of baseline meanHueR/G/B per condition."""
    if ax is None:
        _, ax = plt.subplots(figsize=(10, 5))
    conditions = conditions if conditions is not None else list(baselines)
    channels = ("meanHueR", "meanHueG", "meanHueB")
    colors = ("red", "green", "blue")
    x = np.arange(len(conditions))
    width = 0.25

    for offset, channel, color in zip((-1, 0, 1), channels, colors):
        values = [baselines[c][channel] for c in conditions]
        ax.bar(x + offset * width, values, width=width, color=color, label=channel)

    ax.set_xticks(x)
    ax.set_xticklabels(conditions)
    ax.set_xlabel("condition")
    ax.set_ylabel("baseline mean raw count")
    ax.legend()
    return ax
