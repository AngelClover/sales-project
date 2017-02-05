var Mock = require('mockjs')

function adjustTitle(title){
    title['attr0'].modifiable = false
    //title['attr4'].options = ['设备', '试剂', '耗材']
}
var basicInfoList = ['仓库信息编号(系统自分配)', '设备名称', '在库数字', '简称', '设备类型(设备/试剂/耗材等)']
var approveCharacter = '仓库管理'

var titleList = basicInfoList

module.exports = require('./utils').defaultGenerator(titleList, adjustTitle)
