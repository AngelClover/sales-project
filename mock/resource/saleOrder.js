var Mock = require('mockjs')
var utils = require('./utils')

var titleList = ['合同编号（系统自动分配）', '签订日期', '供应商名称、地址、电话', '结算公司', '到货时间', '收货地点', '付款方式', '保修期限', '发票类型', '售后服务承诺', '保修期限', '产品名称', '规格', '型号', '单位', '单价', '数量', '总价', '生产厂商', '产品配置单']
    
module.exports = utils.defaultGenerator(titleList)
/*
{
    get : getResponse,
    post : postResponse,
    put : putResponse,
    delete : deleteResponse,
}
*/
