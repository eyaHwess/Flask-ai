# chatbot_admin_service.py
import requests
from flask import request

OPENROUTER_API_KEY = "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"
BASE_API = "http://localhost:8081/admin"

def get_auth_headers():
    token = request.headers.get("Authorization")
    if not token:
        print(" No Authorization header found in request!")
    return { "Authorization": token } if token else {}

def safe_json(url):
    try:
        response = requests.get(url, headers=get_auth_headers())
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"ERROR: {e}"

def gather_full_context():
    return {
        "summary": safe_json(f"{BASE_API}/analytics/users/summary"),
        "top_contributors": safe_json(f"{BASE_API}/analytics/users/top-contributors"),
        "top_users": safe_json(f"{BASE_API}/analytics/users/active-users"),
        "new_users": safe_json(f"{BASE_API}/analytics/users/new-this-month/list"),
        "active_users": safe_json(f"{BASE_API}/analytics/users/active/list"),
        "top_rated_assets": safe_json(f"{BASE_API}/assets/top-rated"),
        "upload_trend": safe_json(f"{BASE_API}/assets/upload-trend"),
        "status_breakdown": safe_json(f"{BASE_API}/assets/status-breakdown"),
        "rating_distribution": safe_json(f"{BASE_API}/assets/rating-distribution"),
        "most_downloaded_asset": safe_json(f"{BASE_API}/assets/most-downloaded"),
    }

def generate_global_response(question):
    context = gather_full_context()
    prompt = (
        "You are a smart admin assistant with full access to system data.\n\n"
        f"User Summary: {context['summary']}\n"
        f"Top Contributors: {context['top_contributors']}\n"
        f"Most Active Users: {context['top_users']}\n"
        f"New Users: {context['new_users']}\n"
        f"Active Users: {context['active_users']}\n"
        f"Top Rated Assets: {context['top_rated_assets']}\n"
        f"Upload Trend: {context['upload_trend']}\n"
        f"Status Breakdown: {context['status_breakdown']}\n"
        f"Rating Distribution: {context['rating_distribution']}\n"
        f"Most Downloaded Asset: {context['most_downloaded_asset']}\n"
        f"\nQuestion: {question}\nAnswer:"
    )
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a powerful assistant for admins."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error from AI model: {response.text}"