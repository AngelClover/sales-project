<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference >
        <h3 slot="titlename" align=center> 首营公司管理 </h3>
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
            return this.$store.getters.sourceCompanyTitle
        },
        content() {
            return this.$store.getters.sourceCompanyContent
        },
        preference() {
            return this.$store.getters.sourceCompanyPreference
        }


    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.sourceCompanyList.title.length < 1){
            this.getSourceCompanyList()
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
        getSourceCompanyList (){
            this.$store.dispatch('getSourceCompanyList')
        }
    },

}
</script>

<style>
</style>

