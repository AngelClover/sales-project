<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="storehouse">
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
        }
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
        }


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

