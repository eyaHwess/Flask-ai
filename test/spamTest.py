
from services.spam_detector import detect_spam

def test_legitimate_review_is_not_spam():
    result = detect_spam("This plugin is very helpful and easy to use.")
    assert result["label"] == "ham"
    assert 0 <= result["score"] <= 1

def test_spammy_text_is_detected():
    result = detect_spam("Buy now! Limited offer! Click here to get rich!")
    assert result["label"] == "spam"
    assert 0 <= result["score"] <= 1

def test_empty_input_is_not_spam():
    result = detect_spam("")
    assert result["label"] == "ham"
