<!-- 
    a template for tables
    to hide the extra columns/info into expand-colunm
-->

<template>
    <div>
        <Row v-for="r in formedRows" class="expand-row">
            <Col v-for="c in r" span="6">
                <span class="expand-key">{{c.key + '：'}}</span>
                <span class="expand-value">{{c.value}}</span>
            </Col>
        </Row>
    </div>
</template>

<script>
export default {
    props : ['expandKey','row'],
    computed : {
        formedRows : function () {
            var keys = this.expandKey
            var data = this.row
            var ret = []
            var row = []
            //console.log('CHEN','expandKey', this.expandKey)
            for (var i in keys) {
                if (row.length >= 4) {
                    ret.push(row)
                    row = []
                }
                else {
                    row.push({
                        key : keys[i].name,
                        value : data[keys[i].key]
                    })
                }
            }
            if (row.length > 0) {
                ret.push(row)
            }
            //console.log('CHEN','ret', ret)
            return ret;
        }
    },
}
</script>

<style>
    .expand-row{
        margin-bottom: 16px;
    }
    .expand-key{
        color: #888;
    }
</style>