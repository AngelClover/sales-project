#-*- coding:utf-8 -*-

from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User
from .. import db
from .errors import bad_request, unauthorized, forbidden


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/users/', methods=['POST'])
def new_user():
    user_json = request.get_json()
    if user_json is None:
        return bad_request('user json data error')
    new_user = None
    try:
        email = user_json['email']
        name = user_json['name']
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


