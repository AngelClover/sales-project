var Mock = require('mockjs')

function adjustTitle(title){
    title['attr0'].modifiable = false
    //title['attr4'].options = ['设备', '试剂', '耗材']
}
var basicInfoList = ['物流单号(系统自分配)', '待送设备名称', '送货地址', '设备类型(设备/试剂/耗材等)', '完成状态']
var approveCharacter = '物流工程师'

var titleList = basicInfoList

module.exports = require('./utils').defaultGenerator(titleList, adjustTitle)
