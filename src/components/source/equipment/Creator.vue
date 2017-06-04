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
            <!--
            <Form ref="formData" :model="formData" :rules="formRule" label-position="left" :label-width=100>
                <Form-item prop="name" label="名称">
                    <Input type="text" v-model="formData.name" placeholder="请输入名称">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="abbr" label="简称">
                    <Input type="text" v-model="formData.abbr" placeholder="请输入简称">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="specification" label="描述">
                    <Input type="text" v-model="formData.specification">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="size" label="规格">
                    <Input type="text" v-model="formData.size" >
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="unit" label="单位">
                    <Input type="text" v-model="formData.unit" >
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="company" label="厂商">
                    <Input type="text" v-model="formData.company" >
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="badDate" label="产品注册证到期日期">
                    <Input type="text" v-model="formData.badDate" >
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="accessoryFile" label="审核材料附件">
                    <Input type="text" v-model="formData.accessoryFile" >
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                <Form-item prop="cold" label="是否冷链">
                    <Input type="text" v-model="formData.cold" >
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
            </Form>
            {{detailTitle}}
            -->
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
import api from '../../../api'
import utils from '../../../utils/utils'
//import OutSelector from './outSelector.vue'
import advancedInputer from '../../../utils/advancedInputer.vue'
import EquipCreator from './EquipCreator.vue'
export default {
    components : {
        //OutSelector,
        advancedInputer,
        EquipCreator,
    },
    data: function() {
        return {
            showOutStore : false,
            newContent : {
                '产品注册证到期日期' : this.getDateString(new Date()),
            },
            //showCC : false,
            tmpID : -1,
            formData : {
                name : '',
                abbr : '',
                specification : '',
                size : '',
                unit : '',
                company : '',
                badDate : '',
                accessoryFile : '',
                cold : '',
                code : '', //医疗器械标准码
                classify : '', //医疗器械分类
                englishName : '', 
            },
            formRule : {
                name : [
                { required: true, message: '请填写名称', trigger: 'blur'}
                    ],
                abbr : [
                { required: true, message: '请填写名称', trigger: 'blur'}
                    ],
            },
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
        getDateString(date){
            console.log('date now', date)
            var y = 1900 + date.getYear()
            var m = 1 + date.getMonth()
            var d = date.getDate()
            return  y + '-' + m + '-' + d
        },
        getTimeString(date){
            console.log('time now', date)
            var y = date.getFullYear()
            var m = 1 + date.getMonth()
            var d = date.getDate()
            var h = date.getHours()
            var mm = date.getMinutes()
            var s = date.getSeconds()
            var hh = ""
            if (h < 10) hh = "0" + h
            else hh = h
            var mmm = ""
            if (mm < 10) mmm = "0" + mm
            else mmm = mm
            var ss = ""
            if (s < 10) ss = "0" + s
            else ss = s
            return  y + '-' + m + '-' + d + ' ' + hh + ':' + mmm + ':' + ss
        },
    }
}
</script>

<style>
</style>

