#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, SaleOrder, SaleEquipment
from . import api
from decorators import permission_required
from errors import bad_request
import datetime

@api.route('/sale/headers', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['read'])
def get_sale_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : SaleOrder.get_ordered_headers()
            })

@api.route('/sale', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['read'])
def get_sale_orders():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    orders = []
    if state is None:
        orders = SaleOrder.query.all()
    else:
        orders = SaleOrder.query.filter_by(state=state).all()

    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers' : SaleOrder.get_ordered_headers(),
            'sale_orders' : [order.to_json() for order in orders]
            }
            })

@api.route('/sale/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['read'])
def get_sale_order(id):
    order = SaleOrder.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : order.to_json()
            })

@api.route('/sale', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['write'])
def new_sale_order():
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
        order = SaleOrder()
#order.sign_date = request_json.get('sign_date') or None
        sd = request_json.get('sign_date') or "1970-01-01"
        if sd is not None:
            sd = sd.strip(' ')
            order.sign_date = datetime.datetime.strptime(sd, "%Y-%m-%d")
        else:
            order.sign_date = None
        order.provider_info = request_json.get('provider_info') or None
        order.billing_company = request_json.get('billing_company') or None
#order.arrive_date = request_json.get('arrive_date') or None
        ad = request_json.get('arrive_date') or "1970-01-01 00:00:00"
        if ad is not None:
            ad = ad.strip(' ')
            try:
                order.arrive_date = datetime.datetime.strptime(ad, "%Y-%m-%d %H:%M:%S")
            except Exception, e:
                print e
                order.arrive_date = datetime.datetime.strptime(ad, "%Y-%m-%d %H%M%S")
        else:
            order.arrive_date = None
        order.get_location = request_json.get('get_location') or None
        order.pay_mode = request_json.get('pay_mode') or None
        order.invoice_type = request_json.get('invoice_type') or None
        order.create_user = request_json.get('create_user') or None
        if order.create_user is None:
            order.create_user = g.current_user.id
        order.approve_user = request_json.get('approve_user') or None
        order.contract = request_json.get('contract') or None
        order.state = 1
        #check equipments exist
        equips = request_json.get('equipments') or []
        for e in equips:
            if e.get('equipment_id') is None:
                return jsonify({
                        'error' : 3,
                        'msg' : 'equipment id not exist'
                        })
            Equipment.query.get_or_404(e['equipment_id'])

        #add order for get sale order id
        db.session.add(order)
        db.session.commit()
        #add equipment
        for e in equips:
            pe = SaleEquipment()
            pe.sale_id = order.id
            pe.equipment_id = e['equipment_id']
            pe.service_commitment = e.get('service_commitment') or None
            pe.warranty_period = e.get('warranty_period') or None
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
            'msg' : u'添加销售订单成功',
            'data' : order.to_json()
            })


@api.route('/sale/<int:id>', methods=['PUT'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['write'])
def modify_sale_order(id):
    order = SaleOrder.query.get_or_404(id)
    request_json = request.get_json()
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print request_json
    if order.state < 0:
        return jsonify({
                'error' : 1,
                'msg' : u'state is %d, 不能修改' % order.state,
                'data' : {}
                }), 403
    try:
        for p in order.sale_equipments:
            db.session.delete(p)
#order = SaleOrder()
#order.sign_date = request_json.get('sign_date') or None
        sd = request_json.get('sign_date') or "1970-01-01"
        if sd is not None:
            sd = sd.strip(' ')
            order.sign_date = datetime.datetime.strptime(sd, "%Y-%m-%d")
        else:
            order.sign_date = None
        order.provider_info = request_json.get('provider_info') or None
        order.billing_company = request_json.get('billing_company') or None
#order.arrive_date = request_json.get('arrive_date') or None
        ad = request_json.get('arrive_date') or "1970-01-01 00:00:00"
        if ad is not None:
            ad = ad.strip(' ')
            try:
                order.arrive_date = datetime.datetime.strptime(ad, "%Y-%m-%d %H:%M:%S")
            except Exception, e:
                print e
                order.arrive_date = datetime.datetime.strptime(ad, "%Y-%m-%d %H%M%S")
        else:
            order.arrive_date = None
        order.get_location = request_json.get('get_location') or None
        order.pay_mode = request_json.get('pay_mode') or None
        order.invoice_type = request_json.get('invoice_type') or None
        if request_json.get('create_user'):
            order.create_user = request_json.get('create_user')
        if request_json.get('approve_user'):
            order.approve_user = request_json.get('approve_user')
        order.state = 1
        order.contract = request_json.get('contract') or None
        #check equipments exist
        equips = request_json.get('equipments') or []
        for e in equips:
            if e.get('equipment_id') is None:
                return jsonify({
                        'error' : 3,
                        'msg' : 'equipment id not exist'
                        })
            Equipment.query.get_or_404(e['equipment_id'])

        #add order for get sale order id
#db.session.add(order)
        x = order.to_json()
#db.session.commit()
        #add equipment
        print "VI", equips
        for e in equips:
            pe = SaleEquipment()
            pe.sale_id = order.id
            pe.equipment_id = e['equipment_id']
            pe.service_commitment = e.get('service_commitment') or None
            pe.warranty_period = e.get('warranty_period') or None
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
            'msg' : u'修改销售订单%d成功' % id,
            'data' : order.to_json()
            })

@api.route('/sale/confirm/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['write'])
def confirm_sale_order(id):
    sale_order = SaleOrder.query.get_or_404(id)
    if sale_order.state != 0:
        return bad_request('cannot store a sale order, that\'s state is not confirmed')
    sale_order.state = -2
    db.session.commit()
    return jsonify({'error' : 0, 'msg' : ''})

@api.route('/sale/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['approve'])
def delete_sale_order(id):
    sale_order = SaleOrder.query.get_or_404(id)
    for p in sale_order.sale_equipments:
        db.session.delete(p)
    db.session.delete(sale_order)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'delete sale order successful',
            'data' : {}
            })

@api.route('/sale/approve/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['approve'])
def approve_sale_order(id):
    sale_order = SaleOrder.query.get_or_404(id)
    if sale_order.state != 1:
        return bad_request('wrong order number, cannot approve')

    try:
        request_json = request.get_json()
        if request_json.get('approve_user'):
            sale_order.approve_user = request_json.get('approve_user')
        if sale_order.approve_user is None:
            sale_order.approve_user = g.current_user.id
    except Exception, e:
        print e
        return jsonify({
                'error' : 1,
                'msg' : 'approve_user cannot get',
                'data' : ''
                })

    sale_order.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'approve sale order successful',
            'data' : {}
            })

"""
@api.route('/sale/next/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['sale']['approve'])
def approve_sale_order(id):
    sale_order = SaleOrder.query.get_or_404(id)
    if sale_order.state  <= -4:
        return bad_request('wrong order number, cannot give impetus')
    sale_order.state -= 1
    if sale_order.state == -1:
        sale_order.state -= 1
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'approve sale order successful',
            'data' : {}
            })
"""
