<template>
    <Modal v-model="showMM" @on-cancel="$emit('close')" @on-ok="$emit('close')">
        <div slot="header">
            <h2>
            <center>
            <div class="detail-header" >
                修改
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
            <button class="ui primary button" @click="realModify" >
                修改
            </button>
            </center>
        </div>
        <OutSelector :showOutStore=showOutStore :outContent=detailContent @close="showOutStore=false;" :stores=stores>
        </OutSelector>
    </Modal>
</template>

<script>
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
        }
    },
    props : ['detailTitle', 'cbset', 'stores', 'location', 'detailContent', 'newContent', 'showModifier'],
    computed : {
        showMM (){
            return this.showModifier
        }
    },
    methods : {
        realModify(){
            //console.log("!!!!", this.newContent, this.detailContent)
            //console.log("!!!!", this.cmp(this.newContent, this.detailContent))
            //console.log('real modify', this.newContent)
            if (this.cmp(this.newContent, this.detailContent)){
                this.$store.dispatch('showMsg', '无修改', 'info')
                //this.closeModifier()
            }else{
                console.log("!!!!", this.newContent, this.detailContent)
                //this.showContent = true
                console.log('modify', this.newContent)
                //this.newContent.id = this.showContent.id
                this.cbset.update(this.newContent)
                //this.closeModifier()
            }
            setTimeout(this.$emit('close'), 1000)
        },
        cmp : function( x, y ) {  
            return utils.cmp(x, y)
        },
    }
}
</script>

<style>
</style>

