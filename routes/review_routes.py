from flask import Blueprint, request, jsonify
from services.review_analyzer import analyze_sentiment_and_profanity
from services.trend_service import generate_trend_chart
from services.profanity_service import has_profanity

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
@review_bp.route('/check_profanity', methods=['POST'])
def check_profanity():
    
    try:
        print(f"Request Body: {request.data}")
        review_data = request.get_json()
        if not review_data:
            return jsonify({"error": "Invalid input, JSON is expected"}), 400
        review_text = review_data.get("comment")
        asset_id = review_data.get("assetId")
        if not review_text:
            return jsonify({"error": "Review text is required"}), 400
        print(f"Received review for asset {asset_id}: {review_text}")
        contains_profanity = has_profanity(review_text)
        return jsonify({"containsProfanity": contains_profanity}), 200
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({"error": "Invalid input"}), 400
