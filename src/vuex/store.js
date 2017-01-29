import Vue from 'vue'
import Vuex from 'vuex'
import equipmentList from './modules/equipment.list'
import {getEquipmentList} from './actions'

const debug = process.env.NODE_ENV !== 'production'
Vue.use(Vuex)
//Vue.config.debug = debug
//Vue.config.warnExpressionErrors = false
console.log("vuex store")
console.log("equip list", equipmentList)

export default new Vuex.Store({
    modules: {
        equipmentList
    },
    //middlewares,
    strict : debug,
    actions : {
        getEquipmentList,
    }


})
