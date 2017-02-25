#-*- coding:utf-8 -*-

from flask import jsonify, request, current_app, url_for, g
from flask_login import login_required
from . import api
from ..models import User, AnonymousUser
from .. import db
from .errors import bad_request, unauthorized, forbidden
from .authentication import auth
from .decorators import permission_required, admin_required


@api.route('/users/<int:id>')
@auth.login_required
def get_user(id):
    if isinstance(g.current_user, AnonymousUser) or g.current_user.id != id:
            return forbidden('not allowed')
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/users', methods=['POST'])
def new_user():
    user_json = request.get_json()
    if user_json is None:
        return bad_request('user json data error')
    new_user = None
    try:
        email = user_json['email']
        name = user_json['username']
        password = user_json['password']
        new_user = User(email, name, password)
        print "%s,%s,%s" % (email, name, password)
    except Exception as e:
        return bad_request('email|name|password is not in json')

    if new_user is not None:
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            db.session.rollback()
            return bad_request('email or username duplicated')
    else:
        return bad_request('something error, can\'t add to db')

    return jsonify({
            'error' : 0,
            'msg' : 'add new user successful',
            'data' : new_user.to_json(),
            })

@api.route('/users/<int:id>', methods=['DELETE'])
@admin_required()
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return bad_request('no such a user')
    try:
        db.session.delete(user)
        db.session.commit()
    except:
        db.session.rollback()
        return bad_request('delete user internal error')

    return jsonify({
            'error' : 0,
            'msg' : 'delete user successful',
            'data' : {}
            })

@api.route('/users/<int:id>', methods=['PUT'])
@auth.login_required
def change_user(id):
    user = User.query.get(id)
    if user is None:
        return bad_request('no such a user')
    try:
        if 'name' in request.get_json():
            user.username = request.get_json()['name']
        if 'password' in request.get_json():
            user.password = request.get_json()['password']
        if 'email' in request.get_json():
            user.email = request.get_json()['email']
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print e
        return bad_request('modify user internal error')

    return jsonify({
            'error' : 0,
            'msg' : 'modify user successful',
            'data' : {}
            })

@api.route('/users/login_token', methods=['GET', 'POST'])
@auth.login_required
def get_login_token():
    if isinstance(g.current_user, AnonymousUser) or g.token_used:
        return unauthorized('AnonymousUser or already has a token')
    return jsonify({
            'error' : 0,
            'msg' : 'successful',
            'data' : {'user' : g.current_user.to_json(),
            'token' : g.current_user.generate_auth_token(expiration=3600),
            'expiration' : 3600
            }
            })

@api.route('/users/me', methods=['GET', 'POST'])
@auth.login_required
def get_me():
    if isinstance(g.current_user, AnonymousUser) or g.token_used:
        return unauthorized('Invalid credentials')
    return jsonify({
            'error' : 0,
            'msg' : 'successful',
            'data' : {'user' : g.current_user.to_json()}
            })

