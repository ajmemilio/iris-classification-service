# from flask_cors import CORS
from flask import Flask
from .iris import api_bp


def create_app():
    app = Flask(__name__)
    # CORS(app)

    app.register_blueprint(api_bp)

    return app
