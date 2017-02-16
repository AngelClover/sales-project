import Vue from 'vue'
import Vuex from 'vuex'
import equipmentList from './modules/equipment.list'
import sourceCompanyList from './modules/source.company.list'
import sourceCustomerList from './modules/source.customer.list'
import saleOrderList from './modules/saleorder.list'
import buyOrderList from './modules/buyorder.list'
import storeHouseList from './modules/storehouse.list'
import repairList from './modules/repair.list'
import logisticList from './modules/logistic.list'
import auth from './modules/auth'
import msg from './modules/toast'
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
        buyOrderList,
        storeHouseList,
        repairList,
        logisticList,
        auth,
        msg
    },
    //middlewares,
    strict : debug,
    //actions : { getEquipmentList, }


})
