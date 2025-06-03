from services.sentiment_service import get_sentiment
from services.profanity_service import has_profanity
from services.spam_detector import detect_spam

def analyze_sentiment_and_profanity(text: str):
    sentiment_result = get_sentiment(text)
    contains_profanity = has_profanity(text)
    spam_result = detect_spam(text)
    print(f"[DEBUG] Text: {text}")
    print(f"[DEBUG] Spam Result: {spam_result}")
    return {
        "text": text,
        "sentiment": sentiment_result["label"],
        "score": sentiment_result["score"],
        "contains_profanity": contains_profanity,
        "spamLabel": spam_result["label"],
        "spamScore": spam_result["score"]
    }