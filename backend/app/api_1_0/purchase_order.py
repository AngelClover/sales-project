#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, PurchaseOrder, PurchaseEquipment, Store
from . import api
from decorators import permission_required
from errors import bad_request

@api.route('/purchase/headers', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['read'])
def get_purchase_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : PurchaseOrder.get_ordered_headers()
            })

@api.route('/purchase', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['read'])
def get_purchase_orders():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    orders = []
    if state is None:
        orders = PurchaseOrder.query.all()
    else:
        orders = PurchaseOrder.query.filter_by(state=state).all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers' : PurchaseOrder.get_ordered_headers(),
            'purchase_orders' : [order.to_json() for order in orders]
            }
            })

@api.route('/purchase/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['read'])
def get_purchase_order(id):
    order = PurchaseOrder.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : order.to_json()
            })

@api.route('/purchase', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['write'])
def new_purchase_order():
    order = None
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print request_json
    try:
        order = PurchaseOrder()
        order.sign_date = request_json.get('sign_date') or None
        order.provider_info = request_json.get('provider_info') or None
        order.billing_company = request_json.get('billing_company') or None
        order.arrive_date = request_json.get('arrive_date') or None
        order.get_location = request_json.get('get_location') or None
        order.pay_mode = request_json.get('pay_mode') or None
        order.invoice_type = request_json.get('invoice_type') or None
        order.postage_account = request_json.get('postage_account') or None
        order.state = 1
        #check equipments exist
        equips = request_json.get('equipment_infos') or []
        for e in equips:
            if e.get('equipment_id') is None:
                return jsonify({
                        'error' : 3,
                        'msg' : 'equipment id not exist'
                        })
            Equipment.query.get_or_404(e['equipment_id'])

        #add order for get purchase order id
        db.session.add(order)
        db.session.commit()
        #add equipment
        for e in equips:
            pe = PurchaseEquipment()
            pe.purchase_id = order.id
            pe.equipment_id = e['equipment_id']
            pe.warranty_period = e.get('warranty_period') or None
            pe.install_require = e.get('install_require') or None
            pe.measurement_unit = e.get('measurement_unit') or None
            pe.unit_price = e.get('unit_price') or 0
            pe.quantity = e.get('quantity') or 0
            pe.total_price = float(pe.unit_price) * float(pe.quantity)
            pe.product_configure = e.get('product_configure') or None
            db.session.add(pe)
        db.session.commit()
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 403

    return jsonify({
            'error' : 0,
            'msg' : u'添加采购订单成功',
            'data' : order.to_json()
            })

@api.route('/purchase/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['approve'])
def delete_purchase_order(id):
    purchase_order = PurchaseOrder.query.get_or_404(id)
    for p in purchase_order.purchase_equipments:
        db.session.delete(p)
    db.session.delete(purchase_order)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'delete purchase order successful',
            'data' : {}
            })

@api.route('/purchase/approve/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['approve'])
def approve_purchase_order(id):
    purchase_order = PurchaseOrder.query.get_or_404(id)
    purchase_order.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'approve purchase order successful',
            'data' : {}
            })

@api.route('/purchase/can_store/<int:id>', methods=['GET', 'POSt'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['write'])
def purchase_can_store(id):
    p_order = PurchaseOrder.query.get_or_404(id)
    if p_order.state != 0:
        return bad_request('cannot store a purchase order, that\'s state is not approved')
    p_order.state = 2
    db.session.commit()
    return jsonify({'error' : 0, 'msg' : ''})

@api.route('/purchase/store_one/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def store_one_equipment(id):
    p_equipment = PurchaseEquipment.query.get_or_404(id)
    if p_equipment.purchase_order.state != 2:
        return bad_request('purchase order not at ready to store state') 
    if p_equipment.stored == 1:
        return bac_request('already stored in houseware')
    p_equipment.stored = 1
    equipments = p_equipment.purchase_order.purchase_equipments
    part_stored = False;
    for e in equipments:
        if e.stored != 1:
            part_stored = True
            break
    #部分入库
    p_equipment.purchase_order.total_stored = 1
    if not part_stored:
        #完全入库
        p_equipment.purchase_order.total_stored = 2 
    db.session.commit()
    #add store element
    new_store = Store()
    new_store.equipment_id = p_equipment.equipment_id
    new_store.purchase_id = p_equipment.purchase_order.id
    new_store.store_number = p_equipment.quantity
    new_store.state = 1
    db.session.add(new_store)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'store one equipment successful',
            'data' : {}
            })

@api.route('/purchase/store_all/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def store_all_equipments(id):
    p_order = PurchaseOrder.query.get_or_404(id)
    if p_order.state != 2:
        return bad_request('purchase order not at ready to store state') 

    for p_equipment in p_order.purchase_equipments:
        if p_equipment.stored == 1:
            continue
        new_store = Store()
        new_store.equipment_id = p_equipment.equipment_id
        new_store.purchase_id = p_equipment.purchase_order.id
        new_store.store_number = p_equipment.quantity
        new_store.state = 1
        db.session.add(new_store)
        p_equipment.stored = 1
    p_order.total_stored = 2
    db.session.commit()

    return jsonify({
            'error' : 0,
            'msg' : 'store one equipment successful',
            'data' : {}
            })
