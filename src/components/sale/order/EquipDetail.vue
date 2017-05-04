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
        <div v-if="debug">
            -------------Debug for EquipDetail----------
            subtitle : {{titleForTable}} <br/>
            equipList : {{equipList}}<br/>
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            debug : false,
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
                var res = this.subtitle[item].displayName.match('数量')
                console.log('res right', res)
                if (res && res.length> 0){
                    obj.fixed = 'right'
                    console.log(res.length)
                }
                var res = this.subtitle[item].displayName.match('产品编号')
                console.log('res left', res)
                if (res && res.length> 0){
                    obj.fixed = 'left'
                    console.log(res.length)
                }
                ret.push(obj)
            }
            /*
            ret.push({
                title: '接收',
                key: 'action',
                fixed: 'right',
                width: 80,
                align: 'center',
                render (row, column, index) {
                    return `<i-button type="primary" size="small" @click="receive(${index})">接收</i-button>`;
                }
            })
            ret.push({
                title: '检验',
                key: 'action',
                fixed: 'right',
                width: 80,
                align: 'center',
                render (row, column, index) {
                    return `<i-button type="primary" size="small" @click="inspect(${index})">检验</i-button>`;
                }
            })
            ret.push({
                title: '入库',
                key: 'action',
                fixed: 'right',
                width: 80,
                align: 'center',
                render (row, column, index) {
                    return `<i-button type="primary" size="small" @click="store(${index})">入库</i-button>`;
                }
            })
            */
            console.log('subtitle ', this.subtitle)
            return ret
        }
    },
    methods : {
        /*
        receive : function(index){
            console.log('receive click', index, this.equipList[index].equipment_id, this.cbset)
            if (this.equipList[index]){
                this.cbset.receiveInOne({id:this.equipList[index].equipment_id})
            }
        },
        inspect : function(index){
            console.log('inspect click', index, this.equipList[index].equipment_id, this.cbset)
            if (this.equipList[index]){
                this.cbset.inspectInOne({id:this.equipList[index].equipment_id})
            }
        },
        store : function(index){
            console.log('store click', index, this.equipList[index].equipment_id, this.cbset)
            if (this.equipList[index]){
                this.cbset.storeInOne({id:this.equipList[index].equipment_id})
            }
        },
        */
    }

}
</script>

<style>
</style>

