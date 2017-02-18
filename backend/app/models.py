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
    
    @staticmethod
    def get_headers():
        return { 'id' : u'产品编号',
            'info' : u'产品信息',
            'abbr' : u'产品简称',
            'type' : u'产品分类',
            'spec' : u'产品规格',
            'model' : u'产品型号',
            'producer' : u'厂家'
        }
    @staticmethod
    def get_ordered_headers():
        return [('id', u'产品编号'),
            ('info', u'产品信息'),
            ('abbr' , u'产品简称'),
            ('type', u'产品分类'),
            ('spec' , u'产品规格'),
            ('model', u'产品型号'),
            ('producer', u'厂家')
        ]

class Producer(db.Model):
    __tablename__ = 'producer'
    id = db.Column(db.Integer, primary_key=True)#首营企业编号
    name = db.Column(db.String(256))#供应商名称
    register_capital = db.Column(db.Integer)#注册资金
    abbr = db.Column(db.String(256))#简称
    type = db.Column(db.String(256))#供应商类型(设备/试剂/耗材等)
    ever_name = db.Column(db.String(256))#曾用名
    legal_representor = db.Column(db.String(256))#法人代表
    location = db.Column(db.String(1024))#住所
    establish_date = db.Column(db.Date)#成立日期
    
    def to_json(self):
        producer_json = { 'id' : self.id,
            'name' : self.name,
            'register_capital' : self.register_capital,
            'abbr' : self.abbr,
            'type' : self.type,
            'ever_name' : self.ever_name,
            'legal_representor' : self.legal_representor,
            'location' : self.location,
            'establish_date' : self.establish_date
        }
        return producer_json
    
    @staticmethod
    def get_headers():
        headers = {
            'id' : u'首营企业编号(系统自动分配)',
            'name' : u'供应商名称',
            'register_capital' : u'注册资金',
            'abbr' : u'简称',
            'type' : u'供应商类型(设备/试剂/耗材等)',
            'ever_name' : u'曾用名',
            'legal_representor' : u'法人代表',
            'location' : u'住所',
            'establish_date' : u'成立日期'
        }
        return headers


class Permission:

    MODULE_PERMISSION_LIST = [
        ('equipment', {
         'read' : 0x01,
         'write' : 0x02,
         'approve' : 0x04
         }),
        ('enterprise', {
         'read' : 0x08,
         'write' : 0x10,
         'approve' : 0x20
         }),
        ('purchase', {
         'read' : 0x40,
         'write' : 0x80,
         'approve' : 0x100
         }),
        ('sale', {
         'read' : 0x200,
         'write' : 0x400,
         'approve' : 0x800
         }),
        ('store', {
         'read' : 0x1000,
         'write' : 0x2000,
         'approve' : 0x4000
         }),
        ('repair', {
         'read' : 0x8000,
         'write' : 0x10000,
         'approve' : 0x20000
         }),
        ('logistic', {
         'read' : 0x40000,
         'write' : 0x80000,
         'approve' : 0x100000
         }),
        ('finance', {
         'read' : 0x200000,
         'write' : 0x400000,
         'approve' : 0x800000
         }),
        ('administer', 0xffffffff)
    ]

    MODULE_PERMISSION_DICT = dict(MODULE_PERMISSION_LIST)

    @staticmethod
    def get_modules(permissions):
        modules = []
        for module_perm in Permission.MODULE_PERMISSION_LIST:
            if module_perm[0] == 'administer':
                if (module_perm[1] & permissions == module_perm[1]):
                    modules.append(module_perm[0])
            elif ((module_perm[1]['read'] & permissions) == module_perm[1]['read']):
                modules.append(module_perm[0])
        return modules
    
    @staticmethod
    def to_json():
        return Permission.MODULE_PERMISSION_LIST
        return {
            u'首营设备':  {u'创建申请' : 0x01, u'审批&删除' : 0x03},
            u'首营企业': {u'创建申请': 0x04, u'审批&删除': 0x0c},
            u'采购订单': {u'创建申请': 0x10, u'审批&删除': 0x30},
            u'销售订单': {u'创建申请': 0x40, u'审批&删除': 0xc0},
            u'仓库管理': {u'创建申请': 0x100, u'审批&删除': 0x300},
            u'维修管理': {u'创建申请': 0x400, u'审批&删除': 0xc00},
            u'物流管理': {u'创建申请': 0x1000, u'审批&删除': 0x3000},
            u'财务管理': {u'创建申请': 0x4000, u'审批&删除': 0xc000}
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    permission = db.Column(db.BigInteger, default=0)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        if username == current_app.config['FLASKY_ADMIN']:
            self.permission = Permission.MODULE_PERMISSION_DICT['administer']
        

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def to_json(self):
        user_json = {'id' : self.id,
            'email' : self.email,
            'username' : self.username,
            'module' : Permission.get_modules(self.permission)
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
        return (self.permission & permissions) == permissions

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

    admin = User(current_app.config['FLASKY_ADMIN'], current_app.config['FLASKY_ADMIN'], current_app.config['FLASKY_ADMIN_PASSWORD'])
    db.session.add(admin)
    db.session.commit()
