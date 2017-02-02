var Mock = require('mockjs')
Mock.Random.cparagraph(2, 5)
function getMapFromArray(li){
    console.log('li:', li.length, li)
    var counter = 0
    var ret = {}
    for (item in li){
        var name = 'attr' + counter.toString()
        ret[name] = {
            name : li[item],
            modifiable : true,
            options : [],
        }
        console.log(counter, name, li[item])
        counter++
    }
    return ret
}
function getContentBasicSlot(title){
    var counter = 0
    var ret = {}
    for (var key in title){
        if (counter == 0){
            ret[key + '|+1'] = 1
        }else if (title[key].options && title[key].options.length > 0){
            ret[key + '|1'] = title[key].options
        }else{
            ret[key] = '@cword(2,5)'
        }
        counter++
    }
    return ret
}
function adjustTitle(title){
    title['attr0'].modifiable = false
    title['attr3'].options = ['设备', '试剂', '耗材']
}
function getContent(title){
    var content = getContentBasicSlot(title)
    return content
}
function getTitle(){
    var basicInfoList = ['产品编号(系统自分配)', '产品信息', '产品简称', '产品分类(设备/试剂/耗材等)', '规格', '型号', '品牌', '厂家', '单位']
    var relatedInfoList = ['资质文件', '产品类型（如3类6840）', '注册证号有效期（第一类医疗器械备案凭证、二三类医疗器械注册证）', '授权书', '授权书有效期']
    var approveCharacter = '质量部长质量负责人'
    
    //console.log('basic:', basicInfoList.length, basicInfoList)
    //console.log('related:', relatedInfoList.length, relatedInfoList)

    var titleList = basicInfoList.concat(relatedInfoList)
    //console.log('titleList:', titleList.length, titleList)
    var title = getMapFromArray(titleList)
    adjustTitle(title)
    return title
}
function mockEquipment(){
    var title = getTitle()
    console.log('title:', title)

    //var len = titleList.length
    
    Mock.Random.cparagraph(2, 5)
    //console.log('cpara test', Mock.mock('@cword(5)'))

    var content = getContent(title)
    console.log(content)

    //var listUnit2 = { 'id|+1': 1 }
    var data = Mock.mock({
        title,
        'content|1-20': [
            content
        ],
        preference : []
    })
    console.log(data)
    return data
}
function getResponse(req){
    return mockEquipment()
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
