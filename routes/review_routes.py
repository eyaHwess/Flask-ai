from flask import Blueprint, request, jsonify
from services.review_analyzer import analyze_sentiment_and_profanity
from services.trend_service import generate_trend_chart

review_bp = Blueprint('review_bp', __name__)

@review_bp.route("/analyze", methods=["POST"])
def analyze_review():
    data = request.json
    text = data.get("text", "")
    result = analyze_sentiment_and_profanity(text)
    return jsonify(result)

@review_bp.route("/trend", methods=["GET"])
def sentiment_trend():
    asset_id = request.args.get("assetId")
    if not asset_id:
        return jsonify({"error": "Missing assetId parameter"}), 400

    result = generate_trend_chart(asset_id)
    return jsonify(result)
