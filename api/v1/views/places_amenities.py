#!/usr/bin/python3
"""places_amenities views"""
from flask import abort, jsonify, request, make_response
from api.v1.views import app_views
from api.v1.views import *
from os import getenv
from models import storage

view = "Amenity"
parent_view = "Place"


@app_views.route('/places/<place_id>/amenities', strict_slashes=False,
                 methods=["GET"])
def get_place_amenities(place_id):
    """
    Get a list of all amenites associated with place
    (place_id)
    """
    return get_view_parent(parent_view, place_id, "amenities")


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 strict_slashes=False, methods=['DELETE', 'POST'])
def amenity_in_process(place_id, amenity_id):
    """
    Identify method
    """
    if request.method == "DELETE":
        return delete_place_amenity(place_id, amenity_id)
    else:
        return post_place_amenity(place_id, amenity_id)


def delete_place_amenity(place_id, amenity_id):
    """
    Delete (amenity_id) associated with
    place identified by (place_id)
    """
    place = storage.get(parent_view, place_id)
    if not place:
        return make_response(jsonify({"error": "Not found"}), 404)
    amenity = storage.get(view, amenity_id)
    if not amenity:
        return make_response(jsonify({"error": "Not found"}), 404)
    if amenity not in place.amenities:
        return make_response(jsonify({"error": "Not found"}), 404)
    place.amenities.remove(amenity)
    storage.save()
    return make_response(jsonify({}), 200)


def post_place_amenity(place_id, amenity_id):
    """
    Delete amenity (amenity_id) associated with
    place (place_id)
    """
    place = storage.get(parent_view, place_id)
    if not place:
        return make_response(jsonify({"error": "Not found"}), 404)
    amenity = storage.get(view, amenity_id)
    if not amenity:
        return make_response(jsonify({"error": "Not found"}), 404)

    if amenity in place.amenities:
        return make_response(jsonify(amenity.to_dict()), 200)
    place.amenities.append(amenity)
    place.save()
    return make_response(jsonify(amenity.to_dict()), 201)
