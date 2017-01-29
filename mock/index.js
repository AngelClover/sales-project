var mock = require('mockjs')
var mockEquipment = require('./resource/equipment')

function addContext(titleContent){
    return {
        error : 0,
        msg : "",
        data : titleContent
    }
}

function mockConfig(app){
    mock.Random.integer()
    console.log('mock', mock.mock('@integer'))
    app.get('/integer', (req, res) => {
        var t = mock.mock('@integer')
        console.log("back mock", t, typeof(t))
        res.send(JSON.stringify(t))
    })
    app.get('/api/equipment', (req, res) => {
        res.send(addContext(mockEquipment()))
    })
}

module.exports = mockConfig
