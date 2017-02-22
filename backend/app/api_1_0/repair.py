#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, Repair
from . import api
from decorators import permission_required
from errors import bad_request

@api.route('/repair/headers', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['repair']['read'])
def get_repair_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : Repair.get_ordered_headers()
            })

@api.route('/repair', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['repair']['read'])
def get_repairs():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    repairs = []
    if not state:
        repairs = Repair.query.all()
    else:
        repairs = Repair.query.filter_by(state=state).all()

    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers' : Repair.get_ordered_headers(),
            'repairs' : [repair.to_json() for repair in repairs]
            }
            })

@api.route('/repair/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['repair']['read'])
def get_repair(id):
    repair = Repair.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : repair.to_json()
            })

@api.route('/repair', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['repair']['write'])
def new_repair():
    repair = None
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print request_json
    try:
        repair = Repair()
        repair.equipment_name = request_json.get('equipment_name') or None
        repair.repair_address = request_json.get('repair_address') or None
        repair.equipment_type = request_json.get('equipment_type') or None
        repair.repair_status = request_json.get('repair_status') or None
        repair.state = 1

        db.session.add(repair)
        db.session.commit()
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 403

    return jsonify({
            'error' : 0,
            'msg' : u'添加维修单成功',
            'data' : repair.to_json()
            })

@api.route('/repair/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['repair']['approve'])
def delete_repair(id):
    repair = Repair.query.get_or_404(id)
    db.session.delete(repair)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'删除维修单成功',
            'data' : {}
            })

@api.route('/repair/approve/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['repair']['approve'])
def approve_repair(id):
    repair = Repair.query.get_or_404(id)
    repair.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'审批维修单成功',
            'data' : {}
            })

