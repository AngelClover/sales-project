<template>
    <Modal v-model="showCreator">
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
            <div v-if="location == 'buyorder'">
                buyorder
            </div>
        </div>
        <div slot="footer">
            <center>
            <button class="ui secondary button" @click="$emit('close')">
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
export default {
    components : {
        OutSelector,
        advancedInputer,
    },
    data: function() {
        return {
            showOutStore : false,
            newContent : {}
        }
    },
    props : ['detailTitle', 'cbset', 'stores', 'location', 'detailContent', 'showCreator'],
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

