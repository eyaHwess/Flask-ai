# test/test_theme_extraction.py

from services.theme_detector import detect_themes

def test_detect_keywords_from_positive_reviews():
    reviews = [
        "Amazing performance and excellent UI.",
        "Smooth integration and very easy to use.",
        "Highly responsive and user-friendly design."
    ]
    themes = detect_themes(reviews)
    assert isinstance(themes, list)
    assert len(themes) > 0
    assert all(isinstance(theme, str) for theme in themes)

def test_empty_reviews_list_returns_empty():
    reviews = []
    themes = detect_themes(reviews)
    assert themes == []

def test_single_review_keyword_extraction():
    reviews = ["Great API design with useful endpoints."]
    themes = detect_themes(reviews)
    assert isinstance(themes, list)
    assert len(themes) > 0
