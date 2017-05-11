#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, PurchaseOrder, PurchaseEquipment, Store
from . import api
from decorators import permission_required
from errors import bad_request
import datetime

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
    print "I", request_json
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print "II", request_json
    try:
        order = PurchaseOrder()
#sd = request_json.get('sign_date') or None
        sd = request_json.get('sign_date') or "1970-01-01"
        if sd is not None:
            sd = sd.strip(' ')
            order.sign_date = datetime.datetime.strptime(sd, "%Y-%m-%d")
        else:
            order.sign_date = None
        order.provider_info = request_json.get('provider_info') or None
        order.billing_company = request_json.get('billing_company') or None
#ad = request_json.get('arrive_date') or None
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
        order.postage_account = request_json.get('postage_account') or None
        order.create_user = request_json.get('create_user') or None
        if order.create_user is None:
            order.create_user = g.current_user.id
        order.approve_user = request_json.get('approve_user') or None
        order.state = 1
        #check equipments exist
        equips = request_json.get('equipments') or []
        print "III"
#order.purchase_equipments = []
        for e in equips:
            if e.get('equipment_id') is None:
                return jsonify({
                        'error' : 3,
                        'msg' : 'equipment id not exist'
                        })
            Equipment.query.get_or_404(e['equipment_id'])

        print "IV", equips
        x = order.to_json()
        print "V", x
        #add order for get purchase order id
        db.session.add(order)
        db.session.commit()
        #add equipment
        print "VI", equips
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
        print e
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 400

    return jsonify({
            'error' : 0,
            'msg' : u'添加采购订单成功',
            'data' : order.to_json()
            })


@api.route('/purchase/<int:id>', methods=['PUT'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['read'])
def modify_purchase_order(id):
    order = PurchaseOrder.query.get_or_404(id) 
    request_json = request.get_json()
    print "I", request_json, id
    if request_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print "II", request_json
    if order.state < 0:
        return jsonify({
                'error' : 1,
                'msg' : 'state is %d' % order.state,
                'data' : {}
                }), 403
    try:
#delete old relation
        for p in order.purchase_equipments:
            db.session.delete(p)

        sd = request_json.get('sign_date') or None
        if sd is not None:
            sd = sd.strip(' ')
            order.sign_date = datetime.datetime.strptime(sd, "%Y-%m-%d")
        if request_json.get('provider_info'):
            order.provider_info = request_json.get('provider_info')
        if request_json.get('billing_company'):
            order.billing_company = request_json.get('billing_company')
#ad = request_json.get('arrive_date') or None
        ad = request_json.get('arrive_date') or None
        if ad is not None:
            ad = ad.strip(' ')
            order.arrive_date = datetime.datetime.strptime(ad, "%Y-%m-%d %H:%M:%S")
        if request_json.get('get_location'):
            order.get_location = request_json.get('get_location')
        if request_json.get('pay_mode'):
            order.pay_mode = request_json.get('pay_mode')
        if request_json.get('invoice_type'):
            order.invoice_type = request_json.get('invoice_type')
        if request_json.get('postage_account'):
            order.postage_account = request_json.get('postage_account')
        if request_json.get('create_user'):
            order.create_user = request_json.get('create_user')
        if request_json.get('approve_user'):
            order.approve_user = request_json.get('approve_user')
        order.state = 1
        #check equipments exist
        equips = request_json.get('equipments') or []

        print "III"
#order.purchase_equipments = []
        for e in equips:
            if e.get('equipment_id') is None:
                return jsonify({
                        'error' : 3,
                        'msg' : 'equipment id not exist'
                        })
            Equipment.query.get_or_404(e['equipment_id'])

        x = order.to_json()
#db.session.commit()
#TODO:
        print "VI", equips
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
        print e
        return jsonify({
                'error' : 2,
                'msg' : e.message,
                'data' : {}
                }), 403
    return jsonify({
            'error' : 0,
            'msg' : u'修改采购订单%d成功' % id,
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
    if purchase_order.state != 1:
        return bad_request('wrong order number, cannot approve')

    try:
        request_json = request.get_json()
        if request_json is not None:
            if request_json.get('approve_user'):
                purchase_order.approve_user = request_json.get('approve_user')
        if purchase_order.approve_user is None:
            purchase_order.approve_user = g.current_user.id
    except Exception, e:
        print e
        return jsonify({
                'error' : 1,
                'msg' : 'approve_user cannot get',
                'data' : ''
                })

    purchase_order.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'approve purchase order successful',
            'data' : {}
            })

@api.route('/purchase/can_store/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['purchase']['write'])
def purchase_can_store(id):
    p_order = PurchaseOrder.query.get_or_404(id)
    if p_order.state != 0:
        return bad_request('cannot store a purchase order, that\'s state is not approved')
    p_order.state = -2
    db.session.commit()
    return jsonify({'error' : 0, 'msg' : ''})

##########above is order related
##########equipment related is under

@api.route('/purchase/store_one/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def store_one_equipment(id):
    p_equipment = PurchaseEquipment.query.get_or_404(id)
    request_json = request.get_json()
    print request_json
    if p_equipment.purchase_order.state > -2:
        return bad_request('purchase order not at ready to store state') 
    if p_equipment.stored == 1:
        return bad_request('already stored in houseware')

    p_equipment.stored = 1
    stored_userid = int(request.args.get('stored_userid')) if request.args.get('stored_userid') is not None else None
    if stored_userid is None:
        stored_userid = g.current_user.id
    p_equipment.stored_user = stored_userid
    p_equipment.store_message = request_json.get('store_message') or None
    p_equipment.store_temperature = request_json.get('store_temperature') or None
    p_equipment.store_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    equipments = p_equipment.purchase_order.purchase_equipments
    part_stored = False;
    for e in equipments:
        if e.stored != 1:
            part_stored = True
            break
    #部分入库
    p_equipment.purchase_order.total_stored = 1
    p_equipment.purchase_order.state = -3
    if not part_stored:
        #完全入库
        p_equipment.purchase_order.total_stored = 2 
        p_equipment.purchase_order.state = -4 
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

@api.route('/purchase/receive_one/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def receive_one_equipment(id):
    p_equipment = PurchaseEquipment.query.get_or_404(id)
    request_json = request.get_json()
    print request_json
    if p_equipment.purchase_order.state > -2:
        return bad_request('purchase order not at ready to receive ') 
    if p_equipment.received == 1:
        return bad_request('already received')

    p_equipment.received = 1
    received_userid = int(request.args.get('received_userid')) if request.args.get('received_userid') is not None else None
    if received_userid is None:
        received_userid = g.current_user.id
    p_equipment.received_user = received_userid
    p_equipment.receive_message = request_json.get('receive_message') or None
    p_equipment.receive_temperature = request_json.get('receive_temperature') or None
    p_equipment.receive_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'receive one equipment successful',
            'data' : {}
            })

@api.route('/purchase/inspect_one/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def inspect_one_equipment(id):
    p_equipment = PurchaseEquipment.query.get_or_404(id)
    request_json = request.get_json()
    if p_equipment.purchase_order.state > -2:
        return bad_request('purchase order not at ready to inspect') 
    if p_equipment.inspected == 1:
        return bad_request('already inspected in houseware')

    p_equipment.inspected = 1
    inspected_userid = int(request.args.get('inspected_userid')) if request.args.get('inspected_userid') is not None else None
    if inspected_userid is None:
        inspected_userid = g.current_user.id
    inspect_ok_number = request_json.get('inspect_ok_number') or None
    if inspect_ok_number is not None:
        inspect_ok_number = int(inspect_ok_number)
    else:
        inspect_ok_number = p_equipment.quantity
    p_equipment.inspect_ok_number = inspect_ok_number
    p_equipment.inspect_message = request_json.get('inspect_message') or None
    p_equipment.inspect_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    p_equipment.inspected_user = inspected_userid
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'inspect one equipment successful',
            'data' : {}
            })

@api.route('/purchase/store_all/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def store_all_equipments(id):
    p_order = PurchaseOrder.query.get_or_404(id)
    request_json = request.get_json()
    print request_json
    if p_order.state > -2:
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
        stored_userid = int(request.args.get('stored_userid')) if request.args.get('stored_userid') is not None else None
        if stored_userid is None:
            stored_userid = g.current_user.id
        p_equipment.stored_user = stored_userid
        p_equipment.store_message = request_json.get('store_message') or None
        p_equipment.store_temperature = request_json.get('store_temperature') or None
        p_equipment.store_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    p_order.total_stored = 2
    p_order.state = -4
    db.session.commit()

    return jsonify({
            'error' : 0,
            'msg' : 'store all equipment successful',
            'data' : {}
            })

@api.route('/purchase/receive_all/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def receive_all_equipments(id):
    p_order = PurchaseOrder.query.get_or_404(id)
    request_json = request.get_json()
    print request_json
    if p_order.state > -2:
        return bad_request('purchase order not at ready to store state') 

    for p_equipment in p_order.purchase_equipments:
        if p_equipment.received == 1:
            continue
        p_equipment.received = 1
        received_userid = int(request.args.get('received_userid')) if request.args.get('received_userid') is not None else None
        if received_userid is None:
            received_userid = g.current_user.id
        p_equipment.received_user = received_userid
        p_equipment.receive_message = request_json.get('receive_message') or None
        p_equipment.receive_temperature = request_json.get('receive_temperature') or None
        p_equipment.receive_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.session.commit()

    return jsonify({
            'error' : 0,
            'msg' : 'received all equipment successful',
            'data' : {}
            })

@api.route('/purchase/inspect_all/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def inspect_all_equipments(id):
    p_order = PurchaseOrder.query.get_or_404(id)
    request_json = request.get_json()
    print request_json
    if p_order.state > -2:
        return bad_request('purchase order not at ready to store state') 

    for p_equipment in p_order.purchase_equipments:
        if p_equipment.inspected == 1:
            continue
        p_equipment.inspected = 1
        inspected_userid = int(request.args.get('inspected_userid')) if request.args.get('inspected_userid') is not None else None
        if inspected_userid is None:
            inspected_userid = g.current_user.id
        p_equipment.inspected_user = inspected_userid
        p_equipment.inspect_ok_number = inspect_ok_number
        p_equipment.inspect_message = request_json.get('inspect_message') or None
        p_equipment.inspect_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.session.commit()

    return jsonify({
            'error' : 0,
            'msg' : 'inspect all equipment successful',
            'data' : {}
            })
