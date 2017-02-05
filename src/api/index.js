import {EquipmentResource, SourceCompanyResource, SourceCustomerResource, SaleOrderResource, BuyOrderResource} from './resources'

export default {
    getEquipmentList: function() {
        return EquipmentResource.get()
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
    }
}
