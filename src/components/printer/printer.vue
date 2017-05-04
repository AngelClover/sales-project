<template>
    <div class="printer-wrapper">
        <h1 id="printName">天津市国泰安华医用技术发展有限公司备货单</h1>
        <br/>
        <div>
            <h5 class='pos2-1'> 生化 </h5> 
            <h5 class='pos2-2'>送货单号：XXXXXX</h5>
        </div>
        <table border=1 class="printer-table" width=790px>
            <tr>
            <th width=50px class="printer-table-header"> 产品编码 </th>
            <th width=100px class="printer-table-header"> 产品名称 </th>
            <th width=50px class="printer-table-header"> 名称简称 </th>
            <th width=30px class="printer-table-header"> 单位 </th>
            <th width=30px class="printer-table-header"> 数量 </th>
            <th width=50px class="printer-table-header"> 规格 </th>
            <th width=50px class="printer-table-header"> 单价 </th>
            <th width=50px class="printer-table-header"> 总价 </th>
            <th width=90px class="printer-table-header"> 生产厂家 </th>
            <th width=90px class="printer-table-header"> 生产日期 </th>
            <th width=50px class="printer-table-header"> 批号 </th>
            <th width=50px class="printer-table-header"> 有效期 </th>
            <th width=90px class="printer-table-header"> 注册证号 </th>
            </tr>
            <tr v-for="it in gotData.equipments">
                <td class="printer-table-content"> {{it.equipment_id}}</td>
                <td class="printer-table-content"> {{it.product_name}}</td>
                <td class="printer-table-content"> {{it.abbr}}</td>
                <td class="printer-table-content"> {{it.measurement_unit}}</td>
                <td class="printer-table-content"> {{it.quantity}}</td>
                <td class="printer-table-content"> {{it.model}}</td>
                <td class="printer-table-content"> {{it.unit_price}}</td>
                <td class="printer-table-content"> {{it.total_price}}</td>
                <td class="printer-table-content"> {{it.producer}}</td>
                <td class="printer-table-content"> 生产日期</td>
                <td class="printer-table-content"> 批号</td>
                <td class="printer-table-content"> {{it.warranty_period}}</td>
                <td class="printer-table-content"> 注册证号</td>
            </tr>
        </table>
        <br/>
        <h5 class="pos2-1"> 合计总价: {{gotData.total_price}} </h5>
        <br/>
        <h5 class="pos4-1"> 出库时间: </h5> 
        <h5 class="pos4-2"> 出库温度: </h5> 
        <h5 class="pos4-3"> 到货时间: </h5> 
        <h5 class="pos4-4"> 到货温度: </h5> 
        <br/>
        <h5 class="pos4-1"> 制单：</h5>
        <h5 class="pos4-2"> 仓管员：</h5>
        <h5 class="pos4-3"> 复核：</h5>
        <h5 class="pos4-4"> 收货方（质检员）签字：</h5>
        <div v-if=debug>
            <br/>
            id : {{ $route.params.id }}
            <br/>
            printData : {{printData}}
            <br/>
            gotData : {{gotData}}
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            printData : {
            },
            debug : false,
        }
    },
    computed : {
        gotData : function(){
            console.log('gotdata refresh', this.$route.params.id)
            var content = this.$store.getters.saleOrderContent
            for (var cc of content){
                console.log('cc.id', cc.id)
                if (cc.id == this.$route.params.id)return cc
            }
            return undefined
        }
    },
    methods : {
        created : function(){
           this.$store.dispatch('getSaleOrderList') 
        }
    }
}
</script>

<style lang="less">
/*
五联纸
 a5(148mm x 210mm) .
 => 559 x 794
*/
@length: 790px;
@height: 555px;
@leftdiff: 40px;
.printer-wrapper{
    width: @length;
    height: @height;
    margin: 2px;
}
#printName {
    color: #000;
    font: bold 26px/26px 'microsoft yahei';
    text-align: center;
    margin: 20px;
    margin-left: 0;
}
.printer-table{
    table-layout: fixed;
}
th.printer-table-header{
    color: #000;
    font-family: 'Microsoft Yahei';
    font-size: 12px;
    font-weight: bold;
    table-layout: fixed;
}
td.printer-table-content{
    color: #000;
    font-family: 'Microsoft Yahei';
    font-size: 12px;
    vertical-align: top;
}
h5.pos2-1{
    display: inline-block;
    color: #000;
    font: 16px/16px 'microsoft yahei';
}
h5.pos2-2{
    display: inline-block;
    position:absolute;
    left:@length/2 - @leftdiff;
    color: #000;
    font: 16px/16px 'microsoft yahei';
}
h5.pos4-1{
    display: inline-block;
    color: #000;
    font: 16px/16px 'microsoft yahei';
}
h5.pos4-2{
    display: inline-block;
    position:absolute;
    left:@length/4 - @leftdiff;
    color: #000;
    font: 16px/16px 'microsoft yahei';
}
h5.pos4-3{
    display: inline-block;
    position:absolute;
    left:@length*2/4 - @leftdiff*2;
    color: #000;
    font: 16px/16px 'microsoft yahei';
}
h5.pos4-4{
    display: inline-block;
    position:absolute;
    left:@length*3/4 - @leftdiff*3;
    color: #000;
    font: 16px/16px 'microsoft yahei';
}
</style>

