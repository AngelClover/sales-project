<template>
    <div v-if="showDetails">
        <!--
        <transition name="detail">
            <div class="detail-mask">
                <div class="detail-wrapper">
        -->
        <Modal v-model="showContent" width=auto @on-ok="$emit('close')" @on-cancel="$emit('close')" class-name="vertical-center-modal">
                    <div slot="header">
                        详细信息
                    </div>
                    <div class="detail-container" >
                        <div class="detail-body">
                            <table >
                                <tbody>
                                    <tr v-for="(value, key) in detailTitle">
                                        <td><p>{{value.displayName}}</p>
                                        </td>
                                        <td><p>{{detailContent[value.item]}}</p></td>
                                    </tr>
                                </tbody>
                            </table>
        <EquipDetail v-if=showEquipmentLists @close="showEquipmentLists=false" :equipList=detailContent.equipments :subtitle=detailSubtitle>
        </EquipDetail>

        <div v-show=debug>
            <p> -----------Detail debug below----------- </p>
            <p> showDetails : {{showDetails}} </p>
            <p> location : {{location}} </p>
            <p> detailTitle : {{detailTitle}} </p>
            <p> detailContent : {{detailContent}} </p>
        </div>
                        </div>
                    </div>
                        <div slot="footer">
                            <center>
                            <button class="ui secondary button" @click="$emit('close')"> OK </button>
                            <button class="ui primary button" @click="modifier"> 修改 </button>
                            <button class="ui primary  button" @click="approve" > 审批 </button>
                            <button class="ui primary button" @click="transfer" > 采购 </button>
                            <button class="ui primary button" @click="storeInAll" > 入库 </button>
                            <button class="ui primary button" @click="storeOut" > 出库 </button>
                            <Button @click="handleDelete"> 删除 </Button>
                                <!--
                            <button class="ui green button" @click="storeInOne" >
                                单个入库
                            </button>
                                -->
                            </center>
                        </div>
                    <!--
                </div>
            </div>
        </transition>
                    -->
        </Modal>
        <Modifier :detailTitle=detailTitle :cbset=cbset :stores=stores :location=location :detailContent=detailContent :showModifier=showModifier @close="showModifier=false;showContent=true" :newContent=newContent :detailSubtitle=detailSubtitle>
        </Modifier>
    </div>
</template>

<script>
import api from '../api'
import utils from './utils'
import OutSelector from './outSelector.vue'
import advancedInputer from './advancedInputer.vue'
import Modifier from './Modifier.vue'
import EquipDetail from './EquipDetail.vue'
export default {
    components : {
        OutSelector,
        advancedInputer,
        Modifier,
        EquipDetail,
    },
    props : ['showDetails', 'detailTitle', 'detailContent', 'cbset', 'stores', 'location', 'detailSubtitle'],
    data: function() {
        return {
            debug : false,
            newContent : {},
            showContent : true,
            showModifier : false,
            contentVisible : true,
            showEquipmentLists : true
        }
    },
    watch : {
        detailContent : function(x){
            if (this.showModifier){
            }else{
                this.newContent = JSON.parse(JSON.stringify(x))//this.deepCopy(x)
            }
            console.log('detail various -> ', x)
        },
        newContent : function(x){
            console.log('newContent modified -> ', x)
        },
        showModifier : function(x){
            console.log("showModifier", x, " -> showContent", this.showContent)
            //this.showContent = (x == false)
        },
        showDetails : function(x){
            this.showModifier = false
            this.showContent = true
        }
    },
    methods : {
        modifier: function(){
            this.newContent = JSON.parse(JSON.stringify(this.detailContent))//this.deepCopy(this.detailContent)
            //console.log('deep copy', this.newContent, this.detailContent)
            this.showContent = false
            this.showModifier = true
            console.log("click to modifier ")
            this.$store.dispatch('getEquipmentList')
        },
        /*
        closeModifier(){
            this.showContent = true
            setTimeout(this.newContent = {}, 1000)
        },
        */
        deepCopy : function(source) { 
            //console.log('utils for deepcopy', utils)
            return utils.deepCopy(source)
        },
        cmp : function( x, y ) {  
            return utils.cmp(x, y)
        },
        approve : function(){
            this.cbset.approve(this.detailContent)
        },
        transfer : function(){
            this.cbset.transfer(this.detailContent)
        },
        storeInAll : function(){
            this.cbset.storeInAll(this.detailContent)
        },
        storeOut : function(){
            this.showOutStore = true;
            //this.cbset.storeOut(this.detailContent)
        },
        handleDelete : function(){
            this.cbset.remove(this.detailContent)
        }
    }

}
</script>

<style lang="less">
table {
  width: 90%;
  overflow: scroll;
  margin-left:auto;
  margin-right:auto;
}
td{
    width: 50%;
}
.detail-mask{
  position: fixed;
  z-index: 5000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
  overflow: scroll;
}
.detail-wrapper {
  display: table-cell;
  vertical-align: middle;
  z-index: 6000;
  overflow: scroll;
}

.detail-container {
  width: 75%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  height:90%;
  overflow: scroll;
}
.modifier {
    z-index: 6050;
}

.detail-header h2 {
    margin-top: 0;
    color: #42b983;
    position: center;
}

.detail-body {
    margin: 20px 0;
}

.detail-footer {
}
.detail-default-button{
    float: right;
}

.detail-enter{
  opacity: 0;
}
.detail-leave-to{
  opacity: 0;
}
.modal-enter .modal-contailner,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
.vertical-center-modal{
    display: flex;
    align-items: center;
    justify-content: center;

        .ivu-modal{
            top: 0;
        }
}

</style>

