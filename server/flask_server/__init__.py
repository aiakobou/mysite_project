from flask import Flask
from flask import current_app as app, jsonify, has_request_context, request
from flask_socketio import SocketIO
import os
from flask_sqlalchemy import SQLAlchemy
import logging


db = SQLAlchemy()
socketio = SocketIO()

def _uncaught_exception_handler(_):
    if has_request_context():
        app.logger.exception(f"Uncaught exception during {request.method}" 
                             f"request to {request.full_path}")
    else:
        print(f"PPPUncaught exception")
        app.logger.exception(f"Uncaught exception")
    return jsonify("Error")

def create_app():

    # logging.getLogger("socketio").setLevel(logging.WARNING)
    # logging.getLogger("engineio").setLevel(logging.WARNING)
    # logging.getLogger("werkzeug").setLevel(logging.WARNING)
    #
    # for handler in logging.root.handlers:
    #     # Filter must be added to the handlers, because if added to a logger it
    #     # does not propagate: https://docs.python.org/3/library/logging.html#filter-objects
    #     handler.addFilter(UserRequestFilter())


    app = Flask('server/flask_server')
    app.name = 'flask_server'
    app.config["SECRET_KEY"] = '123secret'

    socketio.init_app(app, cors_allowed_origins="*")

    with app.app_context():
        from .views import auth, client

        app.register_error_handler(Exception, _uncaught_exception_handler)
        return app



