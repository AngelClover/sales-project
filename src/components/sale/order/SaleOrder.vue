<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference>
            <h3 slot="titlename" align=center> 销售订单管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../../utils/ListView.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
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
        }


    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.saleOrderList.title.length < 1){
            this.getSaleOrderList()
        }
    },
    methods : {
        createContent : (title, suffix)=>{
            var ret = {}
            for (var item in title){
                ret[item] = title[item] + suffix
            }
            return ret
        },
        getSaleOrderList (){
            this.$store.dispatch('getSaleOrderList')
        }
    },

}
</script>

<style>
</style>

