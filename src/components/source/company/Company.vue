<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="sourcecompany">
        <h3 slot="titlename" align=center> 首营公司管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from './ListView.vue'
//import api from '../../../api'
//import { getEquipmentList } from '../../../vuex/actions'
import { mapGetters, mapActions } from 'vuex'
export default {
    data (){
        return {
            cbSet : {
            get: this.getSourceCompanyList,
            update: this.updateSourceCompany,
            save: this.saveSourceCompany,
            remove: this.removeSourceCompany,
            approve: this.approveSourceCompany
        }
        }
    },
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
        getSourceCompanyList (){
            this.$store.dispatch('getSourceCompanyList')
        },
        updateSourceCompany(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateSourceCompany', content)
            this.getSourceCompanyList()
        },
        saveSourceCompany(content){
            this.$store.dispatch('saveSourceCompany', content)
            this.getSourceCompanyList()
        },
        removeSourceCompany(content){
            this.$store.dispatch('removeSourceCompany', {id:content.id})
            this.getSourceCompanyList()
        },
        approveSourceCompany(content){
            this.$store.dispatch('approveSourceCompany', {id:content.id})
            this.getSourceCompanyList()
        }
    },

}
</script>

<style>
</style>

