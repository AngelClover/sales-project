var Mock = require('mockjs')

function adjustTitle(title){
    title['attr0'].modifiable = false
    title['attr3'].options = ['设备', '试剂', '耗材']
}
function getContent(title){
    var utils = require('./utils')
    var content = utils.getContentBasicSlot(title)
    return content
}
function getTitle(){
    var basicInfoList = ['产品编号(系统自分配)', '产品信息', '产品简称', '产品分类(设备/试剂/耗材等)', '规格', '型号', '品牌', '厂家', '单位']
    var relatedInfoList = ['资质文件', '产品类型（如3类6840）', '注册证号有效期（第一类医疗器械备案凭证、二三类医疗器械注册证）', '授权书', '授权书有效期']
    var approveCharacter = '质量部长质量负责人'
    
    var titleList = basicInfoList.concat(relatedInfoList)
    var utils = require('./utils')
    var title = utils.getMapFromArray(titleList)
    adjustTitle(title)
    return title
}
function mockEquipment(){
    var title = getTitle()
    var content = getContent(title)
    var data = Mock.mock({
        title,
        'content|1-20': [
            content
        ],
        preference : []
    })
    return data
}
function getResponse(req){
    return mockEquipment()
}

function postResponse(req){
    return {
        query : req.query,
        params : req.params,
    }
}
function putResponse(req){
    return {
        originInput : "nothing"
    }
}
function deleteResponse(req){
    return {
        originInput : "nothing"
    }
}


module.exports = {
    get : getResponse,
    post : postResponse,
    put : putResponse,
    delete : deleteResponse,
}
