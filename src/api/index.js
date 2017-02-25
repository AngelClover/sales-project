import {EquipmentResource, SourceCompanyResource, SourceCustomerResource, SaleOrderResource, BuyOrderResource, StoreHouseResource, RepairResource, LogisticResource} from './resources'
import {LogEquipmentResource, LogSourceCompanyResource, LogSourceCustomerResource, LogSaleOrderResource, LogBuyOrderResource, LogStoreHouseResource, LogRepairResource, LogLogisticResource} from './resources'
import {UserResource, AuthResource} from './resources'

export default {
    //Equipment
    getEquipmentList: function() {
        return EquipmentResource.get()
    },
    updateEquipment: function(payload) {
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
        return EquipmentResource.remove({id:payload.id})
    },

    //SourceCompany
    getSourceCompanyList: function() {
        return SourceCompanyResource.get()
    },
    updateSourceCompanyList: function(payload){
        return SourceCompany.update({id:payload.id}, payload)
    },
    saveSourceCompanyList: function(payload){
        return SourceCompany.save(payload)
    },
    approveSourceCompanyList: function(payload){
        return SourceCompany.get({id:payload.id, action:"approve"},payload)
    },
    removeSourceCompany: function(){
        return SourceCompany.remove({id:payload.id})
    },


    //Customer
    getSourceCustomerList: function(){
        return SourceCustomerResource.get()
    },

    //SaleOrder
    getSaleOrderList: function() {
        return SaleOrderResource.get()
    },
    updateSaleOrderList: function(payload){
        return SaleOrderResource.update({id:payload.id}, payload)
    },
    saveSaleOrderList: function(payload){
        return SaleOrderResource.save(payload)
    },
    approveSaleOrderList: function(payload){
        return SaleOrderResource.get({id:payload.id, action:"approve"},payload)
    },
    removeSaleOrder: function(){
        return SaleOrderResource.remove({id:payload.id})
    },

    //BuyOrder
    getBuyOrderList: function() {
        return BuyOrderResource.get()
    },
    updateBuyOrderList: function(payload){
        return BuyOrderResource.update({id:payload.id}, payload)
    },
    saveBuyOrderList: function(payload){
        return BuyOrderResource.save(payload)
    },
    approveBuyOrderList: function(payload){
        return BuyOrderResource.get({id:payload.id, action:"approve"},payload)
    },
    removeBuyOrder: function(){
        return BuyOrderResource.remove({id:payload.id})
    },
    //Store
    getStoreHouseList: function() {
        return StoreHouseResource.get()
    },
    updateStoreHouseList: function(payload){
        return StoreHouse.update({id:payload.id}, payload)
    },
    saveStoreHouseList: function(payload){
        return StoreHouse.save(payload)
    },
    approveStoreHouseList: function(payload){
        return StoreHouse.get({id:payload.id, action:"approve"},payload)
    },
    removeStoreHouse: function(){
        return StoreHouse.remove({id:payload.id})
    },
    //Repair
    getRepairList: function() {
        return RepairResource.get()
    },
    updateRepairList: function(payload){
        return Repair.update({id:payload.id}, payload)
    },
    saveRepairList: function(payload){
        return Repair.save(payload)
    },
    approveRepairList: function(payload){
        return Repair.get({id:payload.id, action:"approve"},payload)
    },
    removeRepair: function(){
        return Repair.remove({id:payload.id})
    },
    //Logistic
    getLogisticList: function() {
        return LogisticResource.get()
    },
    updateLogisticList: function(payload){
        return Logistic.update({id:payload.id}, payload)
    },
    saveLogisticList: function(payload){
        return Logistic.save(payload)
    },
    approveLogisticList: function(payload){
        return Logistic.get({id:payload.id, action:"approve"},payload)
    },
    removeLogistic: function(){
        return Logistic.remove({id:payload.id})
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
