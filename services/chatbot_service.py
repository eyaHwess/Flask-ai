import requests
from services.asset_theme_builder import fetch_reviews_for_asset

# Paste your OpenRouter key here
OPENROUTER_API_KEY = "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"

def build_prompt(reviews, question):
    review_text = " ".join(reviews[:20])  # Use only the first 20 reviews
    return (
        f"You are a helpful assistant.\n"
        f"These are user reviews about an asset:\n\n"
        f"{review_text}\n\n"
        f"Based on these reviews, answer the following question:\n"
        f"{question}\n"
        f"Answer:"
    )

def generate_response(question, asset_id):
    reviews = fetch_reviews_for_asset(asset_id)
    if not reviews:
        return "No reviews found for this asset."

    prompt = build_prompt(reviews, question)

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error from AI model: {response.text}"
