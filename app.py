from flask import Flask
from routes.review_routes import review_bp
from routes.theme_routes import asset_theme_bp
from routes.recommendation_routes import recommendation_bp
from services.asset_theme_builder import fetch_all_asset_themes
from sentence_transformers import SentenceTransformer
from routes.chatbot_routes import chatbot_bp

app = Flask(__name__)

asset_embeddings_cache = {}

embedder = SentenceTransformer('all-MiniLM-L6-v2')

@app.before_request
def initialize_asset_themes():
    global asset_embeddings_cache
    if not asset_embeddings_cache:
        asset_theme_map = fetch_all_asset_themes()
        
        for asset_id, asset_themes in asset_theme_map.items():
            asset_embeddings_cache[asset_id] = embedder.encode(asset_themes)

        app.config["asset_embeddings_cache"] = asset_embeddings_cache

        print(f"Asset embeddings cached in memory: {len(asset_embeddings_cache)} assets")

app.register_blueprint(review_bp)
app.register_blueprint(asset_theme_bp)
app.register_blueprint(recommendation_bp)
app.register_blueprint(chatbot_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
