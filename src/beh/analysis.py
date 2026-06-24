from itertools import combinations

import numpy as np
import pandas as pd


def compute_session_summary(session_df: pd.DataFrame) -> pd.Series:
    """Mean and median red/green across all runs in a session."""
    return pd.Series(
        {
            "meanRed": session_df["red"].mean(),
            "meanGreen": session_df["green"].mean(),
            "medianRed": session_df["red"].median(),
            "medianGreen": session_df["green"].median(),
        }
    )


def compute_centroid_distance(summary_a: pd.Series, summary_b: pd.Series, point: str = "median") -> float:
    """Euclidean distance between two sessions' median (or mean) (red, green) points."""
    a = np.array([summary_a[f"{point}Red"], summary_a[f"{point}Green"]])
    b = np.array([summary_b[f"{point}Red"], summary_b[f"{point}Green"]])
    return float(np.linalg.norm(a - b))


def compute_mahalanobis_distance(session_a: pd.DataFrame, session_b: pd.DataFrame) -> float:
    """Mahalanobis distance between two sessions' (red, green) distributions.

    Uses the pooled covariance of both sessions' combined (red, green)
    points, then measures the distance between the two sample means in
    that covariance-normalized space — accounts for spread, not just center.
    """
    points_a = session_a[["red", "green"]].to_numpy()
    points_b = session_b[["red", "green"]].to_numpy()
    pooled = np.vstack([points_a, points_b])
    inv_cov = np.linalg.inv(np.cov(pooled, rowvar=False))

    mean_diff = points_a.mean(axis=0) - points_b.mean(axis=0)
    return float(np.sqrt(mean_diff @ inv_cov @ mean_diff))


def compute_session_distances(
    sessions: dict[str, pd.DataFrame], summaries: dict[str, pd.Series]
) -> pd.DataFrame:
    """Pairwise centroid + Mahalanobis distance for every pair of sessions."""
    rows = []
    for session_a, session_b in combinations(sessions, 2):
        rows.append(
            {
                "sessionA": session_a,
                "sessionB": session_b,
                "centroidDistance": compute_centroid_distance(summaries[session_a], summaries[session_b]),
                "mahalanobisDistance": compute_mahalanobis_distance(sessions[session_a], sessions[session_b]),
            }
        )
    return pd.DataFrame(rows)
