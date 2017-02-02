var mock = require('mockjs')
var mockEquipment = require('./resource/equipment')


function addContext(titleContent){
    return {
        error : 0,
        msg : "",
        data : titleContent
    }
}
function addGoodContext(data){
    return {
        error : 0,
        msg : "GoodMessage",
        data
    }
}
function addBadContext(data){
    return {
        error : -1,
        msg : "Bad message",
        data
    }
}

function mockConfig(app){
    /*
    var router = require('express').Router()
    var bodyParser = require('body-parser');
    router.use(bodyParser.json());
    //router.use(bodyParser.urlencoded({ extended: false }));
    */

    mock.Random.integer()
    console.log('mock', mock.mock('@integer'))
    app.get('/integer', (req, res) => {
        var t = mock.mock('@integer')
        console.log("back mock", t, typeof(t))
        res.send(JSON.stringify(t))
    })
    app.get('/api/equipment', (req, res) => {
        res.send(addContext(mockEquipment.get()))
    })
    app.post('/api/equipment', (req, res) => {
        res.send(addGoodContext(mockEquipment.post(req)))
    })
    app.put('/api/equipment', (req, res) => {
        res.send(addGoodContext(mockEquipment.put(req)))
    })
    app.delete('/api/equipment', (req, res) => {
        res.send(addGoodContext(mockEquipment.delete(req)))
    })
}

module.exports = mockConfig
