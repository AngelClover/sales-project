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

function addPath(app, path, mod){
    app.get('/api/' + path, (req, res) => {
        res.send(addContext(mod.get()))
    })
    app.post('/api/' + path, (req, res) => {
        res.send(addGoodContext(mod.post(req)))
    })
    app.put('/api/' + path, (req, res) => {
        res.send(addGoodContext(mod.put(req)))
    })
    app.delete('/api/' + path, (req, res) => {
        res.send(addGoodContext(mod.delete(req)))
    })
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

    //for example
    //sourceEquipment
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
    //sourceCompany
    addPath(app, 'sourcecompany', require('./resource/sourceCompany'))
    //sourceCustomer
    addPath(app, 'sourcecustomer', require('./resource/sourceCustomer'))

    //saleOrder
    addPath(app, 'saleorder', require('./resource/saleOrder'))
    //
    addPath(app, 'buyorder', require('./resource/buyOrder'))

}

module.exports = mockConfig
