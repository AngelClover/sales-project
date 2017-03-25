var xl = require('node-xlrd');
var ep = require('excel-parser')
var paName = "product.xls"
var pbName = "product1.xls"
var caName = "com.xls"
var cbName = "com1.xls"

ep.parse({
    inFile:pbName,
    worksheet: 1,
}, function(err, bk){
    console.log("pa")
    if (err){
        console.log(err)
    }
    console.log(bk.length)
    return

})
