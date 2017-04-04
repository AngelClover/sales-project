<template>
    <div v-if="showOutStore">
        <Modal v-model="showContent" witdh=auto @on-ok="$emit('close')" @on-cancel="$emit('close')" class-name="vertical-center-modal">
                    <div class="outstore-header">
                        销售订单详情
                    </div>
                    <div v-if="detailTitle && detailTitle.length > 0">
                        <Table :columns=detailColumn :data=detailData>
                        </Table>
                    <!--
                    <table border="1">
                        <tr><th v-for="(attr,index) in orderAttr">{{index}}</th></tr>
                        <tr><td v-for="attr in orderAttr">{{attr}}</td></tr>
                    </table>
                    -->
                    </div>
                    <div class="outstore-header">
                        设备清单： 
                    </div>
                    <div  v-if="equipmentList && equipmentList.length > 0">
                        <Table width=auto :columns=subColumn :data=subData @on-row-click="clickEquipment">
                            <!--
                        <tr> <th v-for="(attr, index) in equipmentList[0]">{{index}}</th></tr>
                        <tr v-for="eq in equipmentList" @click="clickEquipment(eq)">
                            <td v-for="attr in eq">{{attr}}</td>
                        </tr>
                            -->
                        </Table>
                    </div>
                    <div class="outstore-header">
                        可选在库设备:
                        <br/>
                    </div>
                        <br/>
                        <!--
                            TODO: decorate
                        -->
                    <div v-if="availableList && availableList.length > 0">
                        <!--
                        <Table width=auto  :columns=optionColumn :data=optionData> 
                        </Table>
                        -->
                        <table border=2>
                        <tr>
                            <th v-for="(attr, index) in optionTitle">{{attr.displayName}}</th>
                            <th>本次出库数量</th>
                        </tr>
                        <tr v-for="(item,index) in availableList">
                            <td v-for="attr in optionTitle">{{item[attr.item]}}</td>
                            <td><Input-number :min="0" :max="item.store_number" v-model="selectedSet[index]"><Input-number></td>
                        </tr>
                        <table>
                    </div>
                    <br/>
                    <div v-show=debug>
                        <p> showOutStore : {{showOutStore}} </p> <br/>
                        <!--
                        <p> outContent : {{outContent}} </p> <br/>
                        <p> storeForEquipment : {{storeForEquipment}} </p> <br/>
                        <p> stores : {{stores}} </p> <br/>
                        <p> targetEquipment : {{targetEquipment}} </p> <br/>
                        -->
                        <p> availableList : {{availableList}} </p> <br/>
                        <p> optionTitle : {{optionTitle}} </p> <br/>
                        <p> optionColumn : {{optionColumn}} </p> <br/>
                    </div>
                    <div slot="footer">
                    <Button @click="$emit('close')">
                        close
                    </Button>
                    <Button @click="outStore">
                        出货
                    </Button>
                    </div>
        </Modal>
    </div>
</template>

<script>
//TODO 需要双击才行的bug
import api from '../api'
import utils from './utils'
import _ from "underscore"
export default {
    props : ['showOutStore', 'outContent', 'storeForEquipment'],
    data: function() {
        return {
            debug : false,
            targetEquipment : {},
            selectedSet : [],
        }
    },
    computed : {
        orderAttr : function() {
            var backlist = ["equipments"]
            var ret = _.omit(this.outContent, backlist)
            console.log("orderAttr", ret)
            return ret
        },
        equipmentList : function(){
            var whitelist = ["equipments"]
            //var ret = _.pick(this.outContent, whiteList)
            var ret = this.outContent.equipments
            console.log("equipmentList", ret)
            return ret
        },
        availableList : function(){
            var ret = [];
            var x = this.targetEquipment.equipment_id
            x = x
            x = this.stores
            x = x
            x = this.$store.getters.inStore
            x = x
            console.log('1 get for equipment_id', this.targetEquipment.equipment_id)
            if (this.stores && this.targetEquipment.equipment_id){
                ret = this.stores[this.targetEquipment.equipment_id]
                console.log('get for equipment_id', this.targetEquipment.equipment_id)
            }
            for (var i in ret){
                ret[i].outNumber = 0
            }
            var rett = []
            for (var i in ret){
                if (ret[i].store_number > 0)rett.push(ret[i])
            }
            console.log('available List ', rett, this.stores)
            return rett;
        },
        stores : function(){
            return this.$store.getters.inStore
        },
        showContent (){
            return this.showOutStore
        },
        detailColumn (){
            var ret = []
                /*
            for (var i in this.orderAttr){
                ret.push({
                    key : i,
                    title : i,
                    width : 100,
                })
            }
            */
            if (typeof(this.detailTitle) == undefined || this.detailTitle.length <= 0)return ret
            for (var i in this.detailTitle){
                ret.push({
                    key : this.detailTitle[i].item,
                    title : this.detailTitle[i].displayName,
                    width : 100,
                })
            }
            return ret
        },
        detailData(){
            var ret = []
            ret.push(this.orderAttr)
            return ret
        },
        detailTitle(){
            return this.$store.getters.saleOrderTitle
        },
        subColumn (){
            var ret = []
            for (var i in this.subtitle){
                var obj = {
                    key : this.subtitle[i].item,
                    title : this.subtitle[i].displayName,
                    width : 100,
                }
                if (obj.title == '产品编号'){
                    obj.fixed = 'left'
                    obj.width = 60
                }
                if (obj.title == '出库状态'){
                    obj.fixed = 'right'
                }
                if (obj.title == '数量'){
                    obj.fixed = 'right'
                    obj.width = 60
                }
                if (obj.title == '已出库数量'){
                    obj.fixed = 'right'
                    obj.width = 60
                }
                ret.push(obj)
            }
            return ret
        },
        subData(){
            return this.equipmentList
        },
        subtitle(){
            return this.$store.getters.saleOrderSubtitle
        },
        optionColumn(){
            var ret = []
            for (var i in this.optionTitle){
                var obj = {
                    key : this.optionTitle[i].item,
                    title : this.optionTitle[i].displayName,
                    width : 100,
                }
                ret.push(obj)
            }
            var obj ={
                title: '出货数量',
                key: 'outNumber',
                width: 100,
                align: 'center',
                render (row, column, index) {
                    //return `<Input-number :min="0" v-model="selectedSet[${index}]"></Input-number>`;
                    return `<Input-number v-model="${row.outNumber}"></Input-number>`;
                    return `number`
                },
                fixed : 'right'

            }
            ret.push(obj)
            return ret
    },
    optionData(){
        return this.availableList
    },
    optionTitle(){
        return this.$store.getters.storeHouseTitle
    }
},
methods : {
    clickEquipment : function(eq){
        this.targetEquipment = eq;
        this.$store.dispatch('getStoredEquipmentList', {id:this.targetEquipment.equipment_id})
        this.$store.dispatch('getStoreHouseList')
            /*
        for (var index in this.availableList){
            this.selectedSet[index] = 0
        }
        */
        var up = 10
        if (this.availableList && this.availableList.length > 10) up = this.availableList.length
        this.selectedSet.splice(0, this.selectedSet.length)
        for (var i = 0; i < up; ++i){
            this.selectedSet.push(0)
        }
    },
    outStore : function(){
        var payload = {}
        payload.sale_equipment_id = this.targetEquipment.id
        payload.store_equipments = []
        //console.log("outstore avail", this.availableList, this.selectedSet)
        for (var i in this.availableList){
            var tmp = {}
            if (this.selectedSet[i] > 0){
                tmp.id = this.availableList[i].id
                tmp.number = this.selectedSet[i]
                payload.store_equipments.push(tmp)
            }
            }
            console.log("outStore payload", payload)
            this.$store.dispatch('outStoreEquipmentList', payload)
        }
    },
}
</script>

<style>
.outstore-mask{
  position: fixed;
  z-index: 7000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
  overflow: scroll;
}
.outstore-wrapper {
  display: table-cell;
  vertical-align: middle;
  z-index: 7100;
  overflow: scroll;
}

.outstore-container {
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
td{
    width:100px;
    text-align:center;
}
</style>

