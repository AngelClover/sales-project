#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, PurchaseOrder, PurchaseEquipment
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

