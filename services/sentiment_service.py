from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }
