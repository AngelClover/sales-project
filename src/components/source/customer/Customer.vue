<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference >
        <h3 slot="titlename" align=center> 首营客户管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../../utils/ListView.vue'
//import api from '../../../api'
//import { getEquipmentList } from '../../../vuex/actions'
import { mapGetters, mapActions } from 'vuex'
export default {
    components : {
        ListView
    },
    computed : {
        title() {
            return this.$store.getters.sourceCustomerTitle
        },
        content() {
            return this.$store.getters.sourceCustomerContent
        },
        preference() {
            return this.$store.getters.sourceCustomerPreference
        }


    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.sourceCustomerList.title.length < 1){
            this.getCustomerList()
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
        getCustomerList (){
            this.$store.dispatch('getSourceCustomerList')
        }
    },

}
</script>

<style>
</style>

