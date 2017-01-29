import {
    GET_EQUIPMENT_LIST_SUCCESS,
    GET_EQUIPMENT_LIST_FAILURE
} from '../types'

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
    }
}

const getters = {
    /*
    title : ({equipmentList}) => equipmentList.title,
    content : ({equipmentList}) => equipmentList.content,
    preference : ({equipmentList}) => equipmentList.preference,
    */
    title : function(state) { console.log('title in getters', state); return state.title},
    content :  ({state}) => state.content, 
    //content :  (state) => state.content, 
    //content : function(state) { return state.content },
    preference : (state) => state.preference,
}

/*
const actions = {
    getEquipmentList : async ({commit}) => {
        console.log('angel commit in module dispatch')
        //commit()
        const res = await api.getEquipmentList()
        commit('GET_EQUIPMENT_LIST_SUCCESS', res)
    }
}
*/

export default{
    state,
    mutations,
    getters,
    //actions
}


