#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Enterprise, Permission
from . import api
from decorators import permission_required
from errors import bad_request
import json

@api.route('/enterprise/headers', methods=['GET', 'POST'])
def get_enterprise_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : Enterprise.get_ordered_headers()
            })

@api.route('/enterprise', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['enterprise']['read'])
def get_enterprises():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    enterprises = []
    if state is None:
        enterprises = Enterprise.query.all()
    else:
        enterprises = Enterprise.query.filter_by(state=state).all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers' : Enterprise.get_ordered_headers(),
            'enterprises' : [enterprise.to_json() for enterprise in enterprises]
            }})


@api.route('/enterprise/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['enterprise']['read'])
def get_enterprise(id):
    enterprise = Enterprise.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : enterprise.to_json()
            })

@api.route('/enterprise', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['enterprise']['write'])
def new_enterprise():
    enterprise_json = request.get_json()
    if enterprise_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print enterprise_json
    try:
        name = enterprise_json['name']
        register_capital = enterprise_json.get('register_capital') or 0 
        abbr = enterprise_json.get('abbr') or None
        type = enterprise_json.get('type') or None
        ever_name = enterprise_json.get('ever_name') or None
        legal_representor = enterprise_json.get('legal_representor') or None
        location = enterprise_json.get('location') or None
        establish_date = enterprise_json.get('establish_date') or None
        a = {}
        for item in enterprise_json:
            print item
            if item != 'id':
                a[item] = enterprise_json[item]
        accessory = json.dumps(a)
        enterprise = Enterprise(name, register_capital, abbr, type, ever_name, legal_representor, location, establish_date, accessory)
        db.session.add(enterprise)
        db.session.commit()
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : 'fields not complete or error:name|register_capital|abbr|type|ever_name|legal_representor|location|estabilish_date|accessory',
                'data' : {}
                }), 404
    
    return jsonify({
            'error' : 0,
            'msg' : u'添加首营企业成功',
            'data' : enterprise.to_json()
            })

@api.route('/enterprise/<int:id>', methods=['PUT'])
@permission_required(Permission.MODULE_PERMISSION_DICT['enterprise']['approve'])
def edit_enterprise(id):
    enterprise = Enterprise.query.get_or_404(id)
    enterprise_json = request.get_json()
    if enterprise_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print enterprise_json
#if enterprise_json.get('name'):
#        enterprise.name = enterprise_json['name']
#    if enterprise_json.get('register_capital'):
#        enterprise.register_capital = enterprise_json['register_capital']
#    if enterprise_json.get('abbr'):
#        enterprise.abbr = enterprise_json['abbr']
#    if enterprise_json.get('type'):
#        enterprise.type = enterprise_json['type']
#    if enterprise_json.get('ever_name'):
#        enterprise.ever_name = enterprise_json['ever_name']
#    if enterprise_json.get('legal_representor'):
#        enterprise.legal_representor = enterprise_json['legal_representor']
#    if enterprise_json.get('location'):
#        enterprise.location = enterprise_json['location']
#    if enterprise_json.get('establish_date'):
#        enterprise.establish_date = enterprise_json['establish_date']
    a = {}
    for item in enterprise_json:
        if item != 'id':
            a[item] = enterprise_json[item]
    enterprise.accessory = json.dumps(a)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : enterprise.to_json()
        })

@api.route('/enterprise/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['enterprise']['approve'])
def delete_enterprise(id):
    enterprise = Enterprise.query.get(id)
    if enterprise is None:
        return bad_request('no such a enterprise')
    db.session.delete(enterprise)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'delete enterprise successful',
            'data' : {}
            })
