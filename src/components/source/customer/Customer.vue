<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="custemor" :filterList="labelFilterSet">
        <h3 slot="titlename" align=center> 客户管理 </h3>
        </ListView>
    </div>
</template>

<script>
//import ListView from '../../../utils/ListView.vue'
import ListView from './ListView.vue'
//import api from '../../../api'
//import { getEquipmentList } from '../../../vuex/actions'
import { mapGetters, mapActions } from 'vuex'
export default {
    data (){
        return {
            cbSet : {
            get: this.getSourceCustomerList,
            update: this.updateSourceCustomer,
            save: this.saveSourceCustomer,
            remove: this.removeSourceCustomer,
            approve: this.approveSourceCustomer
            },
            labelFilterSet : [
            {
                displayName : "一月过期提醒",
                filtercb : function(obj){
                    if (typeof(obj) != undefined && typeof(obj['产品注册证到期日']) != undefined && obj['产品注册证到期日'] != "NULL"){
                        var d = Date.parse(obj['产品注册证到期日'])
                        var now = new Date()
                        var future = new Date().setMonth((new Date().getMonth()-1))
                        if (now <= d && d <= future)return true
                    }
                    return false
                },
            },
            {
                displayName : "过期提醒",
                filtercb : function(obj){
                    if (typeof(obj) != undefined && typeof(obj['产品注册证到期日期']) != undefined && obj['产品注册证到期日期'] != "NULL"){
                        var d = Date.parse(obj['产品注册证到期日期'])
                        var now = new Date()
                        //var future = new Date().setMonth((new Date().getMonth()-1))
                        if (d <= now)return true
                    }
                    return false
                },
            }
            ]
        }
    },
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
        },
        updateSourceCustomer(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateSourceCustomer', content)
            this.getSourceCustomerList()
        },
        saveSourceCustomer(content){
            this.$store.dispatch('saveSourceCustomer', content)
            this.getSourceCustomerList()
        },
        removeSourceCustomer(content){
            this.$store.dispatch('removeSourceCustomer', {id:content.id})
            this.getSourceCustomerList()
        },
        approveSourceCustomer(content){
            this.$store.dispatch('approveSourceCustomer', {id:content.id})
            this.getSourceCustomerList()
        }
    },

}
</script>

<style>
</style>

