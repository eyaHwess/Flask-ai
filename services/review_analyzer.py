# from transformers import pipeline
# from better_profanity import profanity

# sentiment_pipeline = pipeline("sentiment-analysis")

# def analyze_sentiment_and_profanity(text):
#     result = sentiment_pipeline(text)[0]
#     contains_profanity = profanity.contains_profanity(text)
#     return {
#         "text": text,
#         "sentiment": result["label"],
#         "score": result["score"],
#         "contains_profanity": contains_profanity
#     }
from services.sentiment_service import get_sentiment
from services.profanity_service import has_profanity
from services.spam_detector import detect_spam
def analyze_sentiment_and_profanity(text):
    sentiment_result = get_sentiment(text)
    contains_profanity = has_profanity(text)
    spam_result= detect_spam(text)
    return {
        "text": text,
        "sentiment": sentiment_result["label"],
        "score": sentiment_result["score"],
        "contains_profanity": contains_profanity,
        "spamLabel":spam_result["label"],
        "spamScore": spam_result["score"]
    }
