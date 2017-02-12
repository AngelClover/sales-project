var Mock = require('mockjs')

Mock.Random.cparagraph(2, 5)

authAttr = ['id', 'token']

module.exports = {
    get : function(){
        return Mock.mock({
            'id|1' : 1,
            'token|1' : '@word(16)'
        })
    }
}
