import api from '../api'
import * as types from './types'

export const getEquipmentList = ({commit}) => {
    api.getEquipmentList().then(response => {
        console.log('response succ', response)
        if (response.status == 200){
            if (response.data.error != 0){
                return commit(types.GET_EQUIPMENT_LIST_FAILURE, response.data.msg)
            }
            commit(types.GET_EQUIPMENT_LIST_SUCCESS, response.data.data)
        }else{
            commit(types.GET_EQUIPMENT_LIST_FAILURE, response.status + response.statusText)
        }
    }, response => {
        console.log('response fail', response)
        commit(types.GET_EQUIPMENT_LIST_FAILURE)
    })
}
