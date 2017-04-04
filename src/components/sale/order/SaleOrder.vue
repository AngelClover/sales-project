<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="saleorder" :subtitle=subtitle>
            <h3 slot="titlename" align=center> 销售订单管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../../utils/ListView.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
    data (){
        return {
            cbSet : {
            get: this.getSaleOrderList,
            update: this.updateSaleOrder,
            save: this.saveSaleOrder,
            remove: this.removeSaleOrder,
            approve: this.approveSaleOrder
        }
        }
    },
    components : {
        ListView
    },
    computed : {
        title() {
            return this.$store.getters.saleOrderTitle
        },
        content() {
            return this.$store.getters.saleOrderContent
        },
        preference() {
            return this.$store.getters.saleOrderPreference
        },
        subtitle() {
            return this.$store.getters.saleOrderSubtitle
        }
    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.saleOrderList.title.length < 1){
            this.getSaleOrderList()
        }
    },
    methods : {
        getSaleOrderList (){
            this.$store.dispatch('getSaleOrderList')
        },
        updateSaleOrder(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateSaleOrder', content)
            this.getSaleOrderList()
        },
        saveSaleOrder(content){
            this.$store.dispatch('saveSaleOrder', content)
            this.getSaleOrderList()
        },
        removeSaleOrder(content){
            this.$store.dispatch('removeSaleOrder', {id:content.id})
            this.getSaleOrderList()
        },
        approveSaleOrder(content){
            this.$store.dispatch('approveSaleOrder', {id:content.id})
            this.getSaleOrderList()
        },
        confirmSaleOrder(content){
            this.$store.dispatch('confirmSaleOrder', {id:content.id})
            this.getSaleOrderList()
        },
    },

}
</script>

<style>
</style>

