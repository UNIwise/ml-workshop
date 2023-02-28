import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as md


# Plot dataset with time on x-axis and y (default to value) on y-axis
def visualize(df: pd.DataFrame, y: str = "value") -> None:
    df["user_id"] = df["user_id"].astype(str)
    fig = plt.figure(figsize=(10, 7))
    ax = sns.lineplot(
        x="time", y=y, hue="user_id", data=df, style="user_id", markers=True
    )

    ax.xaxis.set_major_formatter(md.DateFormatter("%H:%M"))
    fig.autofmt_xdate()
    plt.xticks(rotation=45)
    plt.show()

# Aggregate dataframe into 5 min intervals with std, mean, and max
def stats(df: pd.DataFrame, feature: str = "value") -> pd.Series:
    df = df.set_index("time")
    df = (
        df.resample("5min")
        .agg(std=(feature, np.std), mean=(feature, np.mean), max=(feature, np.max))
        .reset_index()
    )
    df["user_id"] = "exam"
    return df

# Add a user that represents 3*std
def addStd(df: pd.DataFrame) -> pd.DataFrame:
    df_std = df.copy()
    df_std["user_id"] = "std"
    df_std["value"] = df_std["mean"] + 3 * df_std["std"]

    df_std_neg = df.copy()
    df_std_neg["user_id"] = "std"
    df_std_neg["value"] = df_std_neg["mean"] - 3 * df_std_neg["std"]
    return pd.concat([df, df_std, df_std_neg], ignore_index=True)
