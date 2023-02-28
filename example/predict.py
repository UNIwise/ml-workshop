import pandas as pd
from sklearn.ensemble import IsolationForest
from utils.plot import stats, visualize, addStd


def predict_outliers() -> None:
    
    # Loading in the dataset and batching into 5 minute intervals
    df = pd.read_csv("data/example.csv", parse_dates=["time"])
    df_agg = addStd(stats(df).fillna(0))
    df_agg = df_agg[df_agg["user_id"] != "exam"]

    df["time_sec"] = df["time"].dt.strftime("%s")
    
    
    # Fitting a model on the data
    clf = IsolationForest(n_estimators=10, warm_start=False, random_state=42).fit(
        df[["time_sec", "value"]]
    )
    
    # Getting outlier scores and normalizing them
    scores_df = pd.DataFrame(
        clf.score_samples(df[["time_sec", "value"]]), columns=["score"]
    )
    scores_df["norm_score"] = (scores_df["score"] - scores_df["score"].min()) / (
        scores_df["score"].max() - scores_df["score"].min()
    )

    # Plot outlier observations together together with 3 * standard deviation bounds
    df_outlier = df.loc[scores_df[scores_df["norm_score"] < 0.01].index]
    
    df_outlier = pd.concat([df_agg[df_agg["user_id"]=="std"], df[df["user_id"].isin(df_outlier["user_id"].unique())]])
    
    visualize(df_outlier)


if __name__ == "__main__":
    predict_outliers()
