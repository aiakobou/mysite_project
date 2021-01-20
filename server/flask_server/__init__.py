from flask import Flask
from flask import current_app as app
from flask_socketio import SocketIO
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


app = Flask('server/flask_server')
app.name = 'flask_server'
app.config["SECRET_KEY"] = '123secret'
socketio = SocketIO(app)


