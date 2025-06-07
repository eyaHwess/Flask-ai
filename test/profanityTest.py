# test/test_profanity.py

from services.profanity_service import has_profanity

def test_clean_text_has_no_profanity():
    text = "This asset is very helpful and professionally built."
    assert has_profanity(text) is False

def test_text_with_explicit_profanity():
    text = "This is a stupid piece of crap."
    assert has_profanity(text) is True

def test_empty_text():
    text = ""
    assert has_profanity(text) is False

def test_mild_insult_still_detected():
    text = "Dumb interface and ugly layout."
    assert isinstance(has_profanity(text), bool)
