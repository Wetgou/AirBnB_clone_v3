#!/usr/bin/python3
""" """
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def return_status():
    "status return"
    return jsonify({'status': 'OK'})
