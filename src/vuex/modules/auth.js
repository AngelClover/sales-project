import api from '../../api'

const LOGIN_SUCCESS = "LOGIN_SUCCESS"
const LOGIN_FAILURE = "LOGIN_FAILURE"
const USERINFO_SUCCESS = "USERINFO_SUCCESS"
const USERINFO_FAILURE = "USERINFO_FAILURE"
const LOGOUT_USER = "LOGOUT_USER"
const UPDATE_USER_SUCCESS = "UPDATE_USER_SUCCESS"

import {getCookie, saveCookie} from '../../utils/authService'
import {showMsg, hideMsg} from './toast'

const state = {
    token : getCookie('token') || null,
    user : null,
    error : 0,
    msg : ''
}

const mutations = {
    [LOGIN_SUCCESS](state, response_data){
        state.token = response_data.token
    },
    [LOGIN_FAILURE](state, response_data){
        state.token = getCookie('token') || null
        state.user = null
        state.token = null
    },
    [USERINFO_SUCCESS](state, action){
        state.user = action.user
    },
    [USERINFO_FAILURE](state, action){
        state.user = null
    },
    [LOGOUT_USER](state, action){
        state.token = getCookie('token') || null
        state.user = null
        state.token = null
    },
    [UPDATE_USER_SUCCESS](state, action){
        state.user = action.user
    }
}

const getters = {
    getToken : (state) => {return state.token = getCookie('token') || null }
}

export const getUserInfo = ({commit}) => {
    api.getMe().then(response => {
        if (response.data.error != 0){
            commit(USERINFO_SUCCESS, response.data.data)
        }else{
            commit(USERINFO_FAILURE)
        }
    }, response => {
        commit(USERINFO_FAILURE)
    })
}

//import router from '../../router'
import Vue from 'vue'
export const getLogin = (store, body) => {
    api.Login(body).then(response => {
        console.log('login succ', response)
        if (response.data.error != 0){
            //commit(LOGIN_FAILURE, response.data.msg)
            showMsg(store, response.data.msg || '登录失败')
            return
        }
        const token = response.data.data.token || ""
        saveCookie('token', token)
        getUserInfo({commit})
        store.commit(LOGIN_SUCCESS, {token: response.data.data.token})
        showMsg(store, '登录成功,欢迎光临', 'success')
        console.log('store router', store.rootState)
        //window.location.replace('/')
        window.location.reload(true)
        //TOknow : how to use $router.push here

    }, response => {
        console.log('login fail', response)
        //commit(LOGIN_FAILURE, { 'error':response.status, 'msg':response.statusText})
        showMsg(store, response.statusText || '登录失败')
    })
}

export const register = (store, payload) => {
    api.register(payload).then(response => {
        if (response.data.error != 0){
            showMsg(store, response.data.msg || '登录失败')
        }else{
            showMsg(store, '注册成功, 请用刚注册的用户名登录', 'success')
            var pathname = window.location.pathname
            console.log('register pathname', pathname)
            window.location.replace('#/login')
        }
    }, response=> {
        console.log('register fail', response)
        showMsg(store, response.statusText || '注册失败')
    })

}

const actions = {
    getLogin,
    getUserInfo,
    register
}

export default{
    state,
    mutations,
    getters,
    actions
}
