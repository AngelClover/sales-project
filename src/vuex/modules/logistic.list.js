import api from '../../api'

const GET_LOGISTIC_LIST_SUCCESS = "GET_LOGISTIC_LIST_SUCCESS"
const GET_LOGISTIC_LIST_FAILURE = "GET_LOGISTIC_LIST_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_LOGISTIC_LIST_FAILURE](state){
        state.title = []
        state.content = []
        state.preference = []
    },
    [GET_LOGISTIC_LIST_SUCCESS](state, response_data){
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
    logisticTitle : (state) => state.title,
    logisticContent :  (state) => state.content, 
    logisticPreference : (state) => state.preference,
}

export const getLogisticList = ({commit}) => {
    api.getLogisticList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                return commit(GET_LOGISTIC_LIST_FAILURE, response.data.msg)
            }
            commit(GET_LOGISTIC_LIST_SUCCESS, response.data.data)
        }else{
            commit(GET_LOGISTIC_LIST_FAILURE, response.status + response.statusText)
        }
    }, response => {
        console.log('response fail', response)
        commit(GET_LOGISTIC_LIST_FAILURE)
    })
}

const actions = {
    getLogisticList,
}

export default{
    state,
    mutations,
    getters,
    actions
}


