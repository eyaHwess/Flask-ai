# test/test_chatbot_admin.py

from unittest.mock import patch
from services.chatbot_admin_service import generate_global_response

@patch("services.chatbot_admin_service.gather_full_context")
@patch("services.chatbot_admin_service.requests.post")
def testChatbotAdmin(mock_post, mock_context):
    # Mock context returned by gather_full_context
    mock_context.return_value = {
        "summary": "9 users total",
        "top_contributors": "admin abd",
        "top_users": "eya abd",
        "new_users": "shaima barouni",
        "active_users": "eya abd, malek",
        "top_rated_assets": "dark theme",
        "upload_trend": "steady",
        "status_breakdown": "80% published",
        "rating_distribution": "mostly positive",
        "most_downloaded_asset": "UI Kit"
    }

    # Mock OpenRouter API response
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "choices": [{
            "message": {
                "content": "The platform has 9 users and 'admin abd' is the top contributor."
            }
        }]
    }

    result = generate_global_response("What are the latest stats?")
    
    assert isinstance(result, str)
    assert "admin abd" in result
    assert "9 users" in result or "The platform has 9 users" in result
