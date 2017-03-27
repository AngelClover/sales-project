var xl = require('node-xlrd');
var ep = require('excel-parser')
var paName = "product.xls"
var pbName = "product1.xls"
var caName = "com.xls"
var cbName = "com1.xls"

ep.parse({
    inFile:paName,
    worksheet: 1,
}, function(err, bk){
    console.log("pa")
    if (err){
        console.log(err)
    }
    //console.log(bk.length)
    /*
    for (var i in bk){
        console.log('INSERT INTO equipment SET accessory = ', bk[i]);
    }
    */
    for (var i in bk){
        if (i > 0){
            var obj = {}
            for (var j in bk[i]){
                //console.log("x", bk[i][j])
                var label = bk[0][j]
                if (label == '产品编码')continue
                if (label == '产品简称')label = "简称"
                if (label == '产品名称')label = "名称"
                if (label == '产品英文名称')label = "英文名称"
                if (label == '流程状态')continue
                if (label == '审批结果')continue
                obj[label] = bk[i][j]
            }
            //console.log('INSERT INTO equipment SET accessory = ', JSON.stringify(obj));
            console.log(obj)
        }
    }
    return

})
