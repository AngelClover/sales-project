import api from '../../api'
import hp from '../../utils/HeaderParser'

const GET_SOURCE_CUSTOMER_LIST_SUCCESS = "GET_SOURCE_CUSTOMER_LIST_SUCCESS"
const GET_SOURCE_CUSTOMER_LIST_FAILURE = "GET_SOURCE_CUSTOMER_LIST_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_SOURCE_CUSTOMER_LIST_FAILURE](state){
        state.title = []
        state.content = []
        state.preference = []
    },
    [GET_SOURCE_CUSTOMER_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.enterprises
        //state.preference = response_data.preference
        //state.title = response_data.title
        state.title = []
        for (var item in response_data.headers){
            /*
            var d = {}
            d['item'] = response_data.headers[item][0]
            d['displayName'] = response_data.headers[item][1]
            if (response_data.headers.length >= 3){
            }
            */
            var header = hp.HeaderParser(response_data.headers[item])
            header.displayInList = true
            console.log('header in vuex', header)
            state.title.push(header)
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
    sourceCustomerTitle : (state) => state.title,
    sourceCustomerContent :  (state) => state.content, 
    sourceCustomerPreference : (state) => state.preference,
}
const failBack = ({commit, dispatch}, content, mutation=GET_SOURCE_COMPANY_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}
export const getSourceCustomerList = (store) => {
    var failMessage = "请求失败"
    console.log('getSourceCustomerList dispatched')
    api.getSourceCustomerList().then(response => {
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.msg)
            }else{
                store.commit(GET_SOURCE_COMPANY_LIST_SUCCESS, response.data.data)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateSourceCustomer = (store, payload) => {
    api.updateSourceCustomer(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, "更新失败" + response.data.error + response.data.msg)
            } else{
                store.dispatch('showMsg', '修改成功', 'success')
            }
        } else{
            failBack(store, "更新失败" + response.status + response.statusText)
        }
    }, response => {
        failBack(store, "更新失败" + response.status + response.statusText)
    })
}
const saveSourceCustomer = (store, payload) => {
    var failMessage = "添加失败"
    api.saveSourceCustomer(payload).then(response => {
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
const removeSourceCustomer = (store, payload) => {
    var failMessage = "删除失败"
    api.removeSourceCustomer(payload).then(response => {
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
const approveSourceCustomer = (store, payload) => {
    var failMessage = "审批失败"
    api.approveSourceCustomer(payload).then(response => {
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

/*
export const getSourceCustomerList = ({commit}) => {
    api.getSourceCustomerList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                return commit(GET_SOURCE_CUSTOMER_LIST_FAILURE, response.data.msg)
            }
            commit(GET_SOURCE_CUSTOMER_LIST_SUCCESS, response.data.data)
        }else{
            commit(GET_SOURCE_CUSTOMER_LIST_FAILURE, response.status + response.statusText)
        }
    }, response => {
        console.log('response fail', response)
        commit(GET_SOURCE_CUSTOMER_LIST_FAILURE)
    })
}
*/

const actions = {
    getSourceCustomerList,
    updateSourceCustomer,
    saveSourceCustomer,
    removeSourceCustomer,
    approveSourceCustomer
    /*
    getEquipmentList : async ({commit}) => {
        console.log('angel commit in module dispatch')
        //commit()
        const res = await api.getEquipmentList()
        commit('GET_EQUIPMENT_LIST_SUCCESS', res)
    }
    */
}

export default{
    state,
    mutations,
    getters,
    actions
}

