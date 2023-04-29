#!/usr/bin/python3
"""Module for route /status"""
from api.v1.views import app_views
from flask import jsonify
import models


@app_views.route('/status', methods=["GET"])
def status():
    """Return /status api route"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=["GET"])
def stats():
    """Return /stats api route"""
    return jsonify({"amenities": models.storage.count("Amenity"),
                    "cities": models.storage.count("City"),
                    "places": models.storage.count("Place"),
                    "reviews": models.storage.count("Review"),
                    "states": models.storage.count("State"),
                    "users": models.storage.count("User")})
