import matplotlib.pyplot as plt
import pandas as pd


def plot_session_cloud(session_df: pd.DataFrame, summary: pd.Series | None = None, ax: plt.Axes | None = None) -> plt.Axes:
    """Scatter of (red, green) per run, per data/beh/beh.md's fixed axis ranges.

    If `summary` is given (see compute_session_summary), overlays the mean
    and median points with distinct markers.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(session_df["red"], session_df["green"], label="runs", color="gray", alpha=0.7)

    if summary is not None:
        ax.scatter(summary["meanRed"], summary["meanGreen"], marker="x", s=120, color="blue", label="mean")
        ax.scatter(summary["medianRed"], summary["medianGreen"], marker="*", s=160, color="red", label="median")
        ax.annotate(
            f"({summary['medianRed']:.0f}, {summary['medianGreen']:.0f})",
            (summary["medianRed"], summary["medianGreen"]),
            textcoords="offset points",
            xytext=(8, 8),
            color="red",
        )
        ax.plot([summary["medianRed"]] * 2, [0, summary["medianGreen"]], linestyle="--", color="red", linewidth=1)
        ax.plot([0, summary["medianRed"]], [summary["medianGreen"]] * 2, linestyle="--", color="red", linewidth=1)

    ax.set_xlim(0, 3200)
    ax.set_ylim(0, 2400)
    ax.set_xlabel("red")
    ax.set_ylabel("green")
    ax.legend()
    return ax
