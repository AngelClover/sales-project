import api from '../../api'

const USERINFO_SUCCESS = "USERINFO_SUCCESS"
const USERINFO_FAILURE = "USERINFO_FAILURE"
const UPDATE_USER_SUCCESS = "UPDATE_USER_SUCCESS"
const LOGOUT_USER = "LOGOUT_USER"

import {getCookie, saveCookie} from '../../utils/authService'
import {showMsg, hideMsg} from './toast'

const state = {
    user : null,
}

const mutations = {
    [USERINFO_SUCCESS](state, action){
        console.log('userinfo_success', action)
        console.log('userinfo_success', action.user)
        state.user = action.user
        saveCookie('user', action.user)
    },
    [USERINFO_FAILURE](state, action){
        console.log('userinfo_failure')
        state.user = null
    },
    [LOGOUT_USER](state, action){
        state.user = null
        console.log('clear user')
    },
    [UPDATE_USER_SUCCESS](state, action){
        console.log('update userinfo_success', action)
        state.user = action.user
        saveCookie('user', action.user)
    }
}

const getters = {
    getMe : (state) => {
        console.log('user getters', state.user)
        console.log('user getters', getCookie('user'))
        return state.user || getCookie('user') }
}

export const getUserInfo = ({commit}) => {
    api.getMe().then(response => {
        console.log('getUserInfo', response.data.data)
        var err = response.data.error || 0
        if (err == 0){
            commit(USERINFO_SUCCESS, response.data.data)
        }else{
            commit(USERINFO_FAILURE)
        }
    }, response => {
        commit(USERINFO_FAILURE)
    })
}

const actions = {
    getUserInfo,
}

export default{
    state,
    mutations,
    getters,
    actions
}
