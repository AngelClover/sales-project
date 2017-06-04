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
            <!--
            <div class="selector" v-if="location=='storehouse'||location=='repair'||location=='logistic'">
                <Select v-model="tmpID" placeholder="请选择设备名" @on-change=selectEquip>
                    <Option v-for="item in equipList" :value=item.id :key="item" > {{item.id}} | {{item['简称'] || item['名称']}} </Option>
                </Select>
            </div>
            -->
            <!--
            <table>
                <tbody>
                    <tr v-for="(v, key) in detailTitle">
                        <td v-if="v.invisable"> </td>
                        <td v-else>{{v.displayName}}</td>
                        <td v-if="v.invisable"> </td>
                        <td v-else>
                            <advancedInputer v-model="newContent[v.item]" :header=v>
                            </advancedInputer>
                        </td>
                    </tr>
                </tbody>
            </table>
            -->
            <div v-if="detailTitle.length > 0">
            <Form ref="formData" :model="formData" :rules="formRule" label-position="left" :label-width=100>
                <Form-item prop="stdid" label="产品编号">
                    <div v-if="headerStdid.invisable"></div>
                    <div v-else>
                    <advancedInputer type="text" v-model="formDataStdid" placeholder="请输入名称" :header="headerStdid">
                    </advancedInputer>
                    </div>
                </Form-item>
                <Form-item prop="name" label="名称">
                    <advancedInputer type="text" v-model="formDataName" placeholder="请输入名称" :header="headerName">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="abbr" label="简称">
                    <advancedInputer type="text" v-model="formDataAbbr" placeholder="请输入简称" :header="headerAbbr">
                    </advancedInputer>
                </Form-item>
                <!--
                <Form-item prop="specification" label="描述">
                    <Input type="text" v-model="formDataSpecification">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                    </Input>
                </Form-item>
                -->
                <Form-item prop="size" label="规格">
                    <advancedInputer type="text" v-model="formDataSize" :header="headerSize">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="unit" label="单位">
                    <advancedInputer v-model="formDataUnit" :header="headerUnit">
                    </advancedInputed>
                </Form-item>
                <Form-item prop="class" label="产品类别">
                    <advancedInputer v-model="formDataClass" :header="headerClass">
                    </advancedInputed>
                </Form-item>
                <Form-item prop="company" label="厂商">
                    <advancedInputer type="text" v-model="formDataCompany" :header="headerCompany">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="badDate" label="产品注册证到期日期">
                    <advancedInputer type="text" v-model="formDataBadDate" :header="headerBadDate">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="accessoryFile" label="审核材料附件">
                    <advancedInputer type="text" v-model="formDataAccessoryFile" :header="headerAccessoryFile">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="cold" label="是否冷链">
                    <advancedInputer type="text" v-model="formDataCold" :header="headerCold">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="cold" label="医疗器械标准码">
                    <advancedInputer type="text" v-model="formDataCode" :header="headerCode">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="cold" label="医疗器械分类">
                    <advancedInputer type="text" v-model="formDataClassify" :header="headerClassify">
                    </advancedInputer>
                </Form-item>
                <Form-item prop="cold" label="英文名称">
                    <advancedInputer type="text" v-model="formDataEnglishName" :header="headerEnglishName">
                    </advancedInputer>
                </Form-item>
            </Form>
            </div>
            <div v-if="debug">
            {{detailTitle}}
            <br/>
            newContent:{{newContent}}
            <br/>
            formData:{{formData}}
            </div>
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
            debug : true,
            showOutStore : false,
            newContent : {
                '产品注册证到期日期' : this.getDateString(new Date()),
            },
            //showCC : false,
            tmpID : -1,
            formData : {
                stdid : '',
                name : '',
                abbr : '',
                specification : '',
                size : '',
                unit : '',
                class : '', 
                company : '',
                badDate : this.getDateString(new Date()),
                accessoryFile : '',
                cold : '',
                code : '',
                classify : '',
                englishName : '',
            },
            formDataStdid : '',
            formDataName : '',
            formDataAbbr : '', //简称
            formDataSpecification : '', //描述
            formDataSize : '', //规格
            formDataUnit : '', //单位
            formDataClass : '', //产品类别
            formDataCompany : '', //厂商
            formDataBadDate : this.getDateString(new Date()), //产品注册证过期时间
            formDataAccessoryFile : '', //审核材料附件
            formDataCold : '', //是否冷链
            formDataCode : '', //医疗器械标准码
            formDataClassify : '', //医疗器械分类
            formDataEnglishName : '', 
            formRule : {
                name : [
                { required: true, message: '请填写名称', trigger: 'blur'}
                ],
                abbr : [
                { required: true, message: '请填写简称', trigger: 'blur'}
                ],
            },
            headerStdid : {},
            headerName : {},
            headerAbbr : {},
            headerSpecification : {},
            headerSize : {},
            headerUnit : {},
            headerClass : {},
            headerCompany : {},
            headerBadDate : {},
            headerAccessoryFile : {},
            headerCold : {},
            headerCode : {},
            headerClassify : {},
            headerEnglish : {},

        }
    },
    props : ['detailTitle', 'cbset', 'stores', 'location', 'detailContent', 'showCreator', 'detailSubtitle'],
    computed : {
        showCC (){
            return this.showCreator
        },
        equipList : function(){
            return this.$store.getters.equipmentContent
        },
    },
    watch : {
        tmpID : function(x){
            console.log('tmpID change', x)
            this.newContent.equipment_id = x
            this.selectEquip(x)
        },
        formDataStdid (x){
            console.log('formDataStdid ->', x)
            this.formData.stdid = x
        },
        formDataName (x){
            console.log('formDataName ->', x)
            this.formData.name = x
        },
        formDataAbbr (x){
            console.log('formDataAbbr ->', x)
            this.formData.abbr = x
        },
        formDataSpecification (x){
            console.log('formDataSpecification ->', x)
            this.formData.specification = x
        },
        formDataSize (x){
            console.log('formDataSize ->', x)
            this.formData.size = x
        },
        formDataUnit (x){
            console.log('formDataUnit ->', x)
            this.formData.unit = x
        },
        formDataClass (x){
            console.log('formDataClass ->', x)
            this.formData.class = x
        },
        formDataCompany (x){
            console.log('formDataCompany ->', x)
            this.formData.company = x
        },
        formDataBadDate (x){
            console.log('formDataBadDate ->', x)
            this.formData.badDate = x
        },
        formDataAccessoryFile (x){
            console.log('formDataAccessory ->', x)
            this.formData.accessoryFile = x
        },
        formDataCold (x){
            console.log('formDataCold ->', x)
            this.formData.cold = x
        },
        formDataCode (x){
            console.log('formDataCode ->', x)
            this.formData.code = x
        },
        formDataClassify (x){
            console.log('formDataClassify ->', x)
            this.formData.classify = x
        },
        formDataEnglishName (x){
            console.log('formDataEnglishName ->', x)
            this.formData.englishName = x
        },
        detailTitle (x){
            console.log('detailTitle ->', x)
            for (var index in x){
                if (x[index].item == 'stdid'){
                    this.headerStdid = x[index]
                }
                if (x[index].item == '名称'){
                    this.headerName = x[index]
                }
                if (x[index].item == '简称'){
                    this.headerAbbr = x[index]
                }
                if (x[index].item == '描述'){
                    this.headerSpecification = x[index]
                }
                if (x[index].item == '规格'){
                    this.headerSize = x[index]
                }
                if (x[index].item == '单位'){
                    this.headerUnit = x[index]
                }
                if (x[index].item == '产品类别'){
                    this.headerClass = x[index]
                }
                if (x[index].item == '厂商'){
                    this.headerCompany = x[index]
                }
                if (x[index].item == '产品注册证到期日期'){
                    this.headerBadDate = x[index]
                }
                if (x[index].item == '审核材料附件'){
                    this.headerAccessoryFile = x[index]
                }
                if (x[index].item == '是否冷链'){
                    this.headerCold = x[index]
                }
                if (x[index].item == '医疗器械标准码'){
                    this.headerCode = x[index]
                }
                if (x[index].item == '医疗器械分类'){
                    this.headerClassify = x[index]
                }
                if (x[index].item == '英文名称'){
                    this.headerEnglishName = x[index]
                }
            }
        }
    },
    methods : {
        realCreate(){
            this.getNewContentFromFormData()
                return
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
        getNewContentFromFormData(){
            //TODO:
            this.newContent['stdid'] = this.formData.stdid
            this.newContent['名称'] = this.formData.name
            this.newContent['简称'] = this.formData.abbr
            //this.newContent['id'] = this.formData.specification
            this.newContent['规格'] = this.formData.size
            //型号
            this.newContent['单位'] = this.formData.unit
            this.newContent['产品类别'] = this.formData.class
            this.newContent['厂商'] = this.formData.company
            this.newContent['产品注册证到期日期'] = this.formData.badDate
            this.newContent['审核材料附件'] = this.formData.accessoryFile
            this.newContent['是否冷链'] = this.formData.cold
            this.newContent['医疗器械标准码'] = this.formData.code
            this.newContent['医疗器械分类'] = this.formData.classify
            this.newContent['英文名称'] = this.formData.englishName
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

