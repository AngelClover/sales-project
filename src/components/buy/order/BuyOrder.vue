<template>
    <div>
        <!-- "separate BuyDetail from BuyListView's modal" : 
            add buyDetail
            add v-if to BuyListView
            add v-else to buyDetail
            add @clickShowDetail="openDetail" to BuyListView
        by CHEN 17.6.6 -->
        <BuyListView v-if="!showDetail" msg="asd" :title="title" :content="content" :pref="preference" :cbset="cbSet" location="buyorder" :filterList="labelFilterSet" :subtitle="subtitle" @clickShowDetail="openDetail">
            <h3 slot="titlename" align="center"> 采购订单管理 </h3>
        </BuyListView>

        <!-- whats this ?  :storeForEquipment="stores" -->
        <!-- "separate BuyDetail from BuyListView's modal" :
            add buyDetail here
        by CHEN 17.6.6 -->
        <buyDetail v-else showDetails="true" :detailTitle="title" :detailContent="detailContent" :cbset="cbSet" location="buyorder" :detailSubtitle="subtitle" @close="closeDetail">
            <h3 slot="titlename" align="center"> 订单详情管理 </h3>
        </buyDetail>
    </div>
</template>

<script>
import BuyListView from './buyListView.vue'
import { mapGetters, mapActions } from 'vuex'
import BuyDetail from './buyDetail.vue'
export default {
    data: function() {
        return {
            cbSet : {
                get: this.getBuyOrderList,
                update: this.updateBuyOrder,
                save: this.saveBuyOrder,
                remove: this.removeBuyOrder,
                approve: this.approveBuyOrder,
                transfer: this.transferBuyOrder,
                receiveInAll: this.receiveInAllBuyOrder,
                inspectInAll: this.inspectInAllBuyOrder,
                storeInAll: this.storeInAllBuyOrder,
                receiveInOne: this.receiveInOneBuyOrder,
                inspectInOne: this.inspectInOneBuyOrder,
                storeInOne: this.storeInOneBuyOrder,
            },
            labelFilterSet : [
                {
                    displayName : "待审批",
                    filtercb : function(obj) {
                        return obj && obj.state && obj.state == "待审核" 
                    },
                },
                {
                    displayName : "待采购",
                    filtercb : function(obj) {
                        return obj && obj.state && obj.state == "审核通过" 
                    },
                },
                {
                    displayName : "待入库",
                    filtercb : function(obj) {
                        return obj && obj.state && obj.state == "待入库"
                    },
                },
                {
                    displayName : "已入库",
                    filtercb : function(obj) {
                        return obj && obj.state && obj.state == "已入库" 
                    },
                }
            ],
            //---- "separate BuyDetail from BuyListView's modal" : 
            showDetail : false, //define whether show buyDetail
            detailContent : {} //pass on the content should show
            //---- by CHEN 17.6.6
        }
    },
    components : {
        BuyListView,
        BuyDetail
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
        },
        subtitle() {
            return this.$store.getters.buyOrderSubtitle
        },
    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.buyOrderList.title.length < 1){
            this.getBuyOrderList()
        }
        if (this.$store.state.sourceCompanyList.title.length < 1){
//            this.$store.dispatch('getSourceCompanyList')
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
        receiveInAllBuyOrder(content){
            this.$store.dispatch('receiveInAllBuyOrder', content)
        },
        inspectInAllBuyOrder(content){
            this.$store.dispatch('inspectInAllBuyOrder', content)
        },
        storeInAllBuyOrder(content){
            this.$store.dispatch('storeInAllBuyOrder', content)
        },
        receiveInOneBuyOrder(content){
            this.$store.dispatch('receiveInOneBuyOrder', content)
        },
        inspectInOneBuyOrder(content){
            this.$store.dispatch('inspectInOneBuyOrder', content)
        },
        storeInOneBuyOrder(content){
            this.$store.dispatch('storeInOneBuyOrder', content)
        },
        //---- "separate BuyDetail from BuyListView's modal" : add openDetail, to respond to clickShowDetail-event
        openDetail : function(content) {
            this.showDetail = true
            this.detailContent = content
            //console.log('CHEN', "this.detailContent", this.detailContent)
        },
        //---- by CHEN 17.6.6
        //---- "separate BuyDetail from BuyListView's modal" : add closeDetail, to respond to detail-page's close-event
        closeDetail : function() {
            this.showDetail = false
            this.detailContent = null
        }
        //---- by CHEN 17.6.15
    },

}
</script>

<style>
</style>

