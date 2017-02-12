#!/usr/bin/env python
#-*- coding:utf-8 -*-
from . import db

class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)#产品ID
    info = db.Column(db.String(256), unique=True)#产品信息
    abbr = db.Column(db.String(256), unique=True)#产品简称
    type = db.Column(db.String(256))#产品类型，可选的类型
    spec = db.Column(db.String(256))#产品规格
    model = db.Column(db.String(256))#产品型号
    producer = db.Column(db.String(256))#产品厂家

    def __init__(self, info, abbr, type, spec, model, producer):
        self.info = info
        self.abbr = abbr
        self.type = type
        self.spec = spec
        self.model = model
        self.producer = producer
    
    def to_json(self):
        equip_json = { 'id' : self.id,
            'info' : self.info,
            'abbr' : self.abbr,
            'type' : self.type,
            'spec' : self.spec,
            'model' : self.model,
            'producer' : self.producer
        } 
        return equip_json



def init_db():
    db.create_all()
    db.session.commit()
    table_names = []
    for clazz in db.Model._decl_class_registry.values():
        try:
            table_names.append(clazz.__tablename__)
        except:
            pass
    #set utf8 or not work well
    for table in table_names:
        db.engine.execute("alter table %s convert to character set utf8" % table)
    print table_names
