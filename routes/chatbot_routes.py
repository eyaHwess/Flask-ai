from flask import Blueprint, request, jsonify
from services.chatbot_service import generate_response

chatbot_bp = Blueprint("chatbot_bp", __name__)

@chatbot_bp.route("/api/assets/<asset_id>/chat", methods=["POST"])
def chat_with_asset_bot(asset_id):
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Question is required."}), 400

    answer = generate_response(question, asset_id)
    return jsonify({"answer": answer})
