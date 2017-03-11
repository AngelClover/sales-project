import api from '../../api'

const GET_PERMISSION_LIST_SUCC = "GET_PERMISSION_LIST_SUCC"
const GET_PERMISSION_LIST_FAIL = "GET_PERMISSION_LIST_FAIL"
const UPDATE_PERMISSION_SUCC = "UPDATE_PERMISSION_SUCC"
const UPDATE_PERMISSION_FAIL = "UPDATE_PERMISSION_FAIL"

import {showMsg, hideMsg} from './toast'

const state = {
    permissionList : {},
}

const mutations = {
    [GET_PERMISSION_LIST_SUCC](state, action){
        console.log("in mutasions", action)
        state.permissionList = action
    },
    [GET_PERMISSION_LIST_FAIL](state){
    }
}

const getters = {
    getPermissionList : (state) => {
        return state.permissionList
    }
}

const failBack = ({commit, dispatch}, content, mutation=GET_PERMISSION_FAIL) => {
    console.log('response fail for permissions', content)
    commit(mutation, content)
    dispatch('showMsg', '权限请求失败', 'error')
}

const getPermissionList = (store) => {
    var failMessage = "获取权限列表失败"
    api.getPermissionList().then(response => {
        console.log('get permission list succ', response)
        if (response.status == 200){
            if (response.data.error == 0){
                store.commit(GET_PERMISSION_LIST_SUCC, response.data.data)
                store.dispatch('showMsg', "获取权限列表成功", 'success')
            }else{
                failBack('showMsg', failMessage + response.status + response.stratusText)
            }
        }else{
                failBack('showMsg', failMessage + response.status + response.stratusText)
        }
    }, response => {
        failBack('showMsg', failMessage + response.status + response.stratusText)
    })
}
const addPermissions = (store, payload) => {
    var failMessage = "增加权限失败"
    api.addPermission(payload).then(response => {
        console.log('add permissions succ', response)
        if (response.status == 200 && response.data.error == 0){
            //store.commit(UPDATE_PERMISSION_SUCC,)
            //store.dispatch('showMsg', '增加权限成功')
            console.log('add permssion succ')
            store.dispatch('getUserInfoList')
        } else{
        failBack('showMsg', failMessage + response.status + response.stratusText)
        }
    }, response => {
        failBack('showMsg', failMessage + response.status + response.stratusText)
    })

}
const removePermissions = (store, payload) => {
    var failMessage = "删除权限失败"
    api.removePermission(payload).then(response => {
        console.log('remove permissions succ', response)
        if (response.status == 200 && response.data.error == 0){
            console.log('remove permissions succ')
            store.dispatch('getUserInfoList')
        } else{
            failBack('showMsg', failMessage + response.status + response.stratusText)
        }
    }, response => {
        failBack('showMsg', failMessage + response.status + response.stratusText)
    })
}

const actions = {
    getPermissionList,
    addPermissions,
    removePermissions,
}

export default{
    state,
    mutations,
    getters,
    actions
}
