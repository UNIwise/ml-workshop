import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as md
import seaborn.objects as so


def visualize(df: pd.DataFrame, y: str = "value") -> None:

    fig = plt.figure(figsize=(10, 7))
    ax = sns.lineplot(x="time", y=y, hue="user_id", data=df)
    
    ax.xaxis.set_major_formatter(md.DateFormatter("%H:%M"))
    fig.autofmt_xdate()
    plt.xticks(rotation=45)
    # df["user_id"] = df["user_id"].astype(str)
    # p = so.Plot(df, x="time", y=y, color="user_id").add(so.Line(), so.Agg())
    # p.show()
    plt.show()


def stats(df: pd.DataFrame, feature: str = "value") -> pd.Series:
    df = df.set_index("time")
    return (
        df.groupby("user_id")
        .resample("5min")
        .agg(std=(feature, np.std), mean=(feature, np.mean), value=(feature, np.max))
        .reset_index()
    )

def addStd(df: pd.DataFrame) -> pd.DataFrame:
    df_std = df.copy()
    df_std["user_id"] = "std"
    df_std["value"] = df_std["mean"] + 3*df_std["std"]
    
    df_std_neg = df.copy()
    df_std_neg["user_id"] = "std"
    df_std_neg["value"] = df_std_neg["mean"] - 3*df_std_neg["std"]
    return pd.concat([df, df_std, df_std_neg], ignore_index=True)