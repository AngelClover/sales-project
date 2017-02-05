<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference>
            <h3 slot="titlename" align=center> 物流管理 </h3>
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
            return this.$store.getters.logisticTitle
        },
        content() {
            return this.$store.getters.logisticContent
        },
        preference() {
            return this.$store.getters.logisticPreference
        }


    },
    created : function(){
        //console.log('created this', this)
        if (this.$store.state.logisticList.title.length < 1){
            this.getLogisticList()
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
        getLogisticList (){
            this.$store.dispatch('getLogisticList')
        }
    },

}
</script>

<style>
</style>

