<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference :cbset=cbSet location="logistic">
            <h3 slot="titlename" align=center> 物流管理 </h3>
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
            get: this.getLogisticList,
            update: this.updateLogistic,
            save: this.saveLogistic,
            remove: this.removeLogistic,
            approve: this.approveLogistic
        }
        }
    },
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
        getLogisticList (){
            this.$store.dispatch('getLogisticList')
        },
        updateLogistic(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateLogistic', content)
            this.getLogisticList()
        },
        saveLogistic(content){
            this.$store.dispatch('saveLogistic', content)
            this.getLogisticList()
        },
        removeLogistic(content){
            this.$store.dispatch('removeLogistic', {id:content.id})
            this.getLogisticList()
        },
        approveLogistic(content){
            this.$store.dispatch('approveLogistic', {id:content.id})
            this.getLogisticList()
        }
    },

}
</script>

<style>
</style>

