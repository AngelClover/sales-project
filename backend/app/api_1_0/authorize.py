#-*- coding:utf-8 -*-

from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User, Permission
from .. import db
from .errors import bad_request, unauthorized, forbidden
from decorators import permission_required

@api.route('/authorize/permissions', methods=['GET', 'POST'])
def get_permissions():
    return jsonify({
            'error' : 0,
            'msg' : 'successful',
            'data' : Permission.to_json()
            })

@api.route('/authorize/<int:id>', methods=['POST'])
@permission_required(Permission.ADMINISTER)
def authorize(id):
    user = User.query.get(id)
    if user is None:
        return bad_request('no such a user')
    if 'permissions' not in request.get_json() or \
            not isinstance(request.get_json()['permissions'], list):
        return bad_request('authorize need json permissions field or not a list')
    permissions = request.get_json()['permissions']
    for per in permissions:
        user.permission |= per
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'authorize successful',
            'data' : {}
            })

@api.route('/unauthorize/<int:id>')
@permission_required(Permission.ADMINISTER)
def unauthorize(id):
    user = User.query.get(id)
    if user is None:
        return bad_request('no such a user')
    if 'permissions' not in request.get_json() or \
            not isinstance(request.get_json()['permissions'], list):
        return bad_request('authorize need json permissions field or not a list')
    permissions = request.get_json()['permissions']
    for per in permissions:
        user.permission &= (~per)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'unauthorize successful',
            'data' : {}
            })

