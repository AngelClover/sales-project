/*
import {
    GET_EQUIPMENT_LIST_SUCCESS,
    GET_EQUIPMENT_LIST_FAILURE
} from '../types'
*/
//import {getEquipmentList} from '../actions'
import api from '../../api'

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
        state.title = []
        state.content = []
        state.preference = []
    },
    [GET_EQUIPMENT_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.equipments
        //state.preference = response_data.preference
        //state.title = response_data.headers
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
        console.log(state.title)
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

const failBack = ({commit, dispatch}, content) => {
    console.log('response fail', content)
    commit(GET_EQUIPMENT_LIST_FAILURE, content)
    dispatch('showMsg', '请求失败', 'error')
}

export const getEquipmentList = (store) => {
    api.getEquipmentList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, '请求失败 ' + response.data.msg)
            }else{
                store.commit(GET_EQUIPMENT_LIST_SUCCESS, response.data.data)
            }
        }else{
            //commit(GET_EQUIPMENT_LIST_FAILURE, response.status + response.statusText)
            failBack(store, '请求失败 ' + response.status + response.statusText)
        }
    }, response => {
        console.log('response fail', response)
        //commit(GET_EQUIPMENT_LIST_FAILURE)
        failBack(store, '请求失败 ' + response.status + response.statusText)
    })
}

const updateEquipment = ({dispatch}, payload) => {
    api.updateEquipment(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                dispatch('showMsg', response.data.error + response.data.msg)
            }
            dispatch('showMsg', '修改成功', 'success')
        }else{
            dispatch('showMsg', response.status + response.statusText)
        }
    }, response => {
        dispatch('showMsg', response.status + response.statusText)
    })
}
const saveEquipment = ({dispatch}, payload) => {
    api.saveEquipment(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                dispatch('showMsg', response.data.error + response.data.msg)
            }else{
                dispatch('showMsg', '添加成功', 'success')
            }
        }else{
            dispatch('showMsg', response.status + response.statusText)
        }
    }, response => {
        dispatch('showMsg', response.status + response.statusText)
    })
}
const removeEquipment = ({dispatch}, payload) => {
    api.removeEquipment(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                dispatch('showMsg', response.data.error + response.data.msg)
            }else{
                dispatch('showMsg', '删除成功', 'success')
            }
        }else{
            dispatch('showMsg', response.status + response.statusText)
        }
    }, response => {
        dispatch('showMsg', response.status + response.statusText)
    })
}

const actions = {
    getEquipmentList,
    updateEquipment,
    saveEquipment,
    removeEquipment
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


