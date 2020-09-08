#!/usr/bin/python3
"""Module for route /status"""
from api.v1.views import app_views
from flask import abort, make_response, request, jsonify
import models


@app_views.route('/states', methods=["GET"])
def states():
    state_json_obj = []
    for v in models.storage.all().values():
        if type(v).__name__ == "State":
            state_json_obj.append(v.to_dict())
    return jsonify(state_json_obj)


@app_views.route('/states/<state_id>', methods=["GET"])
def state_by_id(state_id):
    key_objs = "State." + str(state_id)
    if key_objs in models.storage.all():
        return models.storage.all()[key_objs].to_dict()
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=["DELETE"])
def state_delete(state_id):
    key_objs = "State." + str(state_id)
    if key_objs in models.storage.all():
        del models.storage.all()[key_objs]
        return make_response({}, 200)
    else:
        abort(404)


@app_views.route('/states', methods=["POST"])
def create_state():
    if request.get_json:
        if "name" in request.get_json:
            st = models.state.State(request.get_json)
            st.save()
            return make_response(st.to_dict(), 201)
        else:
            return make_response("Missing name", 400)
    else:
        return make_response("Not a JSON", 400)


@app_views.route('/states/<state_id>', methods=["PUT"])
def update_state(state_id):
    key_objs = "State." + str(state_id)
    if key_objs in models.storage.all():
        if request.get_json:
            for key, value in request.get_json.items():
                if key != "id" and key != "created_at" and key != "updated_at":
                    setattr(models.storage.all()[key_objs], key, value)
            models.storage.all()[key_objs].save()
            return make_response(models.storage.all()[key_objs].to_dict(), 200)
        else:
            return make_response("Not a JSON", 400)
    else:
        abort(404)
