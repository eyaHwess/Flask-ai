from services.review_analyzer import analyze_sentiment_and_profanity

def test_positive_sentiment_analysis():
    result = analyze_sentiment_and_profanity("This asset is amazing and works flawlessly.")
    assert result["sentiment"] == "POSITIVE"
    assert result["contains_profanity"] is False
    assert result["spamLabel"] == "ham"

def test_negative_sentiment_with_profanity():
    result = analyze_sentiment_and_profanity("This is a useless piece of crap.")
    assert result["sentiment"] == "NEGATIVE"
    assert result["contains_profanity"] is True
    assert result["spamLabel"] in ["spam", "ham"]

def test_neutral_edge_case():
    result = analyze_sentiment_and_profanity("The asset is okay, nothing special.")
    assert "sentiment" in result
    assert isinstance(result["sentiment"], str)
