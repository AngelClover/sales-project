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
  var authString = localStorage.getItem('AuthString')
  if (authString){
      request.headers.set('Authorization', 'Basic ' + authString)
      localStorage.removeItem('AuthString')
  }else if (getCookie('token')) {
    request.headers.set('Authorization', 'Basic ' + getCookie('token').replace(/(^\")|(\"$)/g, ''))
  }
  console.log('request headers', request.headers)
  next((response) => {
    // 这里可以对响应的结果进行处理
    if (response.status === 401) {
      signOut()
      window.location.pathname = '/login'
    }
  })
})
const apiBase = 'api/v1.0/'

export const EquipmentResource = Vue.resource(API_ROOT + apiBase + 'equipment{/id}')
export const LogEquipmentResource = Vue.resource(API_ROOT + apiBase + 'log/equipment')

export const SourceCompanyResource = Vue.resource(API_ROOT + apiBase + 'sourcecompany')
export const LogSourceCompanyResource = Vue.resource(API_ROOT + apiBase + 'log/sourcecompany')

export const SourceCustomerResource = Vue.resource(API_ROOT + apiBase + 'sourcecustomer')
export const LogSourceCustomerResource = Vue.resource(API_ROOT + apiBase + 'log/sourcecustomer')


export const SaleOrderResource = Vue.resource(API_ROOT + apiBase + 'saleorder')
export const LogSaleOrderResource = Vue.resource(API_ROOT + apiBase + 'log/saleorder')

export const BuyOrderResource = Vue.resource(API_ROOT + apiBase + 'buyorder')
export const LogBuyOrderResource = Vue.resource(API_ROOT + apiBase + 'log/buyorder')


export const StoreHouseResource = Vue.resource(API_ROOT + apiBase + 'storehouse')
export const LogStoreHouseResource = Vue.resource(API_ROOT + apiBase + 'log/storehouse')

export const RepairResource = Vue.resource(API_ROOT + apiBase + 'repair')
export const LogRepairResource = Vue.resource(API_ROOT + apiBase + 'log/repair')

export const LogisticResource = Vue.resource(API_ROOT + apiBase + 'logistic')
export const LogLogisticResource = Vue.resource(API_ROOT + apiBase + 'log/logistic')

export const AuthResource = Vue.resource(API_ROOT + apiBase + 'auth')
export const UserResource = Vue.resource(API_ROOT + apiBase + 'user{/id}')


