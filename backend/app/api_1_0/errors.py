from flask import jsonify
from . import api


def bad_request(message):
    response = jsonify({'error': 400, 'msg': '[bad request]' + message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 401, 'msg': '[unauthorized]' + message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 403, 'msg': '[forbidden]' + message})
    response.status_code = 403
    return response


