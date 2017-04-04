#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, Logistic
from . import api
from decorators import permission_required
from errors import bad_request

@api.route('/logistic/headers', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['read'])
def get_logistic_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : Logistic.get_ordered_headers()
            })

@api.route('/logistic', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['read'])
def get_logistics():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    logistics = []
    if state is None:
        logistics = Logistic.query.all()
    else:
        logistics = Logistic.query.filter_by(state=state).all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers' : Logistic.get_ordered_headers(),
            'logistics' : [logis.to_json() for logis in logistics]
            }
            })

@api.route('/logistic/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['read'])
def get_logistic(id):
    logis = Logistic.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : logis.to_json()
            })

@api.route('/logistic', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['write'])
def new_logistic():
    logis = None
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print request_json
    try:
        logis = Logistic()
        logis.equipment_name = request_json.get('equipment_name') or None
        logis.delivery_address = request_json.get('delivery_address') or None
        logis.equipment_type = request_json.get('equipment_type') or None
#logis.delivery_status = request_json.get('delivery_status') or None
        logis.delivery_status = u'未完成'
        logis.state = 1

        db.session.add(logis)
        db.session.commit()
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 403

    return jsonify({
            'error' : 0,
            'msg' : u'添加物流单成功',
            'data' : logis.to_json()
            })

@api.route('/logistic/<int:id>', methods=['PUT'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['write'])
def modify_logistic(id):
    logis = Logistic.query.get_or_404(id)
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print request_json
    try:
        logis = Logistic()
        if request_json.get('equipment_name'):
            logis.equipment_name = request_json.get('equipment_name') or None
        if request_json.get('delivery_address'):
            logis.delivery_address = request_json.get('delivery_address') or None
        if request_json.get('equipment_type'):
            logis.equipment_type = request_json.get('equipment_type') or None
#logis.delivery_status = request_json.get('delivery_status') or None
        if request_json.get('delivery_status'):
            logis.delivery_status = request_json.get('delivery_status') or u'未完成'
        logis.state = 1

        db.session.add(logis)
        db.session.commit()
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 403

    return jsonify({
            'error' : 0,
            'msg' : u'添加物流单成功',
            'data' : logis.to_json()
            })

@api.route('/logistic/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['approve'])
def delete_logistic(id):
    logis = Logistic.query.get_or_404(id)
    db.session.delete(logis)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'删除物流单成功',
            'data' : {}
            })

@api.route('/logistic/approve/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['logistic']['approve'])
def approve_logistic(id):
    logis = Logistic.query.get_or_404(id)
    logis.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'审批物流单成功',
            'data' : {}
            })

