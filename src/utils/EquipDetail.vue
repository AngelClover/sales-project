<template>
    <div>
        <div>
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
        <div v-if="debug==true">
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
            debug : true,
        }
    },
    props : ['equipList', 'subtitle'],
    computed : {
        titleForTable() {
            var ret = []
            ret.push({
                key : '',
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
                var res = this.subtitle[item].displayName.match('是否')
                console.log('res', res)
                if (res && res.length> 0){
                    obj.fixed = 'right'
                    console.log(res.length)
                }
                ret.push(obj)
            }
            console.log('subtitle ', this.subtitle)
            return ret
        }
    }
}
</script>

<style>
</style>

