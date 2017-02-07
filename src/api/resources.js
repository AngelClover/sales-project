import Vue from 'vue'
import VueResource from 'vue-resource'
import {API_ROOT} from '../config'
import { getCookie,signOut } from '../utils/authService'

Vue.use(VueResource)

Vue.http.options.crossOrigin = true
Vue.http.options.credentials = true

Vue.http.interceptors.push((request, next)=>{
  // 这里对请求体进行处理
  request.headers = request.headers || {}
  if (getCookie('token')) {
    request.headers.Authorization = 'Basic ' + getCookie('token').replace(/(^\")|(\"$)/g, '')
  }
  next((response) => {
    // 这里可以对响应的结果进行处理
    if (response.status === 401) {
      signOut()
      window.location.pathname = '/login'
    }
  })
})

export const EquipmentResource = Vue.resource(API_ROOT + 'api/equipment')
export const LogEquipmentResource = Vue.resource(API_ROOT + 'api/log/equipment')

export const SourceCompanyResource = Vue.resource(API_ROOT + 'api/sourcecompany')
export const LogSourceCompanyResource = Vue.resource(API_ROOT + 'api/log/sourcecompany')

export const SourceCustomerResource = Vue.resource(API_ROOT + 'api/sourcecustomer')
export const LogSourceCustomerResource = Vue.resource(API_ROOT + 'api/log/sourcecustomer')


export const SaleOrderResource = Vue.resource(API_ROOT + 'api/saleorder')
export const LogSaleOrderResource = Vue.resource(API_ROOT + 'api/log/saleorder')

export const BuyOrderResource = Vue.resource(API_ROOT + 'api/buyorder')
export const LogBuyOrderResource = Vue.resource(API_ROOT + 'api/log/buyorder')


export const StoreHouseResource = Vue.resource(API_ROOT + 'api/storehouse')
export const LogStoreHouseResource = Vue.resource(API_ROOT + 'api/log/storehouse')

export const RepairResource = Vue.resource(API_ROOT + 'api/repair')
export const LogRepairResource = Vue.resource(API_ROOT + 'api/log/repair')

export const LogisticResource = Vue.resource(API_ROOT + 'api/logistic')
export const LogLogisticResource = Vue.resource(API_ROOT + 'api/log/logistic')
//export const UserResource = Vue.resource(API_ROOT + 'users{/id}')
