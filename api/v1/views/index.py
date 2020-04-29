#!/usr/bin/python3
""" """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=['GET'])
def return_status():
    "status return"
    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def return_stats():
    "return stats "
    dict = {}

    name_clases = ["Amenity", "City", "Place", "Review", "State", "User"]
    for i in name_clases:
        dict[i] = storage.count(i)
    return jsonify(dict)
