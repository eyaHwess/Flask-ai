# test/test_recommender.py

from services.asset_recommender import recommend_assets

def test_recommend_assets_with_matching_themes():
    user_themes = ["easy to use", "performance", "great UI"]
    asset_theme_map = {
        "asset1": ["performance", "great UI", "responsive"],
        "asset2": ["confusing", "slow interface"],
        "asset3": ["easy to use", "user-friendly", "minimal UI"]
    }

    result = recommend_assets(user_themes, asset_theme_map, top_n=2, similarity_threshold=0.1)
    assert isinstance(result, list)
    assert "asset1" in result or "asset3" in result

def test_no_matching_assets_due_to_threshold():
    user_themes = ["data science", "machine learning"]
    asset_theme_map = {
        "asset1": ["fast", "simple", "responsive"],
        "asset2": ["UI design", "collaboration", "template"]
    }

    result = recommend_assets(user_themes, asset_theme_map, top_n=3, similarity_threshold=0.6)
    assert result == []

def test_empty_user_themes_returns_nothing():
    result = recommend_assets([], {"asset1": ["fast", "useful"]})
    assert result == []
