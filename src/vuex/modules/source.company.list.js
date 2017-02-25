import api from '../../api'

const GET_SOURCE_COMPANY_LIST_SUCCESS = "GET_SOURCE_COMPANY_LIST_SUCCESS"
const GET_SOURCE_COMPANY_LIST_FAILURE = "GET_SOURCE_COMPANY_LIST_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_SOURCE_COMPANY_LIST_FAILURE](state){
        state.title = []
        state.content = []
        state.preference = []
    },
    [GET_SOURCE_COMPANY_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.enterprise
        //state.preference = response_data.preference
        //state.title = response_data.title
        state.title = []
        for (var item in response_data.headers){
            var d = {}
            d['item'] = response_data.headers[item][0]
            d['displayName'] = response_data.headers[item][1]
            if (response_data.headers.length >= 3){
            }
            state.title.push(d)
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
    sourceCompanyTitle : (state) => state.title,
    sourceCompanyContent :  (state) => state.content, 
    sourceCompanyPreference : (state) => state.preference,
}

const failBack = ({commit, dispatch}, content, mutation=GET_SOURCE_COMPANY_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}
export const getSourceCompanyList = (store) => {
    var failMessage = "请求失败"
    api.getSourceCompanyList().then(response => {
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

const updateSourceCompany = (store, payload) => {
    api.updateSourceCompany(payload).then(response => {
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
const saveSourceCompany = (store, payload) => {
    var failMessage = "添加失败"
    api.saveSourceCompany(payload).then(response => {
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
const removeSourceCompany = (store, payload) => {
    var failMessage = "删除失败"
    api.removeSourceCompany(payload).then(response => {
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
const approveSourceCompany = (store, payload) => {
    var failMessage = "审批失败"
    api.approveSourceCompany(payload).then(response => {
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
    getSourceCompanyList,
    updateSourceCompany,
    saveSourceCompany,
    removeSourceCompany,
    approveSourceCompany
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

