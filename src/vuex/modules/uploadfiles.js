/*
import {
    GET_UPLOADFILE_LIST_SUCCESS,
    GET_UPLOADFILE_LIST_FAILURE
} from '../types'
*/
//import {getFileList} from '../actions'
import api from '../../api'
import hp from '../../utils/HeaderParser'

const GET_UPLOADFILE_LIST_SUCCESS = "GET_UPLOADFILE_LIST_SUCCESS"
const GET_UPLOADFILE_LIST_FAILURE = "GET_UPLOADFILE_LIST_FAILURE"

const state = {
    title : [],
    content : [],
    preference : []

}

const mutations = {
    [GET_UPLOADFILE_LIST_FAILURE](state){
        /*
        state.title = []
        state.content = []
        state.preference = []
        */
    },
    [GET_UPLOADFILE_LIST_SUCCESS](state, response_data){
        //console.log('response_data in mutation', response_data)
        state.content = response_data.files
        //state.preference = response_data.preference
        //state.title = response_data.headers
        state.title = []//response_data.headers
        for (var item in response_data.headers){
            /*
            var d = {}
            d['item'] = response_data.headers[item][0]
            d['displayName'] = response_data.headers[item][1]
            if (response_data.headers.length >= 3){
                //TODO: specify
            }
            state.title.push(d)
            */
            var header = hp.HeaderParser(response_data.headers[item])
//            for (var it in headers){
//            console.log('header in vuex', header)
//            }
            state.title.push(header)
        }
        //console.log(state.title)
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
    uploadfilesTitle : (state) => state.title,
    uploadfilesContent :  (state) => state.content, 
    uploadfilesPreference : (state) => state.preference,
}

const failBack = ({commit, dispatch}, content, mutation=GET_UPLOADFILE_LIST_FAILURE) => {
    console.log('response fail', content)
    commit(mutation, content)
    dispatch('showMsg', '请求失败', 'error')
}

export const getFileList = (store, payload) => {
    var failMessage = "请求失败"
        console.log('getFileList', payload)
    api.getFileList({userid:payload.id}).then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.commit(GET_UPLOADFILE_LIST_SUCCESS, response.data.data)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}

const updateFile = (store, payload) => {
    var failMessage = "更新失败"
    api.updateFile(payload).then(response => {
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
const saveFile = (store, payload) => {
    var failMessage = "添加失败"
    api.saveFile(payload).then(response => {
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
const removeFile = (store, payload) => {
    var failMessage = "删除失败"
    api.removeFile(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '删除成功', 'success')
                store.dispatch('getFileList', payload)
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
/*
const approveFile = (store, payload) => {
    var failMessage = "审批失败"
    api.approveFile(payload).then(response => {
        console.log('save response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                failBack(store, failMessage + response.data.error + response.data.msg)
            }else{
                store.dispatch('showMsg', '审批成功', 'success')
            }
        }else{
            failBack(store, failMessage + response.status + response.statusText)
        }
    }, response => {
        failBack(store, failMessage + response.status + response.statusText)
    })
}
*/

const actions = {
    getFileList,
    updateFile,
    saveFile,
    removeFile,
//    approveFile,
    /*
    getFileList : async ({commit}) => {
        console.log('angel commit in module dispatch')
        //commit()
        const res = await api.getFileList()
        commit('GET_UPLOADFILE_LIST_SUCCESS', res)
    }
    */
}

export default{
    state,
    mutations,
    getters,
    actions
}


