var xl = require('node-xlrd');
var ep = require('excel-parser')
var paName = "product.xls"
var pbName = "product1.xls"
var caName = "com.xls"
var cbName = "com1.xls"
var _ = require("underscore")

var blackList = ["流程状态", "审批结果", "编号"]
xl.open(caName,function(err, bk){
    if (err){
        console.log(err)
    }
    var comData = []
    var n = bk.sheet.count
        var cname = []
    for (var si = 0; si < n; ++si){
        console.log('sheet ', si)
        console.log('load ', bk.sheet.loaded(si))
        var s = bk.sheets[si], rn = s.row.count, cn=s.column.count
        console.log('name:', s.name, 'rn:', rn, 'cn:', cn)
        for (var j = 0; j < cn ; ++j){
            var x = s.cell(0, j)
            x = x.replace('供应商', '')
            cname.push(x)
        }
        console.log(cname)
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
    console.log('ca', comData.length)
    var filteredData = []
    for (var i = 0; i < comData.length; ++i){
        var obj = _.omit(comData[i], blackList)
        filteredData.push(obj)
    }
    console.log(filteredData)
})
