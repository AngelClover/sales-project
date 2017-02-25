import {EquipmentResource, SourceCompanyResource, SourceCustomerResource, SaleOrderResource, BuyOrderResource, StoreHouseResource, RepairResource, LogisticResource} from './resources'
import {LogEquipmentResource, LogSourceCompanyResource, LogSourceCustomerResource, LogSaleOrderResource, LogBuyOrderResource, LogStoreHouseResource, LogRepairResource, LogLogisticResource} from './resources'
import {UserResource, AuthResource} from './resources'

export default {
    getEquipmentList: function() {
        return EquipmentResource.get()
    },
    updateEquipment: function(payload) {
        console.log('update', payload, payload.id)
        return EquipmentResource.update({id:payload.id}, payload)
    },
    saveEquipment: function(payload) {
        //TODO: api need uri but how to get uri
        //this will be right?
        return EquipmentResource.save(payload)
    },
    approveEquipment: function(payload) {
        return EquipmentResource.get({id:payload.id, action:"approve"}, payload)
    },
    removeEquipment: function(payload) {
        return EquipmentResource.remove({id:payload})
    },

    getSourceCompanyList: function() {
        return SourceCompanyResource.get()
    },
    getSourceCustomerList: function(){
        return SourceCustomerResource.get()
    },
    getSaleOrderList: function(){
        return SaleOrderResource.get()
    },
    getBuyOrderList: function(){
        return BuyOrderResource.get()
    },
    getStoreHouseList: function(){
        return StoreHouseResource.get()
    },
    getRepairList: function(){
        return RepairResource.get()
    },
    getLogisticList: function(){
        return LogisticResource.get()
    },
    //log
    getLogEquipmentList: function() {
        return LogEquipmentResource.get()
    },
    getLogSourceCompanyList: function() {
        return LogSourceCompanyResource.get()
    },
    getLogSourceCustomerList: function(){
        return LogSourceCustomerResource.get()
    },
    getLogSaleOrderList: function(){
        return LogSaleOrderResource.get()
    },
    getLogBuyOrderList: function(){
        return LogBuyOrderResource.get()
    },
    getLogStoreHouseList: function(){
        return LogStoreHouseResource.get()
    },
    getLogRepairList: function(){
        return LogRepairResource.get()
    },
    getLogLogisticList: function(){
        return LogLogisticResource.get()
    },
    //auth
    getMe: function(){
        return UserResource.get({id:'me'})
    },
    /*
    Login: function(payload){
        return AuthResource.save(payload)
    },
    */
    register: function(payload){
        return UserResource.save(payload)
    },
    getToken: function(body){
        return UserResource.get({id:'login_token'})
    },
    updateUserInfo: function(payload){
        console.log('api payload', payload)
        return UserResource.update({id:payload.username}, payload)
    },
    getUserList: function(){
        return UserResource.query()
    }

}
