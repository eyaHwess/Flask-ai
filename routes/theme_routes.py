from flask import Blueprint, jsonify
from services.asset_theme_builder import fetch_all_asset_themes

asset_theme_bp = Blueprint('asset_theme_bp', __name__)

@asset_theme_bp.route("/assets/themes", methods=["GET"])
def get_all_asset_themes():
    asset_theme_map = fetch_all_asset_themes()
    return jsonify(asset_theme_map)
