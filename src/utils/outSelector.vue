<template>
    <div v-show="showOutStore">
        <div class="outstore-mask">
            <div class="outstore-wrapper">
                <div class="outstore-container" @click="" >
                    <div class="outstore-header">
                        销售订单详情
                    </div>
                    <table border="0">
                        <tr><th v-for="(attr,index) in orderAttr">{{index}}</th></tr>
                        <tr><td v-for="attr in orderAttr">{{attr}}</td></tr>
                    </table>
                    <div class="outstore-header">
                        设备清单： 
                    </div>
                    <table border="0" v-if="equipmentList && equipmentList.length > 0">
                        <tr> <th v-for="(attr, index) in equipmentList[0]">{{index}}</th></tr>
                        <tr v-for="eq in equipmentList" @click="clickEquipment(eq)">
                            <td v-for="attr in eq">{{attr}}</td>
                        </tr>
                    </table>
                    <div class="outstore-header">
                        可选在库设备:
                        <br/>
                    </div>
                        <br/>
                    <table border="0" v-if="availableList && availableList.length > 0">
                        <tr>
                            <th>number</th>
                            <th v-for="(attr, index) in availableList[0]">{{index}}</th>
                        </tr>
                        <tr v-for="(item,index) in availableList">
                            <td><input v-model=selectedSet[index]></td>
                            <td v-for="attr in item">{{attr}}</td>
                        </tr>
                    </table>
                    <br/>
                    <button @click="$emit('close')">
                        close
                    </button>
                    <button @click="outStore">
                        出货
                    </button>
                    <div v-show=debug>
                        <p> showOutStore : {{showOutStore}} </p> <br/>
                        <p> outContent : {{outContent}} </p> <br/>
                        <p> storeForEquipment : {{storeForEquipment}} </p> <br/>
                        <p> availableList : {{availableList}} </p> <br/>
                        <p> stores : {{stores}} </p> <br/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from '../api'
import utils from './utils'
import _ from "underscore"
export default {
    props : ['showOutStore', 'outContent', 'storeForEquipment'],
    data: function() {
        return {
            debug : true,
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
            if (this.stores && this.targetEquipment.equipment_id){
                ret = this.stores[this.targetEquipment.equipment_id]
            }
            return ret;
        },
        stores : function(){
            return this.$store.getters.inStore
        }
    },
    methods : {
        clickEquipment : function(eq){
            this.targetEquipment = eq;
            this.$store.dispatch('getStoredEquipmentList', {id:this.targetEquipment.equipment_id})
                /*
            for (var index in this.availableList){
                this.selectedSet[index] = 0
            }
            */
            var up = 10
            if (this.availableList.length > 10) up = this.availableList.length
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
</style>

