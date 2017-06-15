<template>
    <div v-if="showDetails">
        <!-- "separate BuyDetail from BuyListView's modal" : -->
        <Row>
            <slot name="titlename"> </slot>
            <Button type="text" size="large" icon="forward" style="float: right;" @click="closeDetail">返回订单列表</Button>
        </Row>
        <Card>
            <div style="padding: 20px 10px;">
                <Row style="margin-bottom: 10px;">
                    <Col span="16">
                        <h3>订单信息</h3>
                    </Col>
                    <Col span="8">
                        <div style="float: right;">
                            <Button icon="edit" @click="modifier">修改</Button>
                            <Poptip width="180" confirm placement="bottom-end" title="确认删除该订单吗？" @on-ok="deleteDetail">
                                <Button icon="trash-a">删除</Button>
                            </Poptip>
                        </div>
                    </Col>
                </Row>
                <Form :label-width="150">
                    <div v-for="(value, key) in detailTitle">
                        <Form-item :label="value.displayName" class="formitem">
                            <div v-if="value.type != 'file'">
                                <Label>{{detailContent[value.item]}}</Label>
                            </div>
                            <div v-if="value.type === 'file'">
                                <div v-if="detailContent[value.item] instanceof Array">
                                    <div v-for="item in detailContent[value.item]">
                                        <p><a :href="uploadPrefix + item" target="_blank">file:{{item}}</a></p>
                                    </div>
                                </div>
                                <div v-else-if="detailContent[value.item] != null">
                                    <p><a :href="uploadPrefix + detailContent[value.item]" target="_blank">file:{{detailContent[value.item]}}</a></p>
                                </div>
                            </div>
                        </Form-item>
                    </div>
                </Form>
            </div>
            <br/>
            <div style="padding: 20px 10px; border-top: 1px solid #e9eaec;">
                <Row style="margin-bottom: 10px;">
                    <Col span="16">
                        <h3>流程进度</h3>
                    </Col>
                    <Col span="8">
                        <Button-group style="float: right;">
                            <Button icon="android-checkbox-outline" @click="approve">审核通过</Button>
                            <Button icon="ios-cart" @click="transfer">开始采购</Button>
                        </Button-group>
                    </Col>
                </Row>
                <Steps :current="currentState" style="margin: 30px 0 0 10px;">
                    <Step v-for="(state, index) in stateSet" :title="state" :content="stateDescription[index]"></Step>
                </Steps>
            </div>
            <br/>
            <div style="padding: 20px 10px; border-top: 1px solid #e9eaec;">
                <Row style="margin-bottom: 10px;">
                    <Col span="16">
                        <h3>设备清单</h3>
                    </Col>
                    <Col span="8">
                        <Button-group style="float: right;">
                            <Poptip placement="top-end">
                                <Button icon="forward">全部接收</Button>
                                <div slot="content">
                                    <Row style="margin-bottom: 10px;">
                                        <Label>接收温度：</Label>
                                        <Input v-model="receive_temperature" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>接收湿度：</Label>
                                        <Input v-model="receive_humidity" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>接收备注：</Label>
                                        <Input v-model="receive_message" style="width: 100px"></Input>
                                    </Row>
                                    <Row>
                                        <Button long type="primary" @click="receiveInAll">确定</Button>
                                    </Row>
                                </div>
                            </Poptip>
                            <Poptip placement="top-end">
                                <Button icon="eye">全部检验</Button>
                                <div slot="content">
                                    <Row style="margin-bottom: 10px;">
                                        <Label>检验温度：</Label>
                                        <Input v-model="inspect_temperature" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>检验湿度：</Label>
                                        <Input v-model="inspect_humidity" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>抽检数量：</Label>
                                        <Input v-model="inspect_number" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>合格数量：</Label>
                                        <Input v-model="inspect_ok_number" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>检验备注：</Label>
                                        <Input v-model="inspect_message" style="width: 100px"></Input>
                                    </Row>
                                    <Row>
                                        <Button long type="primary" @click="inspectInAll">确定</Button>
                                    </Row>
                                </div>
                            </Poptip>
                            <Poptip placement="top-end">
                                <Button icon="home">全部入库</Button>
                                <div slot="content">
                                    <Row style="margin-bottom: 10px;">
                                        <Label>入库温度：</Label>
                                        <Input v-model="store_temperature" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>入库湿度：</Label>
                                        <Input v-model="store_humidity" style="width: 100px"></Input>
                                    </Row>
                                    <Row style="margin-bottom: 10px;">
                                        <Label>入库备注：</Label>
                                        <Input v-model="store_message" style="width: 100px"></Input>
                                    </Row>
                                    <Row>
                                        <Button long type="primary" @click="storeInAll">确定</Button>
                                    </Row>
                                </div>
                            </Poptip>
                        </Button-group>
                    </Col>
                </Row> 
                <Collapse>
                    <Panel v-for="equipment in detailContent.equipments">
                        {{ equipment.product_name }}
                        <div slot="content">
                            <Table border :columns="titleForTable" :data="[equipment]">
                            </Table>
                            <Button-group style="float: right; margin: 10px 0;">
                                <Poptip placement="top-end">
                                    <Button icon="forward">接收</Button>
                                    <div slot="content">
                                        <Row style="margin-bottom: 10px;">
                                            <Label>接收温度：</Label>
                                            <Input v-model="receive_temperature" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>接收湿度：</Label>
                                            <Input v-model="receive_humidity" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>接收备注：</Label>
                                            <Input v-model="receive_message" style="width: 100px"></Input>
                                        </Row>
                                        <Row>
                                            <Button long type="primary" @click="receiveInOne(equipment.id)">确定</Button>
                                        </Row>
                                    </div>
                                </Poptip>
                                <Poptip placement="top-end">
                                    <Button icon="eye">检验</Button>
                                    <div slot="content">
                                        <Row style="margin-bottom: 10px;">
                                            <Label>检验温度：</Label>
                                            <Input v-model="inspect_temperature" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>检验湿度：</Label>
                                            <Input v-model="inspect_humidity" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>抽检数量：</Label>
                                            <Input v-model="inspect_number" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>合格数量：</Label>
                                            <Input v-model="inspect_ok_number" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>检验备注：</Label>
                                            <Input v-model="inspect_message" style="width: 100px"></Input>
                                        </Row>
                                        <Row>
                                            <Button long type="primary" @click="inspectInOne(equipment.id)">确定</Button>
                                        </Row>
                                    </div>
                                </Poptip>
                                <Poptip placement="top-end">
                                    <Button icon="home">入库</Button>
                                    <div slot="content">
                                        <Row style="margin-bottom: 10px;">
                                            <Label>入库温度：</Label>
                                            <Input v-model="store_temperature" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>入库湿度：</Label>
                                            <Input v-model="store_humidity" style="width: 100px"></Input>
                                        </Row>
                                        <Row style="margin-bottom: 10px;">
                                            <Label>入库备注：</Label>
                                            <Input v-model="store_message" style="width: 100px"></Input>
                                        </Row>
                                        <Row>
                                            <Button long type="primary" @click="storeInOne(equipment.id)">确定</Button>
                                        </Row>
                                    </div>
                                </Poptip>
                            </Button-group>
                        </div>
                    </Panel>
                </Collapse>
            </div>
        </Card>
        <!-- by CHEN 17.6.13 -->

        <!-- "separate BuyDetail from BuyListView's modal" : remove below 
        <Modal v-model="showContent" width="auto" @on-ok="$emit('close')" @on-cancel="$emit('close')">
            <div slot="header">详细信息</div>
            <div class="detail-container">
                <div class="detail-body">
                    <Steps :current="currentState">
                    <Step v-for="(state, index) in stateSet" :title="state" :content="stateDescription[index]"></Step>
                    </Steps>
                    <br/>
                    <Form :label-width="100">
                        <div v-for="(value, key) in detailTitle">
                            <Form-item :label="value.displayName" class="formitem">
                                <div v-if="value.type != 'file'">
                                    <Label>{{detailContent[value.item]}}</Label>
                                </div>
                                <div v-if="value.type === 'file'">
                                    <div v-if="detailContent[value.item] instanceof Array">
                                        <div v-for="item in detailContent[value.item]">
                                            <p><a :href="uploadPrefix + item" target="_blank">file:{{item}}</a></p>
                                        </div>
                                    </div>
                                    <div v-else-if="detailContent[value.item] != null">
                                        <p><a :href="uploadPrefix + detailContent[value.item]" target="_blank">file:{{detailContent[value.item]}}</a></p>
                                    </div>
                                </div>
                            </Form-item>
                        </div>
                    </Form>
                    <EquipDetail v-if="showEquipmentLists" @close="showEquipmentLists=false" :equipList="detailContent.equipments" :subtitle="detailSubtitle" :cbset="cbset">
                    </EquipDetail>
                    <div style="margin:100px">
                        <center>
                            <button class="ui primary button" v-if="location=='buyorder'" @click="receiveInAll" > 全部接收 </button>
                            <button class="ui primary button" v-if="location=='buyorder'" @click="inspectInAll" > 全部检验通过 </button>
                            <button class="ui primary button" v-if="location=='buyorder'" @click="storeInAll" > 全部入库 </button>
                        </center>
                        <center>
                            <Row>
                                <Label>接收温度:</Label>
                                <Input v-model="receive_temperature" style="width:100px">
                                </Input>
                                <Label>接收湿度:</Label>
                                <Input v-model="receive_humidity" style="width:100px">
                                </Input>
                                <Label>接收备注:</Label>
                                <Input v-model="receive_message" style="width:100px">
                                </Input>
                                <br/>
                                <Label>检验温度:</Label>
                                <Input v-model="inspect_temperature" style="width:100px">
                                </Input>
                                <Label>检验湿度:</Label>
                                <Input v-model="inspect_humidity" style="width:100px">
                                </Input>
                                <Label>抽检数量:</Label>
                                <InputNumber v-model="inspect_number" style="width:100px">
                                </InputNumber>
                                <Label>检验合格数量:</Label>
                                <InputNumber v-model="inspect_ok_number" style="width:100px">
                                </InputNumber>
                                <Label>检验备注:</Label>
                                <Input v-model="inspect_message" style="width:100px">
                                </Input>
                                <br/>
                                <Label>入库温度:</Label>
                                <Input v-model="store_temperature" style="width:100px">
                                </Input>
                                <Label>入库湿度:</Label>
                                <Input v-model="store_humidity" style="width:100px">
                                </Input>
                                <Label>入库备注:</Label>
                                <Input v-model="store_message" style="width:100px">
                                </Input>
                            </Row>
                        </center>
                    </div>

                    <div v-show="debug">
                        <p> -----------Detail debug below----------- </p>
                        <p> showDetails : {{showDetails}} </p>
                        <p> location : {{location}} </p>
                        <p> detailTitle : {{detailTitle}} </p>
                        <p> detailContent : {{detailContent}} </p>
                    </div>
                </div>
                <div slot="footer">
                    <center>
                        <button class="ui secondary button" @click="$emit('close')"> OK </button>
                        <button class="ui primary button" @click="modifier"> 修改 </button>
                        <button class="ui primary  button" @click="approve" v-if="location!='repair'&&location!='logistic'"> 审批 </button>
                        <button class="ui primary  button" @click="complete" v-if="location=='repair'||location=='logistic'"> 完成 </button>
                        <button class="ui primary button" v-if="location=='buyorder'" @click="transfer" > 采购 </button>
                        <Button @click="handleDelete"> 删除 </Button>
                    </center>
                </div>
            </div>
        </Modal>
        by CHEN 17.6.15 -->

        <!-- "separate BuyDetail from BuyListView's modal" : change close-event respond -->
        <Modifier :detailTitle="detailTitle" :cbset="cbset" :stores="stores" :location="location" :detailContent="detailContent" :showModifier="showModifier" @close="showModifier=false;showContent=true" :newContent="newContent" :detailSubtitle="detailSubtitle">
        </Modifier>
        <!-- by CHEN 17.6.15 -->

        <OutSelector :showOutStore="showOutStore" :outContent="detailContent" @close="showOutStore=false;" :stores="stores">
        </OutSelector>
    </div>
</template>

<script>
import api from '../../../api'
import utils from '../../../utils/utils'
import OutSelector from '../../../utils/outSelector.vue'
import advancedInputer from '../../../utils/advancedInputer.vue'
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
            showEquipmentLists : true,
            showOutStore : false,
            uploadPrefix : 'http://angelclover.win:8088/uploadfiles/',
            stateSet : ['待审核', '审核通过', '待入库', '入库中', '已入库'],
            stateDescription : ['待审核','待采购','接收、检验、入库','部分已入库','入库完成'],
            receive_temperature : "",
            receive_humidity : "",
            receive_message : "",
            inspect_temperature : "",
            inspect_humidity : "",
            inspect_number : 0,
            inspect_ok_number : 0,
            inspect_message : "",
            store_temperature : "",
            store_humidity : "",
            store_message : "",
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
    computed : {
        currentState (){
            var ret = 0;
            for (var i = 0; i < this.stateSet.length; ++i){
                if (this.stateSet[i] == this.detailContent.state){
                    return i;
                }
            }
            return ret;
        },
        //---- "separate BuyDetail from BuyListView's modal" : add titleForTable for equipment table
        titleForTable : function() {
            var ret = []
            for (var item in this.detailSubtitle){
                var obj = {
                    key : this.detailSubtitle[item].item,
                    title : this.detailSubtitle[item].displayName,
                    width : 110,
                }
                ret.push(obj)
            }
            return ret
        },
        //---- by CHEN 17.6.14
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
            //TODO: update content after approve by CHEN 17.6.15
            this.cbset.approve(this.detailContent)
        },
        transfer : function(){
            //TODO: update content after transfer by CHEN 17.6.15
            this.cbset.transfer(this.detailContent)
        },
        //---- "separate BuyDetail from BuyListView's modal" : add new states and InOne-functions
        receiveInAll : function(){
            var tmp = {
                id: this.detailContent.id,
                receive_temperature: this.receive_temperature,
                receive_humidity: this.receive_humidity,
                receive_message: this.receive_message,
            }
            this.cbset.receiveInAll(tmp)
        },
        receiveInOne : function(id){
            var tmp = {
                id: id,
                receive_temperature: this.receive_temperature,
                receive_humidity: this.receive_humidity,
                receive_message: this.receive_message,
            }
            this.cbset.receiveInOne(tmp)
        },
        inspectInAll : function(){
            var tmp = {
                id: this.detailContent.id,
                inspect_temperature: this.inspect_temperature,
                inspect_humidity: this.inspect_humidity,
                inspect_number: this.inspect_number,
                inspect_ok_number: this.inspect_ok_number,
                inspect_message: this.inspect_message,
            }
            this.cbset.inspectInAll(tmp)
        },
        inspectInOne : function(id){
            var tmp = {
                id: id,
                inspect_temperature: this.inspect_temperature,
                inspect_humidity: this.inspect_humidity,
                inspect_number: this.inspect_number,
                inspect_ok_number: this.inspect_ok_number,
                inspect_message: this.inspect_message,
            }
            this.cbset.inspectInOne(tmp)
        },
        storeInAll : function(){
            var tmp = {
                id: this.detailContent.id,
                store_temperature: this.store_temperature,
                store_humidity: this.store_humidity,
                store_message: this.store_message,
            }
            this.cbset.storeInAll(tmp)
        },
        storeInOne : function(id){
            var tmp = {
                id: id,
                store_temperature: this.store_temperature,
                store_humidity: this.store_humidity,
                store_message: this.store_message,
            }
            this.cbset.storeInOne(tmp)
        },
        //---- by CHEN 17.6.15
        storeOut : function(){
            this.showOutStore = true;
            //this.cbset.storeOut(this.detailContent)
        },
        handleDelete : function(){
            this.cbset.remove(this.detailContent)
        },
        complete : function(){
            if (this.location == "repair"){
                this.$store.dispatch('updateRepair', {id:this.detailContent.id, repair_status:'已完成'})
                setTimeout(this.$store.dispatch('getRepairList'), 1000)
            }
            if (this.location == "logistic"){
                this.$store.dispatch('updateLogistic', {id:this.detailContent.id, delivery_status:'已完成'})
                setTimeout(this.$store.dispatch('getLogisticList'), 1000)
            }
        },
        saleOrderConfirm : function(){
            //this.cbset.confirmSaleOrder(this.detailContent)
            this.$store.dispatch('confirmSaleOrder', {id:this.detailContent.id})
            //TODO: if success , trigger the repair && logistic
        },
        // "separate BuyDetail from BuyListView's modal" : emit close-event when delete
        deleteDetail : function(){
            this.cbset.remove(this.detailContent)
            this.$emit('close')
        },
        closeDetail : function() {
            this.$emit('close')
        },
        // by CHEN 17.6.15
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

div.formitem.ivu-form-item{
    margin-bottom: 0px;
}

</style>

