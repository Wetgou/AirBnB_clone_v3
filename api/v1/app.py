#!/usr/bin/python3
# Script that starts a flask application in a port 5000
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    """Calls Storage close on appcontext"""
    storage.close()


@app.route("/api/v1/nop")
def not_found():
    """ Response to not found """
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=int(port), threaded=True)
