import api from '../../api'

const GET_STORE_HOUSE_LIST_SUCCESS = "GET_STORE_HOUSE_LIST_SUCCESS"
const GET_STORE_HOUSE_LIST_FAILURE = "GET_STORE_HOUSE_LIST_FAILURE"
const UPDATE_STORES_FOR_EQUIPMENT = "UPDATE_STORES_FOR_EQUIPMENT"

const state = {
    title : [],
    content : [],
    preference : [],
    storeForEquipment : {},
}

const mutations = {
    [GET_STORE_HOUSE_LIST_FAILURE](state){
        state.title = []
        state.content = []
        state.preference = []
        state.storeForEquipment = {}
    },
    [GET_STORE_HOUSE_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.stores
        state.title = []//response_data.headers
        for (var item in response_data.headers){
            var d = {}
            d['item'] = response_data.headers[item][0]
            d['displayName'] = response_data.headers[item][1]
            if (response_data.headers.length >= 3){
                //TODO: specify
            }
            state.title.push(d)
        }
    },
    [UPDATE_STORES_FOR_EQUIPMENT](state, data){
        state.storeForEquipment[data.id] = data.list
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
    storeHouseTitle : (state) => state.title,
    storeHouseContent :  (state) => state.content, 
    storeHousePreference : (state) => state.preference,
    inStore : (state) => state.storeForEquipment,
}

const failBack = ({commit, dispatch}, content, mutation=GET_STORE_HOUSE_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}

export const getStoreHouseList = (store) => {
    var failMessage = "请求失败"
    api.getStoreHouseList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.commit(GET_STORE_HOUSE_LIST_SUCCESS, response.data.data)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateStoreHouse = (store, payload) => {
    var failMessage = "更新失败"
    api.updateStoreHouse(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            } else{
                store.dispatch('showMsg', '修改成功', 'success')
            }
        } else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
const saveStoreHouse = (store, payload) => {
    var failMessage = "添加失败"
    api.saveStoreHouse(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '添加成功', 'success')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
const removeStoreHouse = (store, payload) => {
    var failMessage = "删除失败"
    api.removeStoreHouse(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '删除成功', 'success')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
const approveStoreHouse = (store, payload) => {
    var failMessage = "审批失败"
    api.approveStoreHouse(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '审批成功', 'success')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const getStoredEquipmentList = (store, payload) => {
    var failMessage = "获取在库设备失败"
    api.storedEquipmentList(payload).then(response => {
        console.log('get stored equipment list succ', response)
        if (response.status == 200 && response.data.error == 0){
            console.log('got data', response.data.data)
            store.dispatch('showMsg', '获取在库设备成功', 'success')
            store.commit(UPDATE_STORES_FOR_EQUIPMENT, {id: payload.id, list:response.data.data})
        } else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

//one equipment type , multi store id
const outStoreEquipmentList = (store, payload) => {
    var failMessage = "出库失败"
    api.storeOut(payload).then(response => {
        console.log("outstore request succ", response)
        if (response.status == 200 && reponse.data.error == 0){
            console.log("outstore succ", response)
            store.dispatch('showMsg', '出库成功', 'success')
            store.dispatch('getStoreHouseList')
        } else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        console.log("outstore request fail", response)
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const actions = {
    getStoreHouseList,
    updateStoreHouse,
    saveStoreHouse,
    removeStoreHouse,
    approveStoreHouse,
    getStoredEquipmentList,
    outStoreEquipmentList,
}

export default{
    state,
    mutations,
    getters,
    actions
}


