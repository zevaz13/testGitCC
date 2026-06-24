import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Ellipse


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


def _draw_covariance_ellipse(points: np.ndarray, ax: plt.Axes, color: str, n_std: float = 1.0) -> None:
    """Draw an n_std covariance ellipse for a (N, 2) array of (red, green) points."""
    center = points.mean(axis=0)
    cov = np.cov(points, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
    width, height = 2 * n_std * np.sqrt(eigenvalues)
    ellipse = Ellipse(center, width=width, height=height, angle=angle, facecolor="none", edgecolor=color, linewidth=2)
    ax.add_patch(ellipse)


def plot_sessions_comparison(
    sessions: dict[str, pd.DataFrame], summaries: dict[str, pd.Series], ax: plt.Axes | None = None
) -> plt.Axes:
    """All sessions on one plot: colored scatter, median/mean markers, and a 1-std covariance ellipse per session."""
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 6))

    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for color, (session_name, session_df) in zip(colors, sessions.items()):
        summary = summaries[session_name]
        ax.scatter(session_df["red"], session_df["green"], color=color, alpha=0.5, label=session_name)
        ax.scatter(summary["meanRed"], summary["meanGreen"], marker="x", s=120, color=color)
        ax.scatter(summary["medianRed"], summary["medianGreen"], marker="*", s=160, color=color)
        _draw_covariance_ellipse(session_df[["red", "green"]].to_numpy(), ax, color=color)

    ax.set_xlim(0, 3200)
    ax.set_ylim(0, 2400)
    ax.set_xlabel("red")
    ax.set_ylabel("green")
    ax.legend(title="session")
    return ax
