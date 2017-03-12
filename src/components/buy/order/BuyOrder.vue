<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="buyorder" :filterList="labelFilterSet">
            <h3 slot="titlename" align=center> 采购订单管理 </h3>
        </ListView
    </div>
</template>

<script>
import ListView from '../../../utils/ListView.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
    data (){
        return {
            cbSet : {
                get: this.getBuyOrderList,
                update: this.updateBuyOrder,
                save: this.saveBuyOrder,
                remove: this.removeBuyOrder,
                approve: this.approveBuyOrder,
                transfer: this.transferBuyOrder,
            },
            labelFilterSet : [{
                displayName : "待入库",
                filtercb : function(obj) {
                    console.log("obj in buyorder labelFilter cb", obj)
                    return obj && obj.state && obj.state == "审核通过" && obj.total_stored && obj.total_stored != "完全入库"
                },
            }],
        }
    },
    components : {
        ListView
    },
    computed : {
        title() {
            return this.$store.getters.buyOrderTitle
        },
        content() {
            return this.$store.getters.buyOrderContent
        },
        preference() {
            return this.$store.getters.buyOrderPreference
        }


    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.buyOrderList.title.length < 1){
            this.getBuyOrderList()
        }
    },
    methods : {
        getBuyOrderList (){
            this.$store.dispatch('getBuyOrderList')
        },
        updateBuyOrder(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateBuyOrder', content)
            //this.getBuyOrderList()
        },
        saveBuyOrder(content){
            this.$store.dispatch('saveBuyOrder', content)
            //this.getBuyOrderList()
        },
        removeBuyOrder(content){
            this.$store.dispatch('removeBuyOrder', {id:content.id})
            //this.getBuyOrderList()
        },
        approveBuyOrder(content){
            this.$store.dispatch('approveBuyOrder', {id:content.id})
            //this.getBuyOrderList()
        },
        transferBuyOrder(content){
            this.$store.dispatch('transferBuyOrder', {id:content.id})
        },
    },

}
</script>

<style>
</style>

