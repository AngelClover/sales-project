var Mock = require('mockjs')

function adjustTitle(title){
    title['attr0'].modifiable = false
    title['attr4'].options = ['设备', '试剂', '耗材']
}
function getContent(title){
    var utils = require('./utils')
    var content = utils.getContentBasicSlot(title)
    return content
}
function getTitle(){
    var basicInfoList = ['供应商编号(系统自分配)', '供应商名称', '注册资金', '简称', '供应商类型(设备/试剂/耗材等)', '曾用名', '法定代表人', '住所', '成立日期']
    var contactList = ['联系人', '手机', '电话', '传真', '邮箱', '地址']
    var relatedInfoList = ['资质文件', '营业执照注册号', '营业期限', '组织机构代码证号码', '有效期',  '开户许可证', '第一类医疗器械生产企业备案 证书/《医疗器械生产许可证》（2类3类，到期提醒）', '医疗器械经营企业备案证书（2类）/医疗器械经营许可证（3类，号码，许可期限，到期提醒）', '质量保证书',  '税务登记证', '随货同行单样式和印章印模样式']
    var bankInfoList = ['税号', '是否一般纳税人', '开户行', '账户']
    var approveCharacter = '质量部长质量负责人'
    
    //console.log('basic:', basicInfoList.length, basicInfoList)
    //console.log('related:', relatedInfoList.length, relatedInfoList)

    var titleList = basicInfoList.concat(contactList).concat(relatedInfoList).concat(bankInfoList)
    //console.log('titleList:', titleList.length, titleList)
    var utils = require('./utils')
    //console.log('utils', utils)
    var title = utils.getMapFromArray(titleList)
    adjustTitle(title)
    return title
}

function mockCompany(){
    var title = getTitle()
    Mock.Random.cparagraph(2, 5)
    var content = getContent(title)

    var data = Mock.mock({
        title,
        'content|1-20': [
            content
        ],
        preference : []
    })
    //console.log(data)
    return data
}
function getResponse(req){
    return mockCompany()
}

function postResponse(req){
    //console.log('post req', req)
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
