from flask import jsonify, render_template, request
from flask import current_app as app
from flask_server import socketio
from flask_socketio import emit

@app.route("/")
def index():
    #return render_template("index.html")
    return jsonify("Great Success!")

@socketio.on('connect')
def on_conect():
    print('CONNECTED')
    emit('MESSAGE', 'HELLO HELLO HELLO')

@socketio.on('disconnect')
def on_disconnect():
    emit('MESSAGE', 'BYE BYE BYE')
    print('DISCONNECTED')


@socketio.on('message')
def on_customevent(data):
    print(data)

@app.route("/api")
def api_test():
    return jsonify("GREAT API SUCCESS")

