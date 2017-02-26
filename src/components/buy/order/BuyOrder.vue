<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="buyorder">
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
            approve: this.approveBuyOrder
        }
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
            this.getBuyOrderList()
        },
        saveBuyOrder(content){
            this.$store.dispatch('saveBuyOrder', content)
            this.getBuyOrderList()
        },
        removeBuyOrder(content){
            this.$store.dispatch('removeBuyOrder', {id:content.id})
            this.getBuyOrderList()
        },
        approveBuyOrder(content){
            this.$store.dispatch('approveBuyOrder', {id:content.id})
            this.getBuyOrderList()
        }
    },

}
</script>

<style>
</style>

