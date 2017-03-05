<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="repair">
            <h3 slot="titlename" align=center> 维修管理 </h3>
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
            get: this.getRepairList,
            update: this.updateRepair,
            save: this.saveRepair,
            remove: this.removeRepair,
            approve: this.approveRepair
        }
        }
    },
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
        getRepairList (){
            this.$store.dispatch('getRepairList')
        },
        updateRepair(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateRepair', content)
            this.getRepairList()
        },
        saveRepair(content){
            this.$store.dispatch('saveRepair', content)
            this.getRepairList()
        },
        removeRepair(content){
            this.$store.dispatch('removeRepair', {id:content.id})
            this.getRepairList()
        },
        approveRepair(content){
            this.$store.dispatch('approveRepair', {id:content.id})
            this.getRepairList()
        }
    },

}
</script>

<style>
</style>

