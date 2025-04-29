from flask import Blueprint, request, jsonify
import psycopg2
from config import DB_CONFIG
from services.user_preference_builder import build_user_preferences
from services.asset_recommender import recommend_assets
from services.asset_theme_builder import fetch_all_asset_themes, fetch_reviews_for_asset
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')

recommendation_bp = Blueprint('recommendation_bp', __name__)
@recommendation_bp.route("/recommendations", methods=["POST"])
def recommend():
    data = request.get_json()
    user_id = data.get("userId")

    if not user_id:
        return jsonify({"error": "userId is required"}), 400

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT asset_id, comment FROM review WHERE user_id = %s", (user_id,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return jsonify({"error": "No reviews found for this user"}), 404

    user_reviews = [row[1] for row in rows]
    reviewed_asset_ids = set(row[0] for row in rows)

    user_themes = build_user_preferences(user_reviews)

    asset_theme_map = fetch_all_asset_themes()

    filtered_asset_theme_map = {asset_id: themes for asset_id, themes in asset_theme_map.items() if asset_id not in reviewed_asset_ids}

    recommendations = recommend_assets(user_themes, filtered_asset_theme_map)

    return jsonify({"recommendedAssets": recommendations})
