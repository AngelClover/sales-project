import api from '../../api'
import hp from '../../utils/HeaderParser'

const GET_BUY_ORDER_LIST_SUCCESS = "GET_BUY_ORDER_LIST_SUCCESS"
const GET_BUY_ORDER_LIST_FAILURE = "GET_BUY_ORDER_LIST_FAILURE"

const state = {
    title : [],
    subtitle : [],
    content : [],
    preference : [],
}

const mutations = {
    [GET_BUY_ORDER_LIST_FAILURE](state){
        /*
        state.title = []
        state.content = []
        state.preference = []
        */
    },
    [GET_BUY_ORDER_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.purchase_orders
        state.title = []//response_data.headers
        state.subtitle = []
        var findSpace = false
        for (var item in response_data.headers){
            if (response_data.headers[item].length == 0){
                findSpace = true
                continue
            }
            if (findSpace == false){
                state.title.push(hp.HeaderParser(response_data.headers[item]))
            }else {
                state.subtitle.push(hp.HeaderParser(response_data.headers[item]))
            }
        }
        console.log('title parse', state.title, state.subtitle)
    }
}

/*
const getters = {
    title : function(state) { console.log('title in getters', state); return state.title},
    content :  ({state}) => state.content, 
    preference : (state) => state.preference,
}
*/
const getters = {
    buyOrderTitle : (state) => state.title,
    buyOrderSubtitle : (state) => state.subtitle,
    buyOrderContent :  (state) => state.content, 
    buyOrderPreference : (state) => state.preference,
}

const failBack = ({commit, dispatch}, content, mutation=GET_BUY_ORDER_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}


export const getBuyOrderList = (store) => {
    var failMessage = "请求失败"
    api.getBuyOrderList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.commit(GET_BUY_ORDER_LIST_SUCCESS, response.data.data)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateBuyOrder = (store, payload) => {
    var failMessage = "更新失败"
    api.updateBuyOrder(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            } else{
                store.dispatch('showMsg', '修改成功', 'success')
                store.dispatch('getBuyOrderList')
            }
        } else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
const saveBuyOrder = (store, payload) => {
    var failMessage = "添加失败"
    api.saveBuyOrder(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '添加成功', 'success')
                store.dispatch('getBuyOrderList')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
const removeBuyOrder = (store, payload) => {
    var failMessage = "删除失败"
    api.removeBuyOrder(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '删除成功', 'success')
                store.dispatch('getBuyOrderList')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
const approveBuyOrder = (store, payload) => {
    var failMessage = "审批失败"
    api.approveBuyOrder(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '审批成功', 'success')
                store.dispatch('getBuyOrderList')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const transferBuyOrder = (store, payload) => {
    var failMessage = "采购订单采购申请失败"
    api.transferBuyOrder(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单采购申请成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}

const receiveInAllBuyOrder = (store, payload) => {
    var failMessage = "采购订单接收操作失败"
    api.receiveInAll(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单接收操作成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}
const inspectInAllBuyOrder = (store, payload) => {
    var failMessage = "采购订单检验操作失败"
    api.inspectInAll(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单检验操作成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}
const storeInAllBuyOrder = (store, payload) => {
    var failMessage = "采购订单入库操作失败"
    api.storeInAll(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单入库操作成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}

const receiveInOneBuyOrder = (store, payload) => {
    var failMessage = "采购订单单个物品接收操作失败"
    api.receiveInOne(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单单个物品接收操作成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}
const inspectInOneBuyOrder = (store, payload) => {
    var failMessage = "采购订单单个物品检验操作失败"
    api.inspectInOne(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单单个物品检验操作成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}
const storeInOneBuyOrder = (store, payload) => {
    var failMessage = "采购订单单个物品入库操作失败"
    api.storeInOne(payload).then(response => {
        console.log('transfer response succ', response)
        if (response.status == 200 && response.data.error == 0){
            store.dispatch('showMsg', '采购订单单个物品入库操作成功', 'successs')
            store.dispatch('getBuyOrderList')
        }else{
            failBack(store, failMessage + response.data.error + response.data.msg)
        }
    }, response => {
        failBack(store, failMessage + response.data.error + response.data.msg)
    })
}

const actions = {
    getBuyOrderList,
    updateBuyOrder,
    saveBuyOrder,
    removeBuyOrder,
    approveBuyOrder,
    transferBuyOrder,
    receiveInAllBuyOrder,
    inspectInAllBuyOrder,
    storeInAllBuyOrder,
    receiveInOneBuyOrder,
    inspectInOneBuyOrder,
    storeInOneBuyOrder,
}

export default{
    state,
    mutations,
    getters,
    actions
}


