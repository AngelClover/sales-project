from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, equipment, users, authorize, producer
