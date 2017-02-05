var Mock = require('mockjs')

function adjustTitle(title){
    title['attr0'].modifiable = false
    //title['attr4'].options = ['设备', '试剂', '耗材']
}
var basicInfoList = ['操作编号(系统自分配)', '操作人', '操作表单', '操作详情', '备注']

var titleList = basicInfoList

module.exports = require('./utils').defaultGenerator(titleList, adjustTitle)
