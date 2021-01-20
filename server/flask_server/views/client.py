from flask import jsonify, render_template, request

from flask import current_app as app

@app.route("/")
def index():
    return jsonify("Great Success!")