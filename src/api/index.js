import {EquipmentResource, SourceCompanyResource, SourceCustomerResource, SaleOrderResource, BuyOrderResource, StoreHouseResource, RepairResource, LogisticResource} from './resources'
import {LogEquipmentResource, LogSourceCompanyResource, LogSourceCustomerResource, LogSaleOrderResource, LogBuyOrderResource, LogStoreHouseResource, LogRepairResource, LogLogisticResource, FileResource} from './resources'
import {UserResource, AuthResource, PermissionResource} from './resources'

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
        console.log("save equipment", payload)
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
    updateSourceCompany: function(payload){
        return SourceCompanyResource.update({id:payload.id}, payload)
    },
    saveSourceCompany: function(payload){
        return SourceCompanyResource.save(payload)
    },
    approveSourceCompany: function(payload){
        return SourceCompanyResource.get({id:payload.id, action:"approve"},payload)
    },
    removeSourceCompany: function(payload){
        return SourceCompanyResource.remove({id:payload.id})
    },


    //Customer
    getSourceCustomerList: function(){
        return SourceCustomerResource.get()
    },
    updateSourceCustomer: function(payload){
        return SourceCustomerResource.update({id:payload.id}, payload)
    },
    saveSourceCustomer: function(payload){
        return SourceCustomerResource.save(payload)
    },
    approveSourceCustomer: function(payload){
        return SourceCustomerResource.get({id:payload.id, action:"approve"},payload)
    },
    removeSourceCustomer: function(payload){
        return SourceCustomerResource.remove({id:payload.id})
    },

    //SaleOrder
    getSaleOrderList: function() {
        return SaleOrderResource.get()
    },
    updateSaleOrder: function(payload){
        return SaleOrderResource.update({id:payload.id}, payload)
    },
    saveSaleOrder: function(payload){
        return SaleOrderResource.save(payload)
    },
    approveSaleOrder: function(payload){
        return SaleOrderResource.get({id:payload.id, action:"approve"},payload)
    },
    removeSaleOrder: function(payload){
        return SaleOrderResource.remove({id:payload.id})
    },
    transferSaleOrder: function(payload){
        //TODO
    },
    confirmSaleOrder: function(payload){
        return SaleOrderResource.query({id:payload.id, action:"confirm"}, payload)
        //TODO
    },

    //BuyOrder
    getBuyOrderList: function() {
        return BuyOrderResource.get()
    },
    updateBuyOrder: function(payload){
        return BuyOrderResource.update({id:payload.id}, payload)
    },
    saveBuyOrder: function(payload){
        return BuyOrderResource.save(payload)
    },
    approveBuyOrder: function(payload){
        return BuyOrderResource.get({id:payload.id, action:"approve"},payload)
    },
    removeBuyOrder: function(payload){
        return BuyOrderResource.remove({id:payload.id}, payload)
    },
    transferBuyOrder: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"can_store"}, payload)
    },
    //Store
    getStoreHouseList: function() {
        return StoreHouseResource.get()
    },
    updateStoreHouse: function(payload){
        return StoreHouseResource.update({id:payload.id}, payload)
    },
    saveStoreHouse: function(payload){
        return StoreHouseResource.save(payload)
    },
    approveStoreHouse: function(payload){
        return StoreHouseResource.get({id:payload.id, action:"approve"},payload)
    },
    removeStoreHouse: function(payload){
        return StoreHouseResource.remove({id:payload.id})
    },
    receiveInOne: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"receive_one"}, payload)
    },
    inspectInOne: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"inspect_one"}, payload)
    },
    storeInOne: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"store_one"}, payload)
    },
    receiveInAll: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"receive_all"}, payload)
    },
    inspectInAll: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"inspect_all"}, payload)
    },
    storeInAll: function(payload){
        return BuyOrderResource.save({id:payload.id, action:"store_all"}, payload)
    },
    storeOut: function(payload){
        return StoreHouseResource.save({action:"out_store"}, payload)
    },
    storedEquipmentList: function(payload){
        return EquipmentResource.query({action:"get_store", id:payload.id}, payload)
    },
    //Repair
    getRepairList: function() {
        return RepairResource.get()
    },
    updateRepair: function(payload){
        return RepairResource.update({id:payload.id}, payload)
    },
    saveRepair: function(payload){
        return RepairResource.save(payload)
    },
    approveRepair: function(payload){
        return RepairResource.get({id:payload.id, action:"approve"},payload)
    },
    removeRepair: function(payload){
        return RepairResource.remove({id:payload.id})
    },
    //Logistic
    getLogisticList: function() {
        return LogisticResource.get()
    },
    updateLogistic: function(payload){
        return LogisticResource.update({id:payload.id}, payload)
    },
    saveLogistic: function(payload){
        return LogisticResource.save(payload)
    },
    approveLogistic: function(payload){
        return LogisticResource.get({id:payload.id, action:"approve"},payload)
    },
    removeLogistic: function(payload){
        return LogisticResource.remove({id:payload.id})
    },
    //log
    getLogEquipmentList: function() {
        return LogEquipmentResource.get()
    },
    getLogSourceCompany: function() {
        return LogSourceCompanyResource.get()
    },
    getLogSourceCustomer: function(){
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
        return UserResource.update({id:payload.id}, payload)
    },
    getUserInfoList: function(){
        return UserResource.query()
    },
    saveUserInfo: function(payload){
        return UserResource.save(payload)
    },
    removeUserInfo: function(payload){
        return UserResource.remove({id:payload.id})
    },
    getPermissionList: function(){
        return PermissionResource.get()
    },
    addPermission: function(payload){
        return PermissionResource.save({id:payload.id, action:"authorize"}, payload)
    },
    removePermission: function(payload){
        return PermissionResource.save({id:payload.id, action:"unauthorize"}, payload)
    },

    getFileList: function(payload){
        /*TODO: 妈蛋
<<<<<<< HEAD
        console.log('getFileList api', payload)
        return FileResource.get(payload)
=======
        return FileResource.get({params: payload})
>>>>>>> 5fc53220f7a32e867a4df71296a969aac06ca987
*/
        //params decide the data transporting method, using request.args in flask
        console.log('getFileList api', payload)
        return FileResource.get(payload)
    },
    removeFile: function(payload){
        return FileResource.remove({id:payload.id})
    },
    saveFile: function(payload){
        return FileResource.save(payload)
    },
    updateFile: function(payload){
        return FileResource.update(payload)
    },
    

}
