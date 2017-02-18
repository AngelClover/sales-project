var Mock = require('mockjs')

Mock.Random.cparagraph(2, 5)
userAttr = ['id', 'name', 'nickname']

modelList = ['home', 'buy', 'sale', 'logistic', 'repair', 'source', 'sink', 'storehouse']

function getOneUser(){
     return {
        'id|1' : 1,
        'username|1' : '@word(2,5)',
        'email|1' : '@word(2,6)',
        //'nickname|1' : '@cword(2,5)' ,
        'modelList' : modelList
    }
}


module.exports = {
    get : function(){
        var data = Mock.mock(getOneUser())
        console.log(data)
        return {
            user: data
        }
    },
    get_token : function(){
        var data = Mock.mock({
            'user' : {
                'email|1' : '@word(2,6)',
                'username' : '@word(2,5)',
                'module' : modelList,
                'id|+1' : 1
            },
        'token' : 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ4NzQyMjU2MSwiaWF0IjoxNDg3NDE4OTYxfQ.eyJpZCI6Mn0.QEplkeh0YutYnON_lvpOgLJtVdmF9ChcH-hGrHTl3h4',
        'expiration' : 3600
        })
    console.log(data)
    return data
    }
}
