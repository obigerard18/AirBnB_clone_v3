#!/usr/bin/python3
"""Module for Place view"""
from api.v1.views import app_views
from api.v1.views import *
from models import storage
from models.place import Place
from models.city import City
from flask import jsonify, make_response, request

view = Place
parent_view = City


@app_views.route("/cities/<city_id>/places",
                 strict_slashes=False,
                 methods=["GET"])
def get_places(city_id):
    """GET /city route"""
    return get_view_parent(parent_view, city_id, "places")


@app_views.route("/places/<place_id>", methods=["GET"])
def get_place(place_id):
    """GET view"""
    return get_view(view, place_id)


@app_views.route("/places/<place_id>", methods=["DELETE"])
def delete_place(place_id):
    """DELETE view"""
    return delete_view(view, place_id)


@app_views.route("/cities/<city_id>/places", strict_slashes=False,
                 methods=["POST"])
def post_place(city_id):
    """POST view"""
    required = ["name", "user_id"]
    return post_view(view, parent_view, city_id, required)


@app_views.route("/places/<place_id>", methods=["PUT"])
def put_place(place_id):
    """PUT view"""
    ignore = ["id", "user_id", "city_id", "created_at", "updated_at"]
    return put_view(view, place_id, ignore)
