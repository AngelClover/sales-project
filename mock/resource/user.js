var Mock = require('mockjs')

Mock.Random.cparagraph(2, 5)
userAttr = ['id', 'name', 'nickname']

function getOneUser(){
     return {
        'id|1' : 1,
        'name|1' : '@word(2,5)',
        'nickname|1' : '@cword(2,5)' 
    }
}


module.exports = {
    get : function(){
        var data = Mock.mock(getOneUser())
        console.log(data)
        return {
            user: data
        }
    }
}
