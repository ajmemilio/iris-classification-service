import flask_restful

from flask import Blueprint
from . import model

api_bp = Blueprint('iris', __name__)
api = flask_restful.Api(api_bp)

api.add_resource(model.Model, '/predict')
