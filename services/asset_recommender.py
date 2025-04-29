from sentence_transformers import SentenceTransformer, util
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def score_asset_for_user(asset_themes, user_themes):
    """
    Simple scoring: +1 point per matching theme
    """
    matches = set(asset_themes) & set(user_themes)
    return len(matches)

positive_keywords = ['easy', 'amazing', 'great', 'smooth', 'performance', 'user-friendly', 'fast', 'good']

def recommend_assets(user_themes, asset_theme_map, top_n=5, similarity_threshold=0.3):
    """
    Smart recommendation based on semantic similarity.
    Only recommend assets with a similarity score > similarity_threshold.
    Only positive themes will be considered for recommendation.
    """

    asset_scores = {}

    # Embed all user themes once
    user_embeddings = embedder.encode(user_themes)

    for asset_id, asset_themes in asset_theme_map.items():
        if not asset_themes:
            continue
        
        # Filter out negative themes based on keywords (consider only positive ones)
        positive_themes = [theme for theme in asset_themes if any(keyword in theme for keyword in positive_keywords)]
        
        if not positive_themes:
            continue  # Skip assets with no positive themes

        # Embed all asset themes (only positive themes)
        asset_embeddings = embedder.encode(positive_themes)

        # Calculate cosine similarity matrix
        similarities = util.cos_sim(user_embeddings, asset_embeddings)

        # Aggregate max similarity for each user theme
        max_similarities = similarities.max(dim=1).values

        # Calculate average score
        avg_score = max_similarities.mean().item()

        if avg_score >= similarity_threshold:  # Apply threshold for recommendation
            asset_scores[asset_id] = avg_score

    # Sort assets by score descending and return top `top_n` assets
    sorted_assets = sorted(asset_scores.items(), key=lambda item: item[1], reverse=True)

    return [asset_id for asset_id, _ in sorted_assets][:top_n]