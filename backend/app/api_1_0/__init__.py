from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, equipment, users, permission, enterprise, purchase_order, sale_order, logistic, repair, store, upload
