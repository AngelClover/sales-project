import api from '../../api'

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
    sourceCustomerTitle : (state) => state.title,
    sourceCustomerContent :  (state) => state.content, 
    sourceCustomerPreference : (state) => state.preference,
}

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

const actions = {
    getSourceCustomerList,
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

