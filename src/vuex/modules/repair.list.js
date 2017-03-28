import api from '../../api'
import hp from '../../utils/HeaderParser'

const GET_REPAIR_LIST_SUCCESS = "GET_REPAIR_LIST_SUCCESS"
const GET_REPAIR_LIST_FAILURE = "GET_REPAIR_LIST_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_REPAIR_LIST_FAILURE](state){
        /*
        state.title = []
        state.content = []
        state.preference = []
        */
    },
    [GET_REPAIR_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.repairs
        state.title = []//response_data.headers
        for (var item in response_data.headers){
            /*
            var d = {}
            d['item'] = response_data.headers[item][0]
            d['displayName'] = response_data.headers[item][1]
            if (response_data.headers.length >= 3){
                //TODO: specify
            }
            state.title.push(d)
            */
            state.title.push(hp.HeaderParser(response_data.headers[item]))
        }
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
    repairTitle : (state) => state.title,
    repairContent :  (state) => state.content, 
    repairPreference : (state) => state.preference,
}
const failBack = ({commit, dispatch}, content, mutation=GET_REPAIR_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}
export const getRepairList = (store) => {
    var failMessage = "请求失败"
    api.getRepairList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.commit(GET_REPAIR_LIST_SUCCESS, response.data.data)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateRepair = (store, payload) => {
    var failMessage = "更新失败"
    api.updateRepair(payload).then(response => {
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
const saveRepair = (store, payload) => {
    var failMessage = "添加失败"
    api.saveRepair(payload).then(response => {
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
const removeRepair = (store, payload) => {
    var failMessage = "删除失败"
    api.removeRepair(payload).then(response => {
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
const approveRepair = (store, payload) => {
    var failMessage = "审批失败"
    api.approveRepair(payload).then(response => {
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

const actions = {
    getRepairList,
    updateRepair,
    saveRepair,
    removeRepair,
    approveRepair
}

export default{
    state,
    mutations,
    getters,
    actions
}


