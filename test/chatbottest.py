# test/test_chatbot.py

from unittest.mock import patch
from services.chatbot_service import generate_response

@patch("services.chatbot_service.fetch_reviews_for_asset", return_value=[
    "Great design and very helpful.",
    "Users love the intuitive interface.",
    "Super smooth performance."
])
@patch("services.chatbot_service.requests.post")
def test_generate_response_returns_expected_reply(mock_post, mock_reviews):
    # Mock response from OpenRouter API
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "choices": [{
            "message": {
                "content": "Users generally appreciate the performance and ease of use."
            }
        }]
    }

    result = generate_response("What do users say about this asset?", "asset123")
    assert isinstance(result, str)
    assert "Users generally appreciate" in result
