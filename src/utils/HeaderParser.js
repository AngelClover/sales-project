
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

    

