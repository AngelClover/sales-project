
function normalizeList(obj){
    if (typeof(obj) == Array)return obj
    else if (typeof(obj) == Object)return [obj]
    else return null
}
/* immutable 放在服务端，客户端暂时不做
 */
function pipe(obj){
    if (obj['type']) return obj
    //if (typeof(obj['item']) == undefined) return obj
    switch (obj['item']){
        case '规格':
            obj['type'] = 'star'; break;
        case '单位':
            obj['type'] = 'option';
            obj['selectOptions'] = ['', '盒', '瓶'];
            break;
            /*
        case '厂商':
            obj['type'] = 'option';
            object['selectOptions'] = ['盒'，'瓶'];
            break;
            */
        case '结算方式':
            obj['type'] = 'option';
            obj['selectOptions'] = ['', '现金', '打款'];
            break;
        case '币种':
            obj['type'] = 'option';
            obj['selectOptions'] = ['', '人民币', '美元'];
            break;
        default:
            break;
    }
    if (obj['item'] && obj['item'].search('日期') >= 0 ||
            obj['displayName'] && obj['displayName'].search('日期')  >= 0){
        obj['type'] = 'date'
    }
    if (obj['item'] && obj['item'].search('时间') >= 0 ||
            obj['displayName'] && obj['displayName'].search('时间')  >= 0){
        obj['type'] = 'time'
    }
    if (obj['item'] && obj['displayName'].search('保修期限') >= 0 ||
            obj['displayName'] && obj['displayName'].search('日期')  >= 0){
        obj['type'] = 'date'
    }
    if (obj['item'] && obj['displayName'].search('文件') >= 0 ||
            obj['displayName'] && obj['displayName'].search('材料')  >= 0){
        obj['type'] = 'file'
    }
    
    switch (obj['displayName']){
        case '单价':
            obj['type'] = 'price';
            obj['invisable'] = true;
            break;
        case '数量':
            obj['type'] = 'number';
            obj['invisable'] = true;
            break;
        case '总价':
            obj['type'] = 'price';
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '在库数字':
            obj['type'] = 'number';
            break;
        case '审核人':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '创建人':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '是否接收':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '是否检验':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '是否入库':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '接收人':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '检验人':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        case '入库人':
            obj['immutable'] = true;
            obj['invisable'] = true;
            break;
        default : 
            break;
    }
    return obj
}
function HeaderParser(a){
    if (typeof(a) == undefined) return null
    var obj = {}
    obj['item'] = a[0]
    obj['displayName'] = a[1]
    obj['display'] = true
    for (var i = 2; i < a.length; ++i){
        if (a[i] == 'option'){
            i++
            obj['type'] = 'select'
            obj['selectOptions'] = normalizeList(a[i])
        }
        if (a[i] == 'number'){
            obj['type'] = 'number'
        }
        if (a[i] == 'immutable'){
            obj['immutable'] = true
        }
        if (a[i] == 'hide'){
            obj['display'] = false
        }
    }
    
    obj = pipe(obj)

    console.log(obj)
    return obj
}
export default {
    HeaderParser,
}

    

