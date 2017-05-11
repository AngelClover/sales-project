<template>
    <div>
        <div v-if="titleForTable.length > 0 && equipList">
            <p> 设备清单: </p>
        </div>
        <!--
        <div class="equiplist" v-if="equipList && equipList.length > 0">
            <div class="equipitem" v-for="(item, index) in equipList">
                {{item}}
            </div>
        </div>
        -->
        <div v-if="titleForTable.length > 0 && equipList && equipList.length > 0">
            <Table :columns=titleForTable :data=equipList>
            </Table>
        </div>
        <center>
        <Row>
            <Label>接收温度:</Label>
            <Input v-model=receive_temperature style="width:100px">
            </Input>
            <Label>接收备注:</Label>
            <Input v-model=receive_message style="width:100px">
            </Input>
            <br/>
        <Label>检验合格数量:</Label>
            <InputNumber v-model=inspect_ok_number style="width:100px">
            </InputNumber>
            <Label>检验备注:</Label>
            <Input v-model=inspect_message style="width:100px">
            </Input>
            <br/>
            <Label>入库温度:</Label>
            <Input v-model=store_temperature style="width:100px">
            </Input>
            <Label>入库备注:</Label>
            <Input v-model=store_message style="width:100px">
            </Input>
        </Row>
        </center>
        <!--
        <Modal v-if=showReceive class="zmodel" @on-ok="receive" @on-cancel="showReceive=false">
            <Label>接收温度:</Label>
            <Input v-model=receive_temperature>
            </Input>
            <br/>
            <Label>接收备注:</Label>
            <Input v-model=receive_message>
            </Input>
        </Modal>
        -->
        <div v-if="debug">
            -------------Debug for EquipDetail----------
            subtitle : {{titleForTable}} <br/>
            equipList : {{equipList}}<br/>
            showReceive : {{showReceive}} <br/>
            receive_id : {{receive_id}}<br/>
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            debug : false,
            showReceive : false,
            receive_id : -1,
            receive_message : "",
            receive_temperature : "",
            inspect_message : "",
            inspect_ok_number : 0,
            store_message : "",
            store_temperature : "",
        }
    },
    props : ['equipList', 'subtitle', 'cbset'],
    computed : {
        titleForTable() {
            var ret = []
            ret.push({
                key : 'iindex',
                title : '编号',
                type : 'index',
                width : 50,
                fixed : 'left',
            })
            for (var item in this.subtitle){
                var obj = {
                    key : this.subtitle[item].item,
                    title : this.subtitle[item].displayName,
                    width : 100,
                    sortable : true,
                }
                /*
                var res = this.subtitle[item].displayName.match('是否')
                console.log('res', res)
                if (res && res.length> 0){
                    obj.fixed = 'right'
                    console.log(res.length)
                }
                */
                ret.push(obj)
            }
            ret.push({
                title: '接收',
                key: 'action',
                fixed: 'right',
                width: 150,
                align: 'center',
                render (row, column, index) {
                    if (row.received && row.received == 1){
                        var ret = row.received_user 
                        if (row.receive_temperature)ret += '<br/>' + row.receive_temperature
                        if (row.receive_time)ret += '<br/>' + row.receive_time
                        if (row.receive_message)ret += '<br/>' + row.receive_message
                        return ret 
                    }else 
                        return `<ToolTip content="请先填写接收温度及备注"> <i-button type="primary" size="small" @click="receive(${index})">接收</i-button> </ToolTip>`;
                }
            })
            ret.push({
                title: '检验',
                key: 'action',
                fixed: 'right',
                width: 150,
                align: 'center',
                render (row, column, index) {
                    if (row.inspected && row.inspected == 1){
//                        return row.inspected_user
                        var ret = row.inspected_user 
                        if (row.inspect_ok_number)ret += '<br/>' + row.inspect_ok_number + '/' + row.quantity + "合格"
                        if (row.inspect_time)ret += '<br/>' + row.inspect_time
                        if (row.inspect_message)ret += '<br/>' + row.inspect_message
                        return ret 
                    }else 
                        return `<ToolTip content="请先填写抽检合格数量及备注"> <i-button type="primary" size="small" @click="inspect(${index})">检验</i-button> </ToolTip>`;
                }
            })
            ret.push({
                title: '入库',
                key: 'action',
                fixed: 'right',
                width: 150,
                align: 'center',
                render (row, column, index) {
                    if (row.stored && row.stored == 1){
//                        return row.stored_user
                        var ret = row.stored_user 
                        if (row.store_temperature)ret += '<br/>' + row.store_temperature
                        if (row.store_time)ret += '<br/>' + row.store_time
                        if (row.store_message)ret += '<br/>' + row.store_message
                        return ret 
                    }else 
                        return `<ToolTip content="请先填写入库温度及备注"> <i-button type="primary" size="small" @click="store(${index})">入库</i-button> </ToolTip>`;
                }
            })
            console.log('subtitle ', this.subtitle)
            return ret
        }
    },
    methods : {
        receive : function(index){
            console.log('receive click', index, this.equipList[index].id, this.cbset)
            if (this.equipList[index]){
                this.cbset.receiveInOne({
                    id:this.equipList[index].id,
                    receive_temperature:this.receive_temperature,
                    receive_message:this.receive_message
                })
            }
        },
        inspect : function(index){
            console.log('inspect click', index, this.equipList[index].id, this.cbset)
            if (this.equipList[index]){
                this.cbset.inspectInOne({
                    id:this.equipList[index].id,
                    inspect_ok_number:this.inspect_ok_number,
                    inspect_message:this.inspect_message

                })
            }
        },
        store : function(index){
            console.log('store click', index, this.equipList[index].id, this.cbset)
            if (this.equipList[index]){
                this.cbset.storeInOne({
                    id:this.equipList[index].id,
                    store_temperature:this.store_temperature,
                    store_message:this.store_message
                })
            }
        },
        /*
        clickReceive : function(index){
            console.log("click receive", index)
            this.showReceive = true
            if (this.equipList[index]) this.receive_id = this.equipList[index].id
        }
        */
    }

}
</script>

<style>
.zmodel{
    zindex:9000
}
</style>

