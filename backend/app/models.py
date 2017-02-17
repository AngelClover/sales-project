#!/usr/bin/env python
#-*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
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
    state = db.Column(db.Integer) #当前的状态 0:正常状态， 1:需要审批状态

    def __init__(self, info, abbr, type, spec, model, producer):
        self.info = info
        self.abbr = abbr
        self.type = type
        self.spec = spec
        self.model = model
        self.producer = producer
        self.state = 1
    
    def to_json(self):
        equip_json = { 'id' : self.id,
            'info' : self.info,
            'abbr' : self.abbr,
            'type' : self.type,
            'spec' : self.spec,
            'model' : self.model,
            'producer' : self.producer,
            'state' : self.state
        } 
        return equip_json

class Permission:
    EQUIPMENT_WRITE = 0x01
    EQUIPMENT_APPROVE = 0x03
    ENTERPRISE_WRITE = 0x04
    PURCHASE_ORDER_WRITE = 0x10
    PURCHASE_ORDER_APPROVE = 0x30
    SALES_ORDER_WRITE = 0x40
    SALES_ORDER_APPROVE = 0xc0
    ADMINISTER = 0xffff

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=0)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def to_json(self):
        user_json = {'id' : self.id,
            'email' : self.email,
            'username' : self.username
        }
        return user_json

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        return True
    
    def can(self, permissions):
        return self.permission == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

class AnonymousUser:
    def can(self, permissions):
        return False
    def is_administrator(self):
        return False


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
