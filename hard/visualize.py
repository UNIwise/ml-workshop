import pandas as pd
from utils.plot import stats, visualize, addStd
import argparse

def visualize_data(status_key: str = "CHARACTERS_TYPED") -> None:
    """Plot dataset"""
    df = pd.read_csv("data/hard.csv", parse_dates=["time"])
    df = df[df["status_key"] == status_key]
    
    df_agg = addStd(stats(df).fillna(0))
    df_agg = df_agg[df_agg["user_id"] != "exam"]
    df = pd.concat([df, df_agg])
    
    visualize(df_agg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "status_key",
        type=str,
        metavar="status_key",
        choices=["CHARACTERS_TYPED", "FACIAL_RECOGNITION", "VOICE_DETECTION"],
        help="status key to visiualize ex. CHARACTERS_TYPED"
    )

    args = parser.parse_args()
    visualize_data(args.status_key)
