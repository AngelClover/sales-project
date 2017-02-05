import Vue from 'vue'
import Vuex from 'vuex'
import equipmentList from './modules/equipment.list'
import sourceCompanyList from './modules/source.company.list'
import sourceCustomerList from './modules/source.customer.list'
import saleOrderList from './modules/saleorder.list'
import buyOrderList from './modules/buyorder.list'
//import {getEquipmentList} from './actions'

const debug = process.env.NODE_ENV !== 'production'
Vue.use(Vuex)
//Vue.config.debug = debug
//Vue.config.warnExpressionErrors = false
console.log("vuex store")
console.log("equip list", equipmentList)

export default new Vuex.Store({
    modules: {
        equipmentList,
        sourceCompanyList,
        sourceCustomerList,
        saleOrderList,
        buyOrderList
    },
    //middlewares,
    strict : debug,
    //actions : { getEquipmentList, }


})
