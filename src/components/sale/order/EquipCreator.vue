<template>
    <div>
        <div class=spliter>
        </div>
        <div class="list" v-if="subtitle && subtitle.length > 0">
            <p>已添加清单：</p><br/>
            <div v-if="titleKeyComputed && titleKeyComputed.length > 0 && newContent && newContent.length > 0">
                <Table :columns=titleKeyComputed :data=newContent>
                </Table>
            </div>
            <!--
            <div v-if="subtitle && subtitle.length > 0">
                <table>
                    <thead>
                        <td v-for='(v, index) in subtitle'>{{v.displayName}}</td>
                    </thead>
                    <tbody>
                        <tr v-for='(x, index) in newContent'>
                            <td v-for='(v, ind) in subtitle'>{{x[v.item]}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            -->
        </div>
        <div class=spliter>
        </div>
        <div class="detail add">
            <div class="name">
                <Select v-model="tmpID" placeholder="请选择设备名">
                    <Option v-for="item in equipList" :value=item.id :key="item" @on-change=selectEquip> {{item.id}} | {{item['简称'] || item['名称']}} </Option>
                </Select>
            </div>
            <table>
                <tbody>
                    <tr v-for="(v, key) in subtitle">
                        <td v-if="v.invisable"> </td>
                        <td v-else>{{v.displayName}}</td>

                        <td v-if="v.invisable"> </td>
                        <td v-else>
                            <advancedInputer v-model=newAdder[v.item] :header=v>
                            </advancedInputer>
                        </td>

                    </tr>
                    <tr>
                        <td>单价</td>
                        <td>
                            <advancedInputer v-model=newUnitPrice :header=newUnitPriceHeader>
                            </advancedInputer>
                        </td>
                    </tr>
                    <tr>
                        <td>数量</td>
                        <td>
                            <advancedInputer v-model=newNumber :header=newNumberHeader>
                            </advancedInputer>
                        </td>
                    </tr>
                    <tr>
                        <td>总价</td>
                        <td>
                            <advancedInputer v-model=computedNewTotalPrice :header=newTotalPriceHeader>
                            </advancedInputer>
                        </td>
                    </tr>
                </tbody>
            </table>
            <center>
            <Button @click=addItem> 添加 </Button>
            <Button @click=clearItem> 清空 </Button>
            </center>
        </div>

        <div class="name" v-if="debug">
            newContent : {{newContent}} <br/>
            subtitle : {{subtitle}} <br/>
            titleKey : {{titleKey}} <br/>
            titleKeyComputed : {{titleKeyComputed}}<br/>
            newAdder : {{newAdder}} <br/>
        </div>
        
    </div>
</template>

<script>
import advancedInputer from '../../../utils/advancedInputer.vue'
export default {
    components : {
        advancedInputer,
    },
    data: function() {
        return {
            newContent : [],
            newAdder : {},
            debug : false,
            titleKey : [],
            tmpID : -1,
            newUnitPrice : 0,
            newNumber : 0,
//            newTotalPrice : 0,
            newUnitPriceHeader : {
                type : 'number',
            },
            newNumberHeader : {
                type : 'number',
            },
            newTotalPriceHeader : {
                type : 'number',
                immutable : true,
            },
        }
    },
    props : ['value', 'subtitle'],
    watch : {
        newContent : function(x){
            this.$emit('input', x)
        },
        value : function(x){
            console.log("EquipCreator value ->", x)
            this.newContent = x
        },
        subtitle: function(x){
            var ret = []
            console.log("Angel titleForTable x", x)
            for (var i in x){
                ret.push({
                    key : x[i].item,
                    title : x[i].displayName
                })
            }
            console.log("Angel titleForTable", ret)
            this.titleKey = ret
        },
        tmpID : function(x){
            console.log('tmpID change', x)
            this.newAdder.equipment_id = x
            this.selectEquip(x)
        },
        newAdder : function(x){
            console.log("newAdder -> ", x)
        },
        newUnitPrice : function(x){
            this.newAdder.unit_price = x
        },
        newNumber : function(x){
            this.newAdder.quantity = x
        },
    },
    computed : {
        titleKeyComputed : function(){
            var ret = []
            var x = this.subtitle
            //x = []
            //x = this.subtitle
            console.log('computed subtitle', this.subtitle)
            ret.push({
                key : 'iindex',
                title : '编号',
                type : 'index',
                width : 40,
                fixed : 'left',
            })
            for (var i in this.subtitle){
                ret.push({
                    key : this.subtitle[i].item,
                    title : this.subtitle[i].displayName,
                    width : 100
                })
            }
            this.titleKey = ret
            console.log("Angel titleKeyComputed", ret, "subtitle", this.subtitle)
            ret.push({
                title : '操作',
                key : 'action',
                width: 80,
                align: 'center',
                fixed : 'right',
                render (row, column, index) {
                    return `<i-button type="error" size="small" @click="newAdderRemove(${index})">删除</i-button>`;
                },
            })
            return ret
        },
        equipList : function(){
            return this.$store.getters.equipmentContent
        },
        computedNewTotalPrice : function(){
            return this.newAdder.total_price = this.newUnitPrice * this.newNumber
        },
    },
    methods : {
        check() {
            var ret = true
            if (typeof(this.newAdder.equipment_id) == undefined){
                this.$store.dispatch('showMsg', '请选择要采购的设备')
                ret = false
            }
            if (typeof(this.newAdder.quantity) == undefined){
                this.$store.dispatch('showMsg', '请输入要采购的设备数量')
                ret = false
            }
            return ret
        },
        addItem (){
            if (this.check() == false)return;
            this.newContent.push(JSON.parse(JSON.stringify(this.newAdder)))
            this.clearItem()
        },
        clearItem(){
            this.newAdder = {}
        },
        titleKeyMethod : function(){
            var ret = []
            for (var i in this.subtitle){
                ret.push({
                    key : this.subtitle[i].item,
                    title : this.subtutle[i].displayName
                })
            }
            this.titleKey = ret;
            console.log("Angel titleKeyMethod", ret)
            return ret
        },
        mounted(){
            this.titleKeyMethod()
            this.$store.dispatch('getEquipmentList')
        },
        selectEquip(id){
            console.log("on-change select")
            for (var i in this.equipList){
                if (this.equipList[i].id == id){
                    this.newAdder.product_name = this.equipList[i].info || this.equipList[i]['名称'] || this.equipList[i]['简称']
                    this.newAdder.spec = this.equipList[i]["规格"]
                    this.newAdder.model = this.equipList[i]["型号"]
                    this.newAdder.measurement_unit = this.equipList[i]["单位"]
                    this.newAdder.producer = this.equipList[i]["厂商"]
                    this.newAdder.unit_price = 0
                    this.newAdder.quantity = 0
                    //TODO :  change to the right price
                    this.newAdder.total_price = 0
//                    this.newAdder.product_configure = "产品配置单"
//                    this.newAdder.warranty_period = "保修期限"
//                    this.newAdder.install_require = "安装调试要求"
                    this.newUnitPrice = 0
                    this.newNumber = 0
                    return
                }
            }
        },
        newAdderRemove(ind){
            console.log("newadder remove", ind)
            this.newContent.splice(ind, 1)
       }
    }
}
</script>

<style>
.spliter{
    height:1px;
    width:90%;
    background:#cccccc;
    overflow:hidden;
        margin: 30px;
}
</style>

