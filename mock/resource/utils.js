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
            ret[title[key] + '|+1'] = 1
        //}else if (title[key].options && title[key].options.length > 0){
        //    ret[key + '|1'] = title[key].options
        }else{
            ret[title[key]] = '@cword(2,5)'
        }
        counter++
    }
    return ret
}



function defaultAdjustTitle(title){
    title['attr0'].modifiable = false
}
function getContent(title){
    var utils = require('./utils')
    var content = utils.getContentBasicSlot(title)
    return content
}
function getTitle(titleList, cb){
    var utils = require('./utils')
    //console.log('utils', utils)
    var title = utils.getMapFromArray(titleList)
    //adjustTitle(title)
    cb(title)
    return title
}

function getResponse(columnsList, cb){
    var title = getTitle(columnsList, cb)
    //Mock.Random.cparagraph(2, 5)
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

function defaultGenerator(columsList, cb){
    cb = cb || defaultAdjustTitle
    return {
        get : function(){
            return getResponse(columsList, cb)
        },
        post : postResponse,
        put : putResponse,
        delete : deleteResponse,
    }
}
module.exports = {
    getMapFromArray,
    getContentBasicSlot,
    defaultGenerator,
}
