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
        state.title = response_data.title
        state.content = response_data.content
        state.preference = response_data.preference
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

export const getEquipmentList = ({commit}) => {
    api.getEquipmentList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                return commit(GET_EQUIPMENT_LIST_FAILURE, response.data.msg)
            }
            commit(GET_EQUIPMENT_LIST_SUCCESS, response.data.data)
        }else{
            commit(GET_EQUIPMENT_LIST_FAILURE, response.status + response.statusText)
        }
    }, response => {
        console.log('response fail', response)
        commit(GET_EQUIPMENT_LIST_FAILURE)
    })
}

const updateEquipment = ({dispatch}, payload) => {
    api.updateEquipment(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                //commit(SAVE_EQUIPMENT_FAILURE, response.data.msg)
                dispatch('showMsg', response.data.error + response.data.msg)
            }
            //commit(SAVE_EQUIPMENT_SUCCESS, response.data.data)
        }else{
            dispatch('showMsg', response.status + response.statusText)
        }
    }, response => {
        //console.log('save response fail', response)
        dispatch('showMsg', response.status + response.statusText)
        //commit(SAVE_EQUIPMENT_FAILURE)
    })
}

const actions = {
    getEquipmentList,
    updateEquipment,
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


