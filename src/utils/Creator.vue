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
            <div class="selector" v-if="location=='storehouse'||location=='repair'||location=='logistic'">
                <Select v-model="tmpID" placeholder="请选择设备名" @on-change=selectEquip>
                    <Option v-for="item in equipList" :value=item.id :key="item" > {{item.id}} | {{item['简称'] || item['名称']}} </Option>
                </Select>
            </div>
            <table>
                <tbody>
                    <tr v-for="(v, key) in detailTitle">
                        <td v-if="v.invisable"> </td>
                        <td v-else>{{v.displayName}}</td>
                        <td v-if="v.invisable"> </td>
                        <td v-else>
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
            <EquipCreator :subtitle=detailSubtitle v-model=newContent.equipments v-if="location=='buyorder'||location=='saleorder'">
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
            tmpID : -1,
        }
    },
    props : ['detailTitle', 'cbset', 'stores', 'location', 'detailContent', 'showCreator', 'detailSubtitle'],
    computed : {
        showCC (){
            return this.showCreator
        },
        equipList : function(){
            return this.$store.getters.equipmentContent
        }
    },
    watch : {
        tmpID : function(x){
            console.log('tmpID change', x)
            this.newContent.equipment_id = x
            this.selectEquip(x)
        },
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
                console.log('create', this.newContent)
                //if (false)
                    this.cbset.save(this.newContent)
                //this.closeModifier()
            }
            setTimeout(this.$emit('close'), 1000)
        },
        cmp : function( x, y ) {  
            return utils.cmp(x, y)
        },
        mounted(){
            this.$store.dispatch('getEquipmentList')
        },
        selectEquip : function(id){
            console.log("on-change select")
            for (var i in this.equipList){
                if (this.equipList[i].id == id){
                    this.newContent.equipment_name = this.equipList[i].info || this.equipList[i]['名称'] || this.equipList[i]['简称']
                    return
                }
            }
        },
    }
}
</script>

<style>
</style>

