#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, Store, SaleEquipment
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
        store.equipment_id = request_json.get('equipment_id') or None
        store.purchase_id = request_json.get('purchase_id') or None
        store.store_num = request_json.get('store_number') or None

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
            'msg' : u'不支持store的直接审批',
            'data' : {}
            })

@api.route('/store/out_store', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['approve'])
def out_store_equipments():
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    try:
        stores = request_json.get('store_equipments') or []
        sale_equipment_id = request_json['sale_equipment_id']
        sale_equipment = SaleEquipment.query.get(sale_equipment_id)
        if sale_equipment is None:
            return jsonify({'error' : 1, 'msg' : u'sale equipment id not exist'}), 404
        if sale_equipment.sale_order.state != 0:
            return jsonify({'error' : 1, 'msg' : u'not approved sale order'}), 400

        provide_quantity = 0
        for store_json in stores:
            number = int(store_json['number'])
            store_id = store_json['id']
            store = Store.query.get(store_id)
            if store is None:
                return jsonify({'error' : 1, 'msg' : u'store equipment id not eixst'}), 404
            if store.equipment_id != sale_equipment.equipment_id:
                return jsonify({'error' : 1, 'msg' : u'不是同一种器材，怎能出库'}), 400
            provide_quantity += number
            if store.store_number < number or provide_quantity > (sale_equipment.quantity - sale_equipment.outstore_quantity):
                return jsonify({'error' : 1, 'msg' : u'request number larger than store number, or larger than needed by sale order'}), 400
        for store_json in stores:
            number = int(store_json['number'])
            store_id = store_json['id']
            store = Store.query.get(store_id)
            store.store_number -= number
            sale_equipment.outstore_quantity += number
            db.session.commit()
        if sale_equipment.quantity == sale_equipment.outstore_quantity:
            sale_equipment.outstore_state = 2
        elif sale_equipment.outstore_quantity != 0:
            sale_equipment.outstore_state = 1

        part_outstored = False
        for s_equipment in sale_equipment.sale_order.sale_equipments:
            if s_equipment.outstore_state != 2:
                part_outstored = True
                break
        if part_outstored:
            sale_equipment.sale_order.total_outstore = 1
        else:
            sale_equipment.sale_order.total_outstore = 2
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 403


    return jsonify({
                'error' : 0,
                'msg' : u'出库成功',
                'data' : {}
                })

