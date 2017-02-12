const SHOW_MSG = "SHOW_MSG"
const HIDE_MSG = "HIDE_MSG"

const state = {
    message : {
        content : '',
        type : '',
        place : '',
        title : ''
    }
}

const mutations = {
    [SHOW_MSG](state, action){
        state.message = {...action}
        console.log('show_MSG', state.message)
    },
    [HIDE_MSG](state, action){
        state.message = {
            type : '',
            content : '',
            title : '',
            place : ''
        }
    }
}

const getters = {
    getMessage : (state) => {
        console.log('msg getters', state.message)
        return state.message
    }
}

export const showMsg = ({commit}, content, type='error', place='bottom right', title='') => {
    console.log('action showmsg', content, type, place)
    commit(SHOW_MSG, {content, type, place, title})
}

export const hideMsg = ({commit}) => {
    commit(HIDE_MSG)
}

const actions = {
    showMsg,
    hideMsg
}

export default {
    state,
    mutations,
    actions,
    getters,
}
