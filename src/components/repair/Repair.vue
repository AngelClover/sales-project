<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference>
            <h3 slot="titlename" align=center> 维修管理 </h3>
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
            return this.$store.getters.repairTitle
        },
        content() {
            return this.$store.getters.repairContent
        },
        preference() {
            return this.$store.getters.repairPreference
        }


    },
    created : function(){
        //console.log('created this', this)
        if (this.$store.state.repairList.title.length < 1){
            this.getRepairList()
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
        getRepairList (){
            this.$store.dispatch('getRepairList')
        }
    },

}
</script>

<style>
</style>

