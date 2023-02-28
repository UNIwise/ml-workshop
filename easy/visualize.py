import pandas as pd
from utils.plot import stats, visualize, addStd

def visualize_data() -> None:
    """Plot dataset"""
    df = pd.read_csv("data/easy.csv", parse_dates=["time"])
    df_agg = addStd(stats(df).fillna(0))
    df_agg = df_agg[df_agg["user_id"] != "exam"]
    df = pd.concat([df, df_agg])
    
    visualize(df_agg)



if __name__ == "__main__":
    visualize_data()
