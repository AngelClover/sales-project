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

const failBack = ({commit, dispatch}, content, mutation=GET_USERINFO_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}

const getUserInfoList = (store) =>{
    var failMessage = "获取失败"
    api.getUserInfoList().then(response => {
        console.log('getUserInfoList', response.data.data)
        var err = response.data.error || 0
        if (err == 0){
            /*
            var arr = []
            for (var i = 0; i < 10; ++i){
                arr.push(response.data.data)
            }
            */
            //console.log('getUserInfoListSucc', arr)
            //store.commit(GET_USERINFO_LIST_SUCCESS, {userList:arr})
            store.commit(GET_USERINFO_LIST_SUCCESS, response.data.data)
            store.dispatch('showMsg', '获取用户信息列表成功', 'success')
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
            failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateUserInfo = (store, payload) => {
    var failMessage = "更新失败"
    api.updateUserInfo(payload).then(response => {
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
const saveUserInfo = (store, payload) => {
    var failMessage = "添加失败"
    api.saveUserInfo(payload).then(response => {
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
const removeUserInfo = (store, payload) => {
    var failMessage = "删除失败"
    api.removeUserInfo(payload).then(response => {
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

const actions = {
    getUserInfoList,
    updateUserInfo,
    saveUserInfo,
    removeUserInfo,
}

export default{
    state,
    mutations,
    getters,
    actions
}
