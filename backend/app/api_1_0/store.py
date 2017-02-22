#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, Store
from . import api
from decorators import permission_required
from errors import bad_request

@api.route('/store/headers', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['read'])
def get_store_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : Store.get_ordered_headers()
            })

@api.route('/store', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['read'])
def get_stores():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    stores = []
    if state is None:
        stores = Store.query.all()
    else:
        stores = Store.query.filter_by(state=state).all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers' : Store.get_ordered_headers(),
            'stores' : [store.to_json() for store in stores]
            }
            })

@api.route('/store/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['read'])
def get_store(id):
    store = Store.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : store.to_json()
            })

@api.route('/store', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def new_store():
    store = None
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print request_json
    try:
        store = Store()
        store.equipment_name = request_json.get('equipment_name') or None
        store.store_number = request_json.get('store_number') or None
        store.abbr = request_json.get('abbr') or None
        store.equipment_type = request_json.get('equipment_type') or None
        store.state = 1

        db.session.add(store)
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
            'data' : store.to_json()
            })

@api.route('/store/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['approve'])
def delete_store(id):
    store = Store.query.get_or_404(id)
    db.session.delete(store)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'删除物流单成功',
            'data' : {}
            })

@api.route('/store/approve/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['approve'])
def approve_store(id):
    store = Store.query.get_or_404(id)
    store.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'审批物流单成功',
            'data' : {}
            })

