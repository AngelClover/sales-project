var Mock = require('mockjs')

Mock.Random.cparagraph(2, 5)

authAttr = ['id', 'token']

module.exports = {
    get : function(){
        return Mock.mock({
            'id|1' : 1,
            'token|1' : '@word(16)'
        })
    },

    authorize : function(id) {
        return Mock.mock({})
    },
    unauthorize : function(id) {
        return Mock.mock({})
    },
    permission : function() {
        return Mock.mock([
        ['equipment', {
         'read' : 0x01,
         'write' : 0x02,
         'approve' : 0x04
         }],
        ['enterprise', {
         'read' : 0x08,
         'write' : 0x10,
         'approve' : 0x20
         }],
        ['purchase', {
         'read' : 0x40,
         'write' : 0x80,
         'approve' : 0x100
         }],
        ['sale', {
         'read' : 0x200,
         'write' : 0x400,
         'approve' : 0x800
         }],
        ['store', {
         'read' : 0x1000,
         'write' : 0x2000,
         'approve' : 0x4000
         }],
        ['repair', {
         'read' : 0x8000,
         'write' : 0x10000,
         'approve' : 0x20000
         }],
        ['logistic', {
         'read' : 0x40000,
         'write' : 0x80000,
         'approve' : 0x100000
         }],
        ['finance', {
         'read' : 0x200000,
         'write' : 0x400000,
         'approve' : 0x800000
         }],
        ['administer', 0xffffffff]
    ])
    }
}
