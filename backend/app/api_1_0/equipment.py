#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment
from . import api


@api.route('/equipments/headers', methods=['GET', 'POST'])
def get_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
                'headers' : [('id', '产品编号'), ('info', u'产品信息'), ('abbr', u'产品简称'), ('type', u'产品分类'),
                        ('spec', u'产品规格'), ('model', u'产品型号'), ('producer', u'厂家')]
            }
            })

@api.route('/equipments/', methods=['GET'])
def get_equipments():
    equips = Equipment.query.all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'equipments': [equip.to_json() for equip in equips]
            }
            })
        

@api.route('/equipments/<int:id>', methods=['GET'])
def get_equipment(id):
    equip = Equipment.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'equipment' : equip.to_json()
            }
            })


@api.route('/equipments/', methods=['POST'])
def new_equipment():
    equip_json = request.get_json()
    if equip_json is None:
        return jsonify({
                'error' : 1,
                'msg' : u'不是application/json类',
                'data' : {}
                }), 403
    print equip_json
    try:
        info = equip_json['info']
        abbr = equip_json['abbr'] 
        type = equip_json['type']
        spec = equip_json['spec']
        model = equip_json['model']
        producer = equip_json['producer']
    except Exception, e:
        return jsonify({
                'error' : 2,
                'msg' : 'fields not complete or error:info|abbr|spec|model|producer',
                'data' : {}
                }), 404
    
    equip = Equipment(info, abbr, type, spec, model, producer)
    db.session.add(equip)
    db.session.commit()
    return jsonify({
            'error' : 0,
            'msg' : u'添加首营设备成功',
            'data' : equip.to_json()
            })

@api.route('/equipments/<int:id>', methods=['PUT'])
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
        equip.info = equip_json['abbr']
    if equip_json.get('type') is not None:
        equip.info = equip_json['type']
    if equip_json.get('spec') is not None:
        equip.info = equip_json['spec']
    if equip_json.get('model') is not None:
        equip.info = equip_json['model']
    if equip_json.get('producer') is not None:
        equip.info = equip_json['producer']
    db.session.add(equip)
    db.session.commit()

    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : equip.to_json()
            })
 
