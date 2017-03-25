var xl = require('node-xlrd');
var ep = require('excel-parser')
var paName = "product.xls"
var pbName = "product1.xls"
var caName = "com.xls"
var cbName = "com1.xls"

var comData = []
/*
ep.parse({
    inFile:caName,
    //worksheet: 1,
    //skipEmpty: true,
},function(err, bk){
    if (err){
        console.log(err)
    }
    console.log(bk)
    console.log("ca", bk.length)
        return
    var n = bk.sheet.count
        var cname = []
    for (var si = 0; si < n; ++si){
        console.log('sheet ', si)
        console.log('load ', bk.sheet.loaded(si))
        var s = bk.sheets[si], rn = s.row.count, cn=s.column.count
        console.log('name:', s.name, 'rn:', rn, 'cn:', cn)
        for (var j = 0; j < cn ; ++j){
            cname.push(s.cell(0, j))
        }
        for (var i = 1; i < rn; ++i){
            var row = ""
            var obj = {}
            for (var j = 0; j < cn; ++j){
                try{
                    var x = s.cell(i, j)
                    row += x + " " 
                    obj[cname[j]] = x
                }catch(e){
                    console.log(e.message)
                }
            }
            //console.log(obj)
            comData.push(obj)
        }
    }
})
*/
/*
ep.parse({
    inFile:cbName,
    worksheet: 1,
    //skipEmpty: true,
} , function(err, bk){
    if (err){
        console.log(err)
    }
    console.log("cb", bk.length)
    //console.log(bk)
    return

    var n = bk.sheet.count
        var cname = []
    console.log('n:%d', n)
    for (var si = 0; si < n; ++si){
        console.log('sheet ', si)
        console.log('load ', bk.sheet.loaded(si))
        var s = bk.sheets[si], rn = s.row.count, cn=s.column.count
        console.log('name:', s.name, 'rn:', rn, 'cn:', cn)
        for (var j = 0; j < cn ; ++j){
            cname.push(s.cell(0, j))
        }
        for (var i = 1; i < rn; ++i){
            var row = ""
            var obj = {}
            for (var j = 0; j < cn; ++j){
                try{
                    var x = s.cell(i, j)
                    row += x + " " 
                    obj[cname[j]] = x
                }catch(e){
                    console.log(e.message)
                }
            }
            //console.log(obj)
            comData.push(obj)
        }
    }
})
*/
//console.log(comData)
/*
ep.parse({
    inFile:paName,
    worksheet: 1,
}, function(err, bk){
    console.log("pa")
    if (err){
        console.log(err)
    }
    console.log(bk.length)
    return

})
*/
setTimeout(ep.parse({
    inFile:pbName,
    worksheet: 1,
}, function(err, bk){
    console.log("pb")
    if (err){
        console.log(err)
    }
    console.log(bk.length)
    return

}), 10000)
