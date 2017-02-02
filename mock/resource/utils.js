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
}
function getContent(title){
    var utils = require('./utils')
    var content = utils.getContentBasicSlot(title)
    return content
}
function getTitle(titleList){
    var utils = require('./utils')
    //console.log('utils', utils)
    var title = utils.getMapFromArray(titleList)
    adjustTitle(title)
    return title
}

function getResponse(columnsList){
    var title = getTitle(columnsList)
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

function defaultGenerator(columsList){
    return {
        get : function(){
            return getResponse(columsList)
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
