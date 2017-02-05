import api from '../../api'

const GET_REPAIR_LIST_SUCCESS = "GET_REPAIR_LIST_SUCCESS"
const GET_REPAIR_LIST_FAILURE = "GET_REPAIR_LIST_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_REPAIR_LIST_FAILURE](state){
        state.title = []
        state.content = []
        state.preference = []
    },
    [GET_REPAIR_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.title = response_data.title
        state.content = response_data.content
        state.preference = response_data.preference
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

export const getRepairList = ({commit}) => {
    api.getRepairList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                return commit(GET_REPAIR_LIST_FAILURE, response.data.msg)
            }
            commit(GET_REPAIR_LIST_SUCCESS, response.data.data)
        }else{
            commit(GET_REPAIR_LIST_FAILURE, response.status + response.statusText)
        }
    }, response => {
        console.log('response fail', response)
        commit(GET_REPAIR_LIST_FAILURE)
    })
}

const actions = {
    getRepairList,
}

export default{
    state,
    mutations,
    getters,
    actions
}


