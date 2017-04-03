<template>
    <Modal v-model="showCC" @on-cancel="$emit('close')">
        <div slot="header">
            <h2>
            <center>
            <div class="detail-header" >
                新建
            </div>
            </center>
            </h2>
        </div>
        <div class="detail-body">
            <table>
                <tbody>
                    <tr v-for="(v, key) in detailTitle">
                        <td>{{v.displayName}}</td>
                        <td>
                            <advancedInputer v-model="newContent[v.item]" :header=v>
                            </advancedInputer>
                        <!--
                            <input v-model=newContent[value.item]>
                            </input>
                        -->
                        </td>
                    </tr>
                </tbody>
            </table>
            <EquipCreator :subtitle=detailSubtitle v-model=newContent.equipments v-if="location=='buyorder'">
            </EquipCreator>
            
        </div>
        <div slot="footer">
            <center>
                <button class="ui secondary button" @click="newContent={};$emit('close');">
                放弃
            </button>
            <button class="ui primary button" @click="realCreate">
                新建
            </button>
            </center>
        </div>
    </Modal>
</template>

<script>
import api from '../api'
import utils from './utils'
import OutSelector from './outSelector.vue'
import advancedInputer from './advancedInputer.vue'
import EquipCreator from './EquipCreator.vue'
export default {
    components : {
        OutSelector,
        advancedInputer,
        EquipCreator,
    },
    data: function() {
        return {
            showOutStore : false,
            newContent : {},
            //showCC : false,
        }
    },
    props : ['detailTitle', 'cbset', 'stores', 'location', 'detailContent', 'showCreator', 'detailSubtitle'],
    computed : {
        showCC (){
            return this.showCreator
        }
    },
    methods : {
        realCreate(){
            //console.log("!!!!", this.newContent, this.detailContent)
            //console.log("!!!!", this.cmp(this.newContent, this.detailContent))
            //console.log('real creator', this.newContent)
            if (this.cmp(this.newContent, this.detailContent)){
                this.$store.dispatch('showMsg', '无修改新建', 'info')
                //this.closeModifier()
            }else{
                console.log("!!!!", this.newContent, this.detailContent)
                //this.showContent = true
                this.cbset.save(this.newContent)
                //this.closeModifier()
            }
        },
        cmp : function( x, y ) {  
            return utils.cmp(x, y)
        },
    }
}
</script>

<style>
</style>

