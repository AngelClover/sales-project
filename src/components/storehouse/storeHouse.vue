<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference>
            <h3 slot="titlename" align=center> 仓库管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../utils/ListView.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
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
        createContent : (title, suffix)=>{
            var ret = {}
            for (var item in title){
                ret[item] = title[item] + suffix
            }
            return ret
        },
        getStoreHouseList (){
            this.$store.dispatch('getStoreHouseList')
        }
    },

}
</script>

<style>
</style>

