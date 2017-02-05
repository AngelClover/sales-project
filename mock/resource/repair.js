var Mock = require('mockjs')

function adjustTitle(title){
    title['attr0'].modifiable = false
    //title['attr4'].options = ['设备', '试剂', '耗材']
}
var basicInfoList = ['维修单号(系统自分配)', '待维修设备名称', '维修地址', '设备类型(设备/试剂/耗材等)', '完成状态']
var approveCharacter = '维修工程师'

var titleList = basicInfoList

module.exports = require('./utils').defaultGenerator(titleList, adjustTitle)
