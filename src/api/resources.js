import Vue from 'vue'
import VueResource from 'vue-resource'
import {API_ROOT} from '../config'
import { getCookie,signOut } from '../utils/authService'

Vue.use(VueResource)

Vue.http.options.crossOrigin = true
//Vue.http.options.credentials = true

Vue.http.interceptors.push((request, next)=>{
  // 这里对请求体进行处理
  request.headers = request.headers || {}
  var authString = localStorage.getItem('AuthString')
  if (getCookie('token')) {
      //var str = localStorage.getItem('TestAuth', str)
    var str = 'Basic ' + window.btoa(getCookie('token') + ":")
    //request.headers.set('Authorization', 'Basic ' + getCookie('token').replace(/(^\")|(\"$)/g, ''))
    //request.headers.set('Authorization', 'Basic ' + getCookie('token').replace(/(^\")|(\"$)/g, ''))
    request.headers.set('Authorization', str)
      console.log('use token', str)
  }else if (authString){
      var str = 'Basic ' + authString
      localStorage.setItem('TestAuth', str)
      request.headers.set('Authorization', 'Basic ' + authString)
      //localStorage.removeItem('AuthString')
      console.log('remove auth string')
  }else {
      console.log('p isn\'t there')
  }
  console.log('request headers', request.headers)
  next((response) => {
    console.log('login status', response.status)
    // 这里可以对响应的结果进行处理
    if (response.status === 401) {
      signOut()
      window.location.pathname = '/login'
    }
  })
})
//when change here, think about the hardcode in upload components
const apiBase = 'api/v1.0/'

export const EquipmentResource = Vue.resource(API_ROOT + apiBase + 'equipment{/action}{/id}')
export const LogEquipmentResource = Vue.resource(API_ROOT + apiBase + 'log/equipment')

export const SourceCompanyResource = Vue.resource(API_ROOT + apiBase + 'enterprise{/action}{/id}')
export const LogSourceCompanyResource = Vue.resource(API_ROOT + apiBase + 'log/sourcecompany')

export const SourceCustomerResource = Vue.resource(API_ROOT + apiBase + 'customer{/action}{/id}')
export const LogSourceCustomerResource = Vue.resource(API_ROOT + apiBase + 'log/customer')


export const SaleOrderResource = Vue.resource(API_ROOT + apiBase + 'sale{/action}{/id}')
export const LogSaleOrderResource = Vue.resource(API_ROOT + apiBase + 'log/saleorder')

export const BuyOrderResource = Vue.resource(API_ROOT + apiBase + 'purchase{/action}{/id}')
export const LogBuyOrderResource = Vue.resource(API_ROOT + apiBase + 'log/buyorder')


export const StoreHouseResource = Vue.resource(API_ROOT + apiBase + 'store{/action}{/id}')
export const LogStoreHouseResource = Vue.resource(API_ROOT + apiBase + 'log/storehouse')

export const RepairResource = Vue.resource(API_ROOT + apiBase + 'repair{/action}{/id}')
export const LogRepairResource = Vue.resource(API_ROOT + apiBase + 'log/repair')

export const LogisticResource = Vue.resource(API_ROOT + apiBase + 'logistic{/action}{/id}')
export const LogLogisticResource = Vue.resource(API_ROOT + apiBase + 'log/logistic')

export const AuthResource = Vue.resource(API_ROOT + apiBase + 'auth')
export const UserResource = Vue.resource(API_ROOT + apiBase + 'users{/id}')

export const PermissionResource = Vue.resource(API_ROOT + apiBase + 'permission{/action}{/id}')

export const FileResource = Vue.resource(API_ROOT + apiBase + 'upload{/id}')


