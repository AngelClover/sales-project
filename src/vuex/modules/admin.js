import api from '../../api'

const GET_USERINFO_LIST_SUCCESS = "GET_USERINFO_LIST_SUCCESS"
const GET_USERINFO_LIST_FAILURE = "GET_USERINFO_LIST_FAILURE"

import {showMsg, hideMsg} from './toast'

const state = {
    userList : [],
}

const mutations = {
    [GET_USERINFO_LIST_SUCCESS](state, action){
        state.userList = action.userList
    },
    [GET_USERINFO_LIST_FAILURE](state){
        state.userList = []
    }
}

const getters = {
    getUserList : (state) => {
        return state.userList
    }
}
const getUserInfoList = ({commit}) =>{
    //TODO: to substitute
    api.getMe().then(response => {
        console.log('getUserInfo', response.data.data)
        var err = response.data.error || 0
        if (err == 0){
            var arr = []
            for (var i = 0; i < 10; ++i){
                arr.push(response.data.data)
            }
            console.log('getUserInfoSucc', arr)
            commit(GET_USERINFO_LIST_SUCCESS, {userList:arr})
        }else{
            commit(GET_USERINFO_LIST_FAILURE)
        }
    }, response => {
        commit(GET_USERINFO_LIST_FAILURE)
    })
    /*
    api.getUserInfo(payload).then(response => {
    }, response=>{
    })
    */
}

const actions = {
    getUserInfoList,
}

export default{
    state,
    mutations,
    getters,
    actions
}
