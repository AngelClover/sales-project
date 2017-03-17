<template>
    <div v-show="showDetails">
        <transition name="detail">
            <div class="detail-mask">
                <div class="detail-wrapper">
                    <div class="detail-container" @click="" v-show="showContent && actionType == 'show'">
                        <div class="detail-header">
                            详细信息
                        </div>
                        <div class="detail-body">
                            <table>
                                <tbody>
                                    <tr v-for="(value, key) in detailTitle">
                                        <td>{{value.displayName}}</td>
                                        <td>{{detailContent[value.item]}}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="detail-footer">
                            <center>
                            <button class="ui primary button" @click="$emit('close')">
                                OK
                            </button>
                            <button class="ui button" @click="modifier">
                                修改
                            </button>
                            <button class="ui red button" @click="approve" >
                                审批
                            </button>
                            <button class="ui green button" @click="transfer" >
                                采购
                            </button>
                            <button class="ui green button" @click="storeInAll" >
                                入库
                            </button>
                            <button class="ui green button" @click="storeOut" >
                                出库
                            </button>
                                <!--
                            <button class="ui green button" @click="storeInOne" >
                                单个入库
                            </button>
                                -->
                            </center>
                        </div>
                    </div>
                    <div class="detail-container modifier" @click="" v-show="!showContent || actionType == 'create'">
                        <div class="detail-header" v-show="actionType == 'show'">
                            修改
                        </div>
                        <div class="detail-header" v-show="actionType == 'create'">
                            新建
                        </div>
                        <div class="detail-body">
                            <table>
                                <tbody>
                                    <tr v-for="(value, key) in detailTitle">
                                        <td>{{value.displayName}}</td>
                                        <td>
                                            <input v-model=newContent[value.item]>
                                            </input>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="detail-footer">
                            <center>
                            <button class="ui red button" @click="closeModifier">
                                放弃
                            </button>
                            <button class="ui primary button" @click="realModify" v-show="actionType == 'show'">
                                修改
                            </button>
                            <button class="ui primary button" @click="realModify" v-show="actionType == 'create'">
                                新建
                            </button>
                            </center>
                        </div>
                    </div>
                    <OutSelector :showOutStore=showOutStore :outContent=detailContent @close="showOutStore=false;" :stores=stores>
                    </OutSelector>
                </div>
            </div>
        </transition>
        <div v-show=debug>
            <p> -----------Detail debug below----------- </p>
            <p> showDetails : {{showDetails}} </p>
            <p> detailTitle : {{detailTitle}} </p>
            <p> detailContent : {{detailContent}} </p>
            <p> actionType : {{actionType}} </p>
        </div>
    </div>
</template>

<script>
import api from '../api'
import utils from './utils'
import OutSelector from './outSelector.vue'
export default {
    components : {
        OutSelector
    },
    props : ['showDetails', 'detailTitle', 'detailContent', 'actionType', 'cbset', 'stores'],
    data: function() {
        return {
            debug : true,
            newContent : {},
            showContent : true,
            showOutStore : false,
        }
    },
    methods : {
        modifier: function(){
            this.newContent = this.deepCopy(this.detailContent)
            console.log('deep copy', this.newContent, this.detailContent)
            this.showContent = false
        },
        closeModifier(){
            this.newContent = {}
            this.showContent = true
            if (this.actionType == 'create'){
                this.$emit('close')
            }
            
        },
        realModify(){
            console.log("!!!!", this.newContent, this.detailContent)
            console.log("!!!!", this.cmp(this.newContent, this.detailContent))
            console.log('real modify', this.newContent)
            if (this.cmp(this.newContent, this.detailContent)){
                this.$store.dispatch('showMsg', '无修改', 'info')
                this.closeModifier()
            }else{
                console.log("!!!!", this.newContent, this.detailContent)
                this.showContent = true
                if (this.actionType == 'create'){
                    this.cbset.save(this.newContent)
                    this.closeModifier()
                }else if(this.actionType == 'show'){
                    console.log('modify', this.newContent)
                    //this.newContent.id = this.showContent.id
                    this.cbset.update(this.newContent)
                }else{
                    console.log('error actionType', this.actionType)
                }
            }
        },
        deepCopy : function(source) { 
            console.log('utils for deepcopy', utils)
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
    }

}
</script>

<style>
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

.detail-header h3 {
    margin-top: 0;
    color: #42b983;
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


</style>

