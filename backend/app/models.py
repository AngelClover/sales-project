#!/usr/bin/env python
#-*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db
import json
import datetime
import os

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
    accessory = db.Column(db.String(1024))#json
#create_person = db.relationship('User')
    create_user = db.Column(db.Integer)
    approve_user = db.Column(db.Integer)

    def __init__(self, info, abbr, type, spec, model, producer, accessory, create_user, approve_user):
        self.info = info
        self.abbr = abbr
        self.type = type
        self.spec = spec
        self.model = model
        self.producer = producer
        self.state = 1
        self.accessory = accessory
        self.create_user = create_user
        self.approve_user = approve_user
    
    def to_json(self):
        create_user_name = self.create_user
        if self.create_user is not None:
            cu = User.query.get(self.create_user)
            if cu is not None:
                create_user_name = cu.nickname or cu.username
        approve_user_name = self.approve_user
        if self.approve_user is not None:
            au = User.query.get(self.approve_user)
            if au is not None:
                approve_user_name = au.nickname or au.username

        equip_json = { 'id' : self.id,
#'info' : self.info,
#            'abbr' : self.abbr,
#            'type' : self.type,
#            'spec' : self.spec,
#            'model' : self.model,
#            'producer' : self.producer,
            'state' : (u'审核通过' if self.state == 0 else u'待审核'),
            'create_user' : create_user_name,
            'approve_user' : approve_user_name
        } 
        if self.accessory:
            obj = json.loads(self.accessory)
            for item in obj:
                equip_json[item] = obj[item]
                
        return equip_json
    
    def get_name(self):
        ret = ""
        if self.accessory is not None:
            x = json.loads(self.accessory)
            for key,value in x.items():
                if key == u'简称' and value is not None and len(value) > 0:
                    ret = value
                if key == u'名称' and value is not None and len(value) > 0 and ret == "":
                    ret = value
        if self.info is not None and len(self.info) > 0 and ret == "":
            ret = self.info

        return ret
    
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
        return [
        ('id', u'产品编号', 'immutable'),
        ('名称', '名称'),
        ('简称', '简称'),
        ('医疗器械标准码', '医疗器械标准码'),
        ('医疗器械分类', '医疗器械分类'),
        ('英文名称', '英文名称'),
        ('规格', '规格'),
        ('型号', '型号'),
        ('单位', '单位'),
        ('产品类别', '产品类别', 'option', ['设备', '试剂', '耗材']),
        ('厂商', '厂商'),
        ('产品注册证到期日期', '产品注册证到期日期'),
        ('审核材料附件', '审核材料附件'),
        ('是否冷链', '是否冷链'),
        ('create_user', '创建人'),
        ('approve_user', '审核人'),
#('流程编号', '流程编号'),
        ]
#return [('id', u'产品编号'),
#            ('info', u'产品信息'),
#            ('abbr' , u'产品简称'),
#            ('type', u'产品分类', 'option', [u'设备', u'试剂', u'耗材']),
#            ('spec' , u'产品规格'),
#            ('model', u'产品型号'),
#            ('producer', u'厂家'),
#            ('state', u'当前状态'),
#        ]

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
    accessory = db.Column(db.String(1024)) #json
    create_user = db.Column(db.Integer)
    approve_user = db.Column(db.Integer)

    def __init__(self, name, register_capital, abbr, type, ever_name, legal_representor, location, establish_date, accessory, create_user, approve_user):
        self.name = name
        self.register_capital = register_capital
        self.abbr = abbr
        self.type = type
        self.ever_name = ever_name
        self.legal_representor = legal_representor
        self.location = location
        self.establish_date = establish_date
        self.accessory = accessory
        self.create_user = create_user
        self.approve_user = approve_user
    
    def to_json(self):
        create_user_name = self.create_user
        if self.create_user is not None:
            cu = User.query.get(self.create_user)
            if cu is not None:
                create_user_name = cu.nickname or cu.username
        approve_user_name = self.approve_user
        if self.approve_user is not None:
            au = User.query.get(self.approve_user)
            if au is not None:
                approve_user_name = au.nickname or au.username

        enterprise_json = { 'id' : self.id,
#'name' : self.name,
#'register_capital' : self.register_capital,
#'abbr' : self.abbr,
#'type' : self.type,
#'ever_name' : self.ever_name,
#'legal_representor' : self.legal_representor,
#'location' : self.location,
#'establish_date' : self.establish_date,
            'create_user' : create_user_name,
            'approve_user' : approve_user_name,
        }
        if self.accessory:
            obj = json.loads(self.accessory)
            for item in obj:
                enterprise_json[item] = obj[item]
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
        return [
            ('id', '首营企业编号', 'immutable'),
            ('简称', '简称'),
            ('名称', '名称'),
            ('归属地', '归属地'),
            ('状态', '状态'),
            ('医疗器械经营范围', '医疗器械经营范围'),
            ('分类', '分类'),
            ('联系人', '联系人'),
            ('电话', '电话'),
            ('地址', '地址'),
            ('经营范围', '经营范围'),
            ('手机', '手机'),
            ('传真', '传真'),
            ('币种', '币种'),
            ('承运方式', '承运方式'),
            ('结算方式', '结算方式'),
            ('邮箱', '邮箱'),
            ('网址', '网址'),
            ('备注', '备注'),
            ('维护人员', '维护人员'),
            ('结算单位', '结算单位'),
            ('create_user', '创建人'),
            ('approve_user', '审核人'),
        ]
#return [('id', u'首营企业编号(系统自动分配)'),
#('name', u'供应商名称'),
#('register_capital', u'注册资金'),
#('abbr', u'简称'),
#('type', u'供应商类型(设备/试剂/耗材等)', 'option', [u'设备', u'试剂', u'耗材']),
#('ever_name', u'曾用名'),
#('legal_representor', u'法人代表'),
#('location', u'住所'),
#('establish_date', u'成立日期')
#]

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
    contract = db.Column(db.String(256))#合同文件名
    create_user = db.Column(db.Integer)
    approve_user = db.Column(db.Integer)

    @staticmethod
    def get_ordered_headers():
        return [('id', u'合同编号', 'immutable'),
        ('sign_date', u'签订日期'),
        ('provider_info', u'供应商名称、地址、电话'),
        ('billing_company', u'结算公司'),
        ('arrive_date', u'到货时间'),
        ('get_location', u'收货地点'),
        ('pay_mode', u'付款方式'),
        ('invoice_type', u'发票类型'),
        ('postage_account', u'运费承担方'),
        ('state', u'当前状态', 'immutable'),
        ('total_stored', u'入库情况（未/部分/完全)', 'immutable'),
        ('contract', u'合同文件'),
        ('create_user', '创建人'),
        ('approve_user', '审核人'),
        (),
        ('equipment_id', '产品编号', 'immutable'),
        ('warranty_period', u'保修期限'),
        ('install_require', u'安装调试要求'),
        ('product_name', u'产品名称', 'immutable'),
        ('spec', u'规格', 'immutable'),
        ('model', u'型号', 'immutable'),
        ('measurement_unit', u'单位', 'immutable'),
        ('unit_price', u'单价'),
        ('quantity', u'数量'),
        ('total_price', u'总价'),
        ('producer', u'生产厂商', 'immutable'),
        ('product_configure', u'产品配置单'),
        ('received', u'是否接收', 'immutable'),
        ('received_user', u'接收人', 'immutable'),
        ('inspected', u'是否检验', 'immutable'),
        ('inspected_user', u'检验人', 'immutable'),
        ('stored', u'是否入库', 'immutable'),
        ('stored_user', u'入库人', 'immutable'),
        ]

    def to_json(self):
        total_price = 0
        equipments = []
#print "IV.I", self.purchase_equipments
        for e in self.purchase_equipments:
            total_price += e.total_price
            ru = e.received_user
            if ru is not None:
                ru = User.query.get(ru)
                if ru is not None:
                    ru = ru.nickname or ru.username
            iu = e.inspected_user
            if iu is not None:
                iu = User.query.get(iu)
                if iu is not None:
                    iu = iu.nickname or iu.username
            su = e.stored_user
            if su is not None:
                su = User.query.get(su)
                if su is not None:
                    su = su.nickname or su.username
            equipments.append({
                    'equipment_id' : e.equipment.id,
                    'warranty_period' : e.warranty_period,
                    'install_require' : e.install_require,
                    'measurement_unit' : e.measurement_unit,
                    'unit_price' : e.unit_price,
                    'quantity' : e.quantity,
                    'total_price' : e.total_price,
                    'producer' : e.equipment.producer,
                    'product_configure' : e.product_configure,
                    'product_name' : e.equipment.get_name(),# or json.loads(e.equipment.accessory)['名称'],
                    'spec' : e.equipment.spec,
                    'model' : e.equipment.model,
                    'received' : e.received,
                    'received_user' : ru,
                    'inspected' : e.inspected,
                    'inspected_user' : iu,
                    'stored' : e.stored,
                    'stored_user' : su,
                    })
#print "IV.II"
#print self, equipments, total_price
#print "Angel ", self.sign_date , type(self.sign_date), type(self.arrive_date)
#print "Angel ", len(self.sign_date), len(self.arrive_date)
#print self.sign_date , len(self.sign_date), len(self.sign_date.strip(' '))
#self.sign_date = self.sign_date.strip(' ')
#print "Angel ", len(self.sign_date), len(self.arrive_date)
#sds =  datetime.datetime.strptime(self.sign_date, "%Y-%m-%d")
#sds = self.sign_date.strftime('%Y-%m-%d')
#sds =  self.sign_date
#print self.arrive_date
#ads =  datetime.datetime.strptime(self.arrive_date.strip(' '), '%Y-%m-%d %H:%M:%S')
#ads = self.arrive_date.strftime('%Y-%m-%d %H:%M:%S')
#ads =  self.arrive_date
#print self.id, self.provider_info, self.billing_company, self.get_location, self.pay_mode, self.invoice_type, self.postage_account 

#print "IV.IIUUU"

        create_user_name = self.create_user
        if self.create_user is not None:
            cu = User.query.get(self.create_user)
            if cu is not None:
                create_user_name = cu.nickname or cu.username
        approve_user_name = self.approve_user
        if self.approve_user is not None:
            au = User.query.get(self.approve_user)
            if au is not None:
                approve_user_name = au.nickname or au.username

        equip_json = {'id' : self.id,
            'sign_date' : self.sign_date.strftime('%Y-%m-%d'),
            'provider_info' : self.provider_info,
            'billing_company' : self.billing_company,
            'arrive_date' : self.arrive_date.strftime('%Y-%m-%d %H:%M:%S'),
            'get_location' : self.get_location,
            'pay_mode' : self.pay_mode,
            'invoice_type' : self.invoice_type,
            'postage_account' : self.postage_account,
            'total_price' : total_price,
            'state' : (u'审核通过' if self.state == 0 else (u'待审核' if self.state == 1 else (u'待入库' if self.state == -2 else (u'入库中' if self.state == -3 else (u'已入库' if self.state == -4 else u'状态异常'))))),
            'equipments' : equipments,
            'total_stored' : u'未入库' if self.total_stored == 0 else (u'部分入库' if self.total_stored == 1 else u'完全入库'),
            'contract' : self.contract,
            'create_user' : create_user_name,
            'approve_user' : approve_user_name
        }
#print "IV.III"
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
    stored_user = db.Column(db.Integer)
    received = db.Column(db.Integer, default=0)
    received_user = db.Column(db.Integer)
    inspected = db.Column(db.Integer, default=0)
    inspected_user = db.Column(db.Integer)
    
    
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
    #state = db.Column(db.Integer, default=1)#状态， 0:正常，1:创建，待审核
    state = db.Column(db.Integer, default=1)#状态，1:创建，待审核, 0:已审批, -1:(合同生成) -2:(待出库 ==> 已审批) -3:出库中(partial) -4：已出库
    total_outstore = db.Column(db.Integer, default=0)#出库状态，0:未出库; 1:部分出库; 2:完全出库
    contract = db.Column(db.String(256))#合同文件
    create_user = db.Column(db.Integer)
    approve_user = db.Column(db.Integer)

    @staticmethod
    def get_ordered_headers():
        return [('id', u'销售订单编号', 'immutable'),
        ('sign_date', u'签订日期'),
        ('provider_info', u'客户名称、地址、电话'),
        ('billing_company', u'结算公司'),
        ('arrive_date', u'到货时间'),
        ('get_location', u'收货地点'),
        ('pay_mode', u'付款方式'),
        ('invoice_type', u'发票类型'),
        ('state', u'订单状态', 'immutable'),
        ('total_outstore', u'出库情况(未/部分/完全', 'immutable'),
        ('total_price', u'总价', 'immutable'),
        ('contract', u'合同文件'),
        ('create_user', '创建人'),
        ('approve_user', '审核人'),
        (),
        ('service_commitment', u'售后服务承诺'),
        ('warranty_period', u'保修期限'),
        ('product_name', u'产品名称', 'immutable'),
        ('spec', u'规格', 'immutable'),
        ('model', u'型号', 'immutable'),
        ('measurement_unit', u'单位', 'immutable'),
        ('unit_price', u'单价'),
        ('total_price', u'总价'),
        ('producer', u'生产厂商', 'immutable'),
        ('product_configure', u'产品配置单'),
        ('equipment_id', u'产品编号', 'immutable'),
        ('outstore_quantity', u'已出库数量', 'immutable'),
        ('quantity', u'数量'),
        ('outstore_state', u'出库状态', 'immutable'),
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
                    'product_name' : e.equipment.get_name(), #.info,
                    'spec' : e.equipment.spec,
                    'model' : e.equipment.model,
                    'equipment_id' : e.equipment_id,
                    'outstore_state' : u' 未出库' if e.outstore_state == 0 else (u'部分出库' if e.outstore_state == 1 else (u'全出库' if e.outstore_state == 2 else u'状态异常')),
                    'outstore_quantity' : e.outstore_quantity,
                    })

        create_user_name = self.create_user
        if self.create_user is not None:
            cu = User.query.get(self.create_user)
            if cu is not None:
                create_user_name = cu.nickname or cu.username
        approve_user_name = self.approve_user
        if self.approve_user is not None:
            au = User.query.get(self.approve_user)
            if au is not None:
                approve_user_name = au.nickname or au.username

        equip_json = {'id' : self.id,
            'sign_date' : self.sign_date.strftime('%Y-%m-%d'),
            'provider_info' : self.provider_info,
            'billing_company' : self.billing_company,
            'arrive_date' : self.arrive_date.strftime('%Y-%m-%d %H:%M:%S'),
            'get_location' : self.get_location,
            'pay_mode' : self.pay_mode,
            'invoice_type' : self.invoice_type,
            'total_price' : total_price,
            'state' : (u'审核通过' if self.state == 0 else (u'待审核' if self.state == 1 else (u'合同生成' if self.state == -1 else (u'待出库' if self.state == -2 else (u'出库中' if self.state == -3 else (u'已出库' if self.state == -4 else u'状态异常')))))),
            'total_outstore' : u'未出库' if self.total_outstore == 0  else (u'部分出库' if self.total_outstore == 1 else u'完全出库'),
            'equipments' : equipments,
            'contract' : self.contract,
            'create_user' : create_user_name,
            'approve_user' : approve_user_name
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
    order_num = db.Column(db.Integer)

    def __init__(self):
        self.state = 1

    @staticmethod
    def get_ordered_headers():
        return [('id', u'物流单号(系统自分配)', 'immutable'),
        ('equipment_name', u'待送设备名称', 'immutable'),
        ('delivery_address', u'送货地址'),
        ('equipment_type', u'设备类型(设备/试剂/耗材等)', 'immutable'),
        ('delivery_status', u'完成状态', 'immutable'),
        ('order_num', u'相关销售订单编号')
        ]

    def to_json(self):
        return {
            'id' : self.id,
            'equipment_name' : self.equipment_name,
            'delivery_address' : self.delivery_address,
            'equipment_type' : self.equipment_type,
            'delivery_status' : self.delivery_status,
            'order_num' : self.order_num,
        }

class Repair(db.Model):
    __tablename__ = 'repair'
    
    id = db.Column(db.Integer, primary_key=True)#维修单号(系统自分配)
    equipment_name = db.Column(db.String(256))#待维修设备名称
    repair_address = db.Column(db.String(1024))#维修地址
    equipment_type = db.Column(db.String(64))#设备类型(设备/试剂/耗材等)
    repair_status = db.Column(db.String(64))#完成状态
    state = db.Column(db.Integer, default=1)#当前状态, 0:审核完成, 1:待审核
    order_num = db.Column(db.Integer)

    def __init__(self):
        self.state = 1

    @staticmethod
    def get_ordered_headers():
        return [('id', u'维修单号(系统自分配)', 'immutable'),
        ('equipment_name', u'待维修设备名称', 'immutable'),
        ('repair_address', u'维修地址'),
        ('equipment_type', u'设备类型(设备/试剂/耗材等)', 'immutable'),
        ('repair_status', u'完成状态', 'immutable'),
        ('order_num', u'相关销售订单编号')
        ]

    def to_json(self):
        return {
            'id' : self.id,
            'equipment_name' : self.equipment_name,
            'repair_address' : self.repair_address,
            'equipment_type' : self.equipment_type,
            'repair_status' : self.repair_status,
            'order_num' : self.order_num,
        }

class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)#仓库信息编号(系统自分配)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'))
    store_number = db.Column(db.Integer)#在库数字
    #state = db.Column(db.Integer, default=1)#当前状态, 0:审核完成, 1:待审核
    bad_date = db.Column(db.Date)

    purchase_order = db.relationship(PurchaseOrder, uselist=False, backref="stores")
    equipment = db.relationship(Equipment, uselist=False, backref="stores")

    def __init(self):
        #self.state = 1
        pass

    @staticmethod
    def get_ordered_headers():
        return [('id', u'仓库信息编号(系统自分配)', 'immutable'),
        ('equipment_name', u'设备名称', 'immutable'),
#('abbr', u'简称'),
#('equipment_type', u'设备类型(设备/试剂/耗材等)'),
        ('store_number', u'在库数字'),
        ('bad_date', u'过期日期')
        ]

    def to_json(self):
        return {
            'id' : self.id,
            'equipment_name' : self.equipment.get_name(), #info,
#'abbr' : self.equipment.abbr,
#'equipment_type' : self.equipment.type,
            'store_number' : self.store_number,
            'bad_date' : 'NULL' if self.bad_date is None else self.bad_date.strftime('%Y-%m-%d'),
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
    nickname = db.Column(db.String(64))

    def __init__(self, email, username, password, nickname):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.nickname = nickname
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
            'permission' : Permission.get_permission(self.permission),
            'nickname' : self.nickname,
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

class UploadFile(db.Model):
    __tablename__ = 'upload_files'
    UPLOAD_DIR ="../uploadfiles"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    filename = db.Column(db.String(256))
    displayName = db.Column(db.String(256))#此变量风格用错
    upload_time = db.Column(db.DateTime)

    def __init__(self, userid, filename, displayName, todaytime):
        self.userid = userid
        self.filename = filename
        self.displayName = displayName
        self.upload_time = todaytime

    def to_json(self):
        upload_user_name = self.userid
        if self.userid is not None:
            cu = User.query.get(self.userid)
            if cu is not None:
                upload_user_name = cu.nickname or cu.username
        if upload_user_name == 0:
            upload_user_name = 'AnonymousUser'
        filejson = {'id' : self.id,
            'upload_user' : upload_user_name,
            'filename' : self.target_filename(), 
            'displayName' : self.displayName,
            'upload_time' : self.upload_time.strftime('%Y-%m-%d %H:%M:%S') if self.upload_time is not None else None, }
        return filejson

    def target_filename(self):
        return os.path.join(self.UPLOAD_DIR, self.filename)

    @staticmethod
    def get_ordered_headers():
        return [('id', u'文件编号', 'immutable'),
        ('userid', u'上传用户编号', 'immutable'),
        ('filename', u'文件名', 'immutable'),
        ('displayName', u'原始文件名', 'immutable'),
        ('upload_time', u'上传时间', 'immutable'),
        ]

class AnonymousUser:
    id = 0
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
