import psycopg2
import pandas as pd
from transformers import pipeline
from config import DB_CONFIG

sentiment_pipeline = pipeline("sentiment-analysis")

def fetch_reviews_from_db(asset_id):
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT id, comment, created_at FROM review WHERE asset_id = %s"
    df = pd.read_sql_query(query, conn, params=(asset_id,))
    conn.close()
    return df

def generate_trend_chart(asset_id):
    df = fetch_reviews_from_db(asset_id)
    if df.empty:
        return {"error": "No reviews found"}

    df["created_at"] = pd.to_datetime(df["created_at"])
    df["month"] = df["created_at"].dt.to_period("M").astype(str)
    df["sentiment"] = df["comment"].apply(lambda t: sentiment_pipeline(t)[0]["label"])

    trend = df.groupby(["month", "sentiment"]).size().unstack(fill_value=0).reset_index()

    result = {
        "assetId": asset_id,
        "trend": trend.to_dict(orient="records")
    }

    return result
