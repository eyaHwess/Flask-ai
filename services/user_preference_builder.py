from services.theme_detector import detect_themes

def build_user_preferences(user_reviews):
    """
    Input: list of user reviews (strings)
    Output: list of preferred themes (strings)
    """
    user_themes = detect_themes(user_reviews)

    return user_themes
