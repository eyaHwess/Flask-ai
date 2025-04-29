import psycopg2
from services.theme_detector import detect_themes
from config import DB_CONFIG  # Import your existing db config

def fetch_assets_from_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id FROM asset")  # Your asset table, get asset IDs
    asset_rows = cur.fetchall()
    assets = [row[0] for row in asset_rows]
    conn.close()
    return assets

def fetch_reviews_for_asset(asset_id):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT comment FROM review WHERE asset_id = %s", (asset_id,))
    review_rows = cur.fetchall()
    reviews = [row[0] for row in review_rows]
    conn.close()
    return reviews

def fetch_all_asset_themes():
    asset_theme_map = {}

    asset_ids = fetch_assets_from_db()

    for asset_id in asset_ids:
        reviews = fetch_reviews_for_asset(asset_id)
        if not reviews:
            continue

        themes = detect_themes(reviews)

        asset_theme_map[asset_id] = themes

    return asset_theme_map
