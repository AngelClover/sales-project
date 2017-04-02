<template>
    <div>
        <ListView msg="asd" :title=title :content=content :pref=preference  :cbset=cbSet location="equipment">
            <h3 slot="titlename" align=center> 首营设备管理 </h3>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../../utils/ListView.vue'
//import api from '../../../api'
//import { getEquipmentList } from '../../../vuex/actions'
import { mapGetters, mapActions } from 'vuex'
export default {
    data (){
        return {
            cbSet : {
                get: this.getEquipmentList,
                update: this.updateEquipment,
                save: this.saveEquipment,
                remove: this.removeEquipment,
                approve: this.approveEquipment
            }
        }
    },
    components : {
        ListView
    },
    computed : {
        title() {
            return this.$store.getters.equipmentTitle
        },
        content() {
            return this.$store.getters.equipmentContent
        },
        preference() {
            return this.$store.getters.equipmentPreference
        }
    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.equipmentList.title.length < 1){
            this.getEquipmentList()
        }
    },
    methods : {
        getEquipmentList (){
            this.$store.dispatch('getEquipmentList')
        },
        updateEquipment(content){
            //console.log('save equipment', content)
            this.$store.dispatch('updateEquipment', content)
            this.getEquipmentList()
        },
        saveEquipment(content){
            this.$store.dispatch('saveEquipment', content)
            this.getEquipmentList()
        },
        removeEquipment(content){
            this.$store.dispatch('removeEquipment', {id:content.id})
            this.getEquipmentList()
        },
        approveEquipment(content){
            this.$store.dispatch('approveEquipment', {id:content.id})
            this.getEquipmentList()
        }
    },

}
</script>

<style>
</style>

