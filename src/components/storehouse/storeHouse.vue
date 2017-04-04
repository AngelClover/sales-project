<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="storehouse" stores="storeForEquipment" :filterList="labelFilterSet">
            <h3 slot="titlename" align=center> 仓库管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../utils/ListView.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
    data (){
        return {
            cbSet : {
                get: this.getStoreHouseList,
                update: this.updateStoreHouse,
                save: this.saveStoreHouse,
                remove: this.removeStoreHouse,
                approve: this.approveStoreHouse
            },
            labelFilterSet : [
            {
                displayName : "一月过期提醒",
                filtercb : function(obj){
                    if (typeof(obj) != undefined && typeof(obj.bad_date) != undefined && obj.bad_date != "NULL"){
                        var d = Date.parse(obj.bad_date)
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
                    if (typeof(obj) && typeof(obj.bad_date) && obj.bad_date != "NULL"){
                        var d = Date.parse(obj.bad_date)
                        var now = new Date()
                        if (d < now)return true
                    }
                    return false
                },
            },
            {
                displayName : "在库列表(数字不为0)",
                filtercb : function(obj){
                    //console.log('filter', obj.store_number, obj && obj.store_number && obj.store_numer > 0, obj&& obj.store_number, obj.store_number > 0)
                    if (typeof(obj) != undefined && typeof(obj.store_number) != undefined)return obj.store_number > 0
                    //return obj && obj.store_number && obj.store_numer > 0
                },
            },
                ],
        }
    },
    components : {
        ListView
    },
    computed : {
        title() {
            return this.$store.getters.storeHouseTitle
        },
        content() {
            return this.$store.getters.storeHouseContent
        },
        preference() {
            return this.$store.getters.storeHousePreference
        },
        storeForEquipment(){
            console.log("store for equipment in storehouse", this.$store.getters.inStore);
            return this.$store.getters.inStore
        },

    },
    created : function(){
        //console.log('created this', this)
        if (this.$store.state.storeHouseList.title.length < 1){
            this.getStoreHouseList()
        }
    },
    methods : {
        getStoreHouseList (){
            this.$store.dispatch('getStoreHouseList')
        },
        updateStoreHouse(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateStoreHouse', content)
            this.getStoreHouseList()
        },
        saveStoreHouse(content){
            this.$store.dispatch('saveStoreHouse', content)
            this.getStoreHouseList()
        },
        removeStoreHouse(content){
            this.$store.dispatch('removeStoreHouse', {id:content.id})
            this.getStoreHouseList()
        },
        approveStoreHouse(content){
            this.$store.dispatch('approveStoreHouse', {id:content.id})
            this.getStoreHouseList()
        }
    },

}
</script>

<style>
</style>

