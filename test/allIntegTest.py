# test/integration/test_sprint3_endpoints.py
from flask import Flask
from routes.chatbot_routes import chatbot_bp
from routes.recommendation_routes import recommendation_bp
from routes.review_routes import review_bp

import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True

    app.register_blueprint(chatbot_bp)
    app.register_blueprint(recommendation_bp)
    app.register_blueprint(review_bp)

    with app.test_client() as client:
        yield client

#  /check_profanity
def testCheckProfanity(client):
    response = client.post('/check_profanity', json={
        "comment": "This asset is very helpful and clean.",
        "assetId": "dummy123"
    })
    assert response.status_code == 200
    assert response.get_json()["containsProfanity"] is False

def test_check_profanity_detected(client):
    response = client.post('/check_profanity', json={
        "comment": "This is a stupid piece of crap.",
        "assetId": "dummy123"
    })
    assert response.status_code == 200
    assert response.get_json()["containsProfanity"] is True

#  /analyze
def test_analyze_positive(client):
    response = client.post('/analyze', json={
        "text": "This asset is extremely helpful and well designed."
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["sentiment"] == "POSITIVE"
    assert json_data["contains_profanity"] is False
    assert json_data["spamLabel"] in ["ham", "spam"]

def test_analyze_negative(client):
    response = client.post('/analyze', json={
        "text": "This is a terrible and useless piece of crap."
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["sentiment"] == "NEGATIVE"
    assert json_data["contains_profanity"] is True
    assert json_data["spamLabel"] in ["ham", "spam"]

# /recommendations
def test_recommendations_endpoint(client):
    response = client.post('/recommendations', json={ "userId": 123 })

    assert response.status_code in [200, 404]  # If no reviews, backend may return 404
    assert isinstance(response.get_json(), dict)

#  /api/assets/<id>/chat
def test_chat_asset(client):
    response = client.post('/api/assets/test-asset-1/chat', json={
        "question": "What do users think about this asset?"
    })
    assert response.status_code in [200, 404]  # 404 if no reviews
    assert "answer" in response.get_json() or "error" in response.get_json()

#  /api/chat/global
def test_chat_global(client):
    response = client.post('/api/chat/global', json={ "question": "Which assets are trending?" })

    assert response.status_code in [200, 400]
    assert "answer" in response.get_json() or "error" in response.get_json()
