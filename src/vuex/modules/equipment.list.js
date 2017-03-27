/*
import {
    GET_EQUIPMENT_LIST_SUCCESS,
    GET_EQUIPMENT_LIST_FAILURE
} from '../types'
*/
//import {getEquipmentList} from '../actions'
import api from '../../api'
import hp from '../../utils/HeaderParser'

const GET_EQUIPMENT_LIST_SUCCESS = "GET_EQUIPMENT_LIST_SUCCESS"
const GET_EQUIPMENT_LIST_FAILURE = "GET_EQUIPMENT_LIST_FAILURE"
const SAVE_EQUIPMENT_SUCCESS = "SAVE_EQUIPMENT_SUCCESS"
const SAVE_EQUIPMENT_FAILURE = "SAVE_EQUIPMENT_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_EQUIPMENT_LIST_FAILURE](state){
        /*
        state.title = []
        state.content = []
        state.preference = []
        */
    },
    [GET_EQUIPMENT_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.equipments
        //state.preference = response_data.preference
        //state.title = response_data.headers
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
        //console.log(state.title)
    },
}

/*
const getters = {
    title : function(state) { console.log('title in getters', state); return state.title},
    content :  ({state}) => state.content, 
    preference : (state) => state.preference,
}
*/
const getters = {
    equipmentTitle : (state) => state.title,
    equipmentContent :  (state) => state.content, 
    equipmentPreference : (state) => state.preference,
}

const failBack = ({commit, dispatch}, content, mutation=GET_EQUIPMENT_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}

export const getEquipmentList = (store) => {
    var failMessage = "请求失败"
    api.getEquipmentList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.commit(GET_EQUIPMENT_LIST_SUCCESS, response.data.data)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateEquipment = (store, payload) => {
    var failMessage = "更新失败"
    api.updateEquipment(payload).then(response => {
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
const saveEquipment = (store, payload) => {
    var failMessage = "添加失败"
    api.saveEquipment(payload).then(response => {
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
const removeEquipment = (store, payload) => {
    var failMessage = "删除失败"
    api.removeEquipment(payload).then(response => {
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
const approveEquipment = (store, payload) => {
    var failMessage = "审批失败"
    api.approveEquipment(payload).then(response => {
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
    getEquipmentList,
    updateEquipment,
    saveEquipment,
    removeEquipment,
    approveEquipment,
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


