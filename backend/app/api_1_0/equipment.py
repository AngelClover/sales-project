#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Permission, Store
from . import api
from decorators import permission_required
from errors import bad_request
import json


@api.route('/equipment/headers', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['read'])
def get_equipment_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : Equipment.get_ordered_headers()
            })

@api.route('/equipment', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['read'])
def get_equipments():
    state = int(request.args.get('state')) if request.args.get('state') is not None else None
    equips = []
    if state is None:
        equips = Equipment.query.all()
    else:
        equips = Equipment.query.filter_by(state=state).all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers': Equipment.get_ordered_headers(),
            'equipments': [equip.to_json() for equip in equips]
            }
            })
        

@api.route('/equipment/<int:id>', methods=['GET'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['read'])
def get_equipment(id):
    equip = Equipment.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : equip.to_json()
            })


@api.route('/equipment', methods=['POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['write'])
def new_equipment():
    equip_json = request.get_json()
    if equip_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print equip_json
    print 'asd'
    equip = None
    try:
        info = None #equip_json['info'] or None
        abbr = None #equip_json['abbr'] or None
        type = None #equip_json['type'] or None
        spec = None #equip_json['spec'] or None
        model = None #equip_json['model'] or None
        producer = None #equip_json['producer'] or None

        a = {}
        for item in equip_json:
            if item != 'id' and item != 'state':
                a[item] = equip_json[item]
        accessory = json.dumps(a)

        equip = Equipment(info, abbr, type, spec, model, producer, accessory)
        db.session.add(equip)
        db.session.commit()
    except Exception, e:
        print e
        return jsonify({
                'error' : 2,
                'msg' : 'fields not complete or error:info|abbr|spec|model|producer|accessory',
                'data' : {}
                }), 403
    
    return jsonify({
            'error' : 0,
            'msg' : u'添加首营设备成功',
            'data' : equip.to_json()
            })

@api.route('/equipment/<int:id>', methods=['PUT'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['approve'])
def edit_equipment(id):
    equip = Equipment.query.get_or_404(id)

    equip_json = request.get_json()
    if equip_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print equip_json
    if equip_json.get('info') is not None:
        equip.info = equip_json['info']
    if equip_json.get('abbr') is not None:
        equip.abbr = equip_json['abbr']
    if equip_json.get('type') is not None:
        equip.type = equip_json['type']
    if equip_json.get('spec') is not None:
        equip.spec = equip_json['spec']
    if equip_json.get('model') is not None:
        equip.model = equip_json['model']
    if equip_json.get('producer') is not None:
        equip.producer = equip_json['producer']

    a = {}
    for item in equip_json:
        if item != 'id' and item != 'state':
            a[item] = equip_json[item]
    equip.accessory = json.dumps(a)

    db.session.commit()

    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : equip.to_json()
            })
 
@api.route('/equipment/approve/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['approve'])
def approve_new_equipment(id):
    equip = Equipment.query.get(id)
    if equip is None:
        return bad_request('no such a equipment')
    equip.state = 0
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : equip.to_json()
            })

@api.route('/equipment/<int:id>', methods=['DELETE'])
@permission_required(Permission.MODULE_PERMISSION_DICT['equipment']['approve'])
def delete_equipment(id):
    equip = Equipment.query.get(id)
    if equip is None:
        return bad_request('no such a equipment')
    db.session.delete(equip)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : 'delete equipment successful',
            'data' : {}
            })

@api.route('/equipment/get_store/<int:id>', methods=['GET', 'POST'])
@permission_required(Permission.MODULE_PERMISSION_DICT['store']['write'])
def get_store_equipoment(id):
    equip = Equipment.query.get(id)
    if equip is None:
        return bad_request('no such a equipment')
    print "get store equipment id", id, len(equip.stores)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : [store.to_json() for store in equip.stores]
            })
