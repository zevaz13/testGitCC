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
