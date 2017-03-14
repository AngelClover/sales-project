#!/usr/bin/env python
#-*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db

class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)#产品ID
    info = db.Column(db.String(256))#产品信息
    abbr = db.Column(db.String(256))#产品简称
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
            'state' : (u'审核通过' if self.state == 0 else u'待审核')
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
            'producer' : u'厂家',
            'state' : u'当头状态'
        }
    @staticmethod
    def get_ordered_headers():
        return [('id', u'产品编号'),
            ('info', u'产品信息'),
            ('abbr' , u'产品简称'),
            ('type', u'产品分类', 'option', [u'设备', u'试剂', u'耗材']),
            ('spec' , u'产品规格'),
            ('model', u'产品型号'),
            ('producer', u'厂家'),
            ('state', u'当前状态'),
        ]

class Enterprise(db.Model):
    __tablename__ = 'enterprise'
    id = db.Column(db.Integer, primary_key=True)#首营企业编号
    name = db.Column(db.String(256))#供应商名称
    register_capital = db.Column(db.Integer)#注册资金
    abbr = db.Column(db.String(256))#简称
    type = db.Column(db.String(256))#供应商类型(设备/试剂/耗材等)
    ever_name = db.Column(db.String(256))#曾用名
    legal_representor = db.Column(db.String(256))#法人代表
    location = db.Column(db.String(1024))#住所
    establish_date = db.Column(db.Date)#成立日期

    def __init__(self, name, register_capital, abbr, type, ever_name, legal_representor, location, establish_date):
        self.name = name
        self.register_capital = register_capital
        self.abbr = abbr
        self.type = type
        self.ever_name = ever_name
        self.legal_representor = legal_representor
        self.location = location
        self.establish_date = establish_date
    
    def to_json(self):
        enterprise_json = { 'id' : self.id,
            'name' : self.name,
            'register_capital' : self.register_capital,
            'abbr' : self.abbr,
            'type' : self.type,
            'ever_name' : self.ever_name,
            'legal_representor' : self.legal_representor,
            'location' : self.location,
            'establish_date' : self.establish_date
        }
        return enterprise_json
    
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
    
    @staticmethod
    def get_ordered_headers():
        return [('id', u'首营企业编号(系统自动分配)'),
        ('name', u'供应商名称'),
        ('register_capital', u'注册资金'),
        ('abbr', u'简称'),
        ('type', u'供应商类型(设备/试剂/耗材等)', 'option', [u'设备', u'试剂', u'耗材']),
        ('ever_name', u'曾用名'),
        ('legal_representor', u'法人代表'),
        ('location', u'住所'),
        ('establish_date', u'成立日期')
        ]

class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.Integer, primary_key=True)#合同编号
    sign_date = db.Column(db.Date)#签订日期
    provider_info = db.Column(db.String(256))#供应商名称、地址、电话
    billing_company = db.Column(db.String(256))#结算公司
    arrive_date = db.Column(db.DateTime)#到货日期
    get_location = db.Column(db.String(1024))#收货地点
    pay_mode = db.Column(db.String(256))#付款方式
    invoice_type = db.Column(db.String(256))#发票类型
    postage_account = db.Column(db.String(256))#运费承担方
    state = db.Column(db.Integer, default=1)#状态，1:创建，待审核, 0:已审批, -1:买货中(占位) -2:待入库 -3:入库中(partial) -4：已入库
    total_stored = db.Column(db.Integer, default=0)#是否完全入库, 0:未入库；1：部分入库；2:完全入库

    @staticmethod
    def get_ordered_headers():
        return [('id', u'合同编号（系统自动分配）'),
        ('sign_date', u'签订日期'),
        ('provider_info', u'供应商名称、地址、电话'),
        ('billing_company', u'结算公司'),
        ('arrive_date', u'到货时间'),
        ('get_location', u'收货地点'),
        ('pay_mode', u'付款方式'),
        ('invoice_type', u'发票类型'),
        ('postage_account', u'运费承担方'),
        ('state', u'当前状态'),
        ('total_stored', u'入库情况（未/部分/完全)'),
        (),
        ('warranty_period', u'保修期限'),
        ('install_require', u'安装调试要求'),
        ('product_name', u'产品名称'),
        ('spec', u'规格'),
        ('model', u'型号'),
        ('measurement_unit', u'单位'),
        ('unit_price', u'单价'),
        ('quantity', u'数量'),
        ('total_price', u'总价'),
        ('producer', u'生产厂商'),
        ('product_configure', u'产品配置单'),
        ('stored', u'是否入库(0/1)')
        ]

    def to_json(self):
        total_price = 0
        equipments = []
        for e in self.purchase_equipments:
            total_price += e.total_price
            equipments.append({
                    'id' : e.equipment.id,
                    'warranty_period' : e.warranty_period,
                    'install_require' : e.install_require,
                    'measurement_unit' : e.measurement_unit,
                    'unit_price' : e.unit_price,
                    'quantity' : e.quantity,
                    'total_price' : e.total_price,
                    'producer' : e.equipment.producer,
                    'product_configure' : e.product_configure,
                    'product_name' : e.equipment.info,
                    'spec' : e.equipment.spec,
                    'model' : e.equipment.model,
                    'stored' : e.stored
                    })

        equip_json = {'id' : self.id,
            'sign_date' : self.sign_date.strftime('%Y-%m-%d'),
            'provider_info' : self.provider_info,
            'billing_company' : self.billing_company,
            'arrive_date' : self.arrive_date.strftime('%Y-%m-%d %H%M%S'),
            'get_location' : self.get_location,
            'pay_mode' : self.pay_mode,
            'invoice_type' : self.invoice_type,
            'postage_account' : self.postage_account,
            'total_price' : total_price,
            'state' : (u'审核通过' if self.state == 0 else (u'待审核' if self.state == 1 else (u'待入库' if self.state == -2 else (u'入库中' if self.state == -3 else (u'已入库' if self.state == -4 else u'状态异常'))))),
            'equipments' : equipments,
            'total_stored' : u'未入库' if self.total_stored == 0 else (u'部分入库' if self.total_stored == 1 else u'完全入库')
        }
        return equip_json

#associate PurchaseOrder and Equipment
class PurchaseEquipment(db.Model):
    __tablename__ = 'purchase_equipment'
    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    #extra info
    warranty_period = db.Column(db.String(256))#保修期限
    install_require = db.Column(db.String(256))#安装调试要求
    measurement_unit = db.Column(db.String(256))#单位
    unit_price = db.Column(db.Float)#单价
    quantity = db.Column(db.Integer)#数量
    total_price = db.Column(db.Float)#总价
    product_configure = db.Column(db.Text)#产品配置单
    stored = db.Column(db.Integer, default=0)#0:未入库，1:已入库
    
    purchase_order = db.relationship(PurchaseOrder, uselist=False, backref="purchase_equipments")
    equipment = db.relationship(Equipment, uselist=False, backref="purchase_order")


class SaleOrder(db.Model):
    __tablename__ = 'sale_order'
    id = db.Column(db.Integer, primary_key=True)#合同编号
    sign_date = db.Column(db.Date)#签证日期
    provider_info = db.Column(db.String(256))#供应商名称、地址、电话
    billing_company = db.Column(db.String(256))#结算公司
    arrive_date = db.Column(db.DateTime)#到货日期
    get_location = db.Column(db.String(1024))#收货地点
    pay_mode = db.Column(db.String(256))#付款方式
    invoice_type = db.Column(db.String(256))#发票类型
    state = db.Column(db.Integer, default=1)#状态， 0:正常，1:创建，待审核
    total_outstore = db.Column(db.Integer, default=0)#出库状态，0:未出库; 1:部分出库; 2:完全出库

    @staticmethod
    def get_ordered_headers():
        return [('id', u'合同编号（系统自动分配）'),
        ('sign_date', u'签订日期'),
        ('provider_info', u'供应商名称、地址、电话'),
        ('billing_company', u'结算公司'),
        ('arrive_date', u'到货时间'),
        ('get_location', u'收货地点'),
        ('pay_mode', u'付款方式'),
        ('invoice_type', u'发票类型'),
        ('total_outstore', u'出库情况(未/部分/完全'),
        (),
        ('service_commitment', u'售后服务承诺'),
        ('warranty_period', u'保修期限'),
        ('product_name', u'产品名称'),
        ('spec', u'规格'),
        ('model', u'型号'),
        ('measurement_unit', u'单位'),
        ('unit_price', u'单价'),
        ('quantity', u'数量'),
        ('total_price', u'总价'),
        ('producer', u'生产厂商'),
        ('product_configure', u'产品配置单')
        ]

    def to_json(self):
        total_price = 0
        equipments = []
        for e in self.sale_equipments:
            total_price += e.total_price
            equipments.append({
                    'id' : e.id,
                    'service_commitment' : e.service_commitment,
                    'warranty_period' : e.warranty_period,
                    'measurement_unit' : e.measurement_unit,
                    'unit_price' : e.unit_price,
                    'quantity' : e.quantity,
                    'total_price' : e.total_price,
                    'producer' : e.equipment.producer,
                    'product_configure' : e.product_configure,
                    'product_name' : e.equipment.info,
                    'spec' : e.equipment.spec,
                    'model' : e.equipment.model
                    })

        equip_json = {'id' : self.id,
            'sign_date' : self.sign_date.strftime('%Y-%m-%d'),
            'provider_info' : self.provider_info,
            'billing_company' : self.billing_company,
            'arrive_date' : self.arrive_date.strftime('%Y-%m-%d %H%M%S'),
            'get_location' : self.get_location,
            'pay_mode' : self.pay_mode,
            'invoice_type' : self.invoice_type,
            'total_price' : total_price,
            'state' : (u'审核通过' if self.state == 0 else u'待审核'),
            'total_outstore' : u'未出库' if self.total_outstore == 0  else (u'部分出库' if self.total_outstore == 1 else u'完全出库'),
            'equipments' : equipments
        }
        return equip_json

#associate sale_order and equipment
class SaleEquipment(db.Model):
    __tablename__ = 'sale_equipment'
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale_order.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    #extra info
    service_commitment = db.Column(db.String(1024))
    warranty_period = db.Column(db.String(256))#保修期限
    measurement_unit = db.Column(db.String(256))#单位
    unit_price = db.Column(db.Float)#单价
    quantity = db.Column(db.Integer)#数量
    total_price = db.Column(db.Float)#总价
    product_configure = db.Column(db.Text)#产品配置单
    outstore_quantity = db.Column(db.Integer, default=0)
    outstore_state = db.Column(db.Integer, default=0)#出库状态：0:完全未出库，1:部分出库；2：完全出库

    sale_order = db.relationship(SaleOrder, uselist=False, backref='sale_equipments')
    equipment = db.relationship(Equipment, uselist=False, backref='sale_order')

class Logistic(db.Model):
    __tablename__ = 'logistic'
    id = db.Column(db.Integer, primary_key=True)#物流单号(系统自分配)
    equipment_name = db.Column(db.String(256))#待送设备名称
    delivery_address = db.Column(db.String(1024))#送货地址
    equipment_type = db.Column(db.String(64))#设备类型(设备/试剂/耗材等)
    delivery_status = db.Column(db.String(64))#完成状态
    state = db.Column(db.Integer, default=1) #当前状态 0:审批通过，1:待审批

    def __init__(self):
        self.state = 1

    @staticmethod
    def get_ordered_headers():
        return [('id', u'物流单号(系统自分配)'),
        ('equipment_name', u'待送设备名称'),
        ('delivery_address', u'送货地址'),
        ('equipment_type', u'设备类型(设备/试剂/耗材等)'),
        ('delivery_status', u'完成状态')
        ]

    def to_json(self):
        return {
            'id' : self.id,
            'equipment_name' : self.equipment_name,
            'delivery_address' : self.delivery_address,
            'equipment_type' : self.equipment_type,
            'delivery_status' : self.delivery_status
        }

class Repair(db.Model):
    __tablename__ = 'repair'
    
    id = db.Column(db.Integer, primary_key=True)#维修单号(系统自分配)
    equipment_name = db.Column(db.String(256))#待维修设备名称
    repair_address = db.Column(db.String(1024))#维修地址
    equipment_type = db.Column(db.String(64))#设备类型(设备/试剂/耗材等)
    repair_status = db.Column(db.String(64))#完成状态
    state = db.Column(db.Integer, default=1)#当前状态, 0:审核完成, 1:待审核

    def __init__(self):
        self.state = 1

    @staticmethod
    def get_ordered_headers():
        return [('id', u'维修单号(系统自分配)'),
        ('equipment_name', u'待维修设备名称'),
        ('repair_address', u'维修地址'),
        ('equipment_type', u'设备类型(设备/试剂/耗材等)'),
        ('repair_status', u'完成状态')
        ]

    def to_json(self):
        return {
            'id' : self.id,
            'equipment_name' : self.equipment_name,
            'repair_address' : self.repair_address,
            'equipment_type' : self.equipment_type,
            'repair_status' : self.repair_status
        }

class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)#仓库信息编号(系统自分配)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'))
    store_number = db.Column(db.Integer)#在库数字
    #state = db.Column(db.Integer, default=1)#当前状态, 0:审核完成, 1:待审核

    purchase_order = db.relationship(PurchaseOrder, uselist=False, backref="stores")
    equipment = db.relationship(Equipment, uselist=False, backref="stores")

    def __init(self):
        #self.state = 1
        pass

    @staticmethod
    def get_ordered_headers():
        return [('id', u'仓库信息编号(系统自分配)'),
        ('equipment_name', u'设备名称'),
        ('abbr', u'简称'),
        ('equipment_type', u'设备类型(设备/试剂/耗材等)'),
        ('store_number', u'在库数字')
        ]

    def to_json(self):
        return {
            'id' : self.id,
            'equipment_name' : self.equipment.info,
            'abbr' : self.equipment.abbr,
            'equipment_type' : self.equipment.type,
            'store_number' : self.store_number
        }


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
    def get_permission(permissions):
        permission_json = {}
        for module_perm in Permission.MODULE_PERMISSION_LIST:
            if module_perm[0] == 'administer':
                continue
            permission_json[module_perm[0]] = {}
            for name, value in module_perm[1].iteritems():
                if (value & permissions) == value:
                    permission_json[module_perm[0]][name] = True
                else:
                    permission_json[module_perm[0]][name] = False
        return permission_json

    @staticmethod
    def to_json():
        return Permission.MODULE_PERMISSION_LIST
    
    
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
            'module' : Permission.get_modules(self.permission),
            'permission' : Permission.get_permission(self.permission)
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
    test_equipment_x = Equipment(u'xx试剂', u'xx', u'试剂', u'100ml', u'轻量', u'北京污业公司')
    test_equipment_y = Equipment(u'yy试剂', u'yy', u'试剂', u'100ml', u'轻量', u'北京伟业公司')
    db.session.add(test_equipment_x)
    db.session.add(test_equipment_y)
    db.session.add(admin)
    db.session.commit()
