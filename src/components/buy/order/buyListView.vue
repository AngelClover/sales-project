<template>
    <div>
        <slot name="titlename"> </slot>
        <div class="ui transparent left icon input">
            <input name="query" v-model="searchQuery" placeholder="Search.." type="text">
            <i class="search icon"></i>
        </div>
        <br/>
        <div class="filter label" v-show="this.filteredList.length > 0">
            <Button v-for="item in this.filteredList" class="ui button"  @click="filterByLabel(item)">
                {{item.displayName}}
            </Button>
        </div>
        <br/>
        <!--
        <table class="ui selected striped padded very basic compact table">
            <thead>
                <tr>
            <th v-for="(item, index) in preference"
                @click="sortBy(item)"
                :class="{ active : sortKey == item}" >
                {{titleMap[item] | capitalize}}
                <span class="arrow" :class="sortOrders[item] > 0 ? 'asc' : 'dsc'">
                </span>
            </th>
                </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in filteredContent" @click=clickItem(item,index)> 
                <td v-for="(prefitem, prefindex) in preference"> {{item[prefitem]}} </td>
            </tr>
            </tbody>
        </table>
        -->
                <!--
                <td><Icon type="close-round" @click=handleDelete(item,index)></Icon></td>
                -->
        <div v-if="titleKey.length > 0 && filteredContent && filteredContent.length > 0">
            <Table width="auto" :columns="titleKey" :data="filteredContent"> <!-- "put NO-Pref columns into expand" : remove @on-row-click="clickItem" by CHEN 17.6.5 --> 
            </Table>
        </div>

        <br/>
        <div class="ui buttom" align=center>
            <Button @click="createAction" > 新建 </Button>
            <Button @click="showPrefs" > 偏好设置 </Button>
            <Button @click="showLogTips" > 变更记录 </Button>
        </div>

        <br/>
        <!-- temp
        <BuyDetail :showDetails="showDetails" :detailTitle="title" :detailContent="detailContent" @close="showDetails=false;" :cbset="cbset" :storeForEquipment="stores" :location="location" :detailSubtitle="subtitle">
        </BuyDetail>
        -->
        <Creator :detailTitle="title" :showCreator="showCreator" :cbset="cbset" @close="showCreator=false;" :detailSubtitle="subtitle" :location="location">
        </Creator>

        <Preference :showPref="showPref" :oriTitle="title" :location="location" @close="showPref=false;">
        </Preference>


        <div v-show="debug">
            <p> -----------for debug below-------------- </p>
            <p> This is list view page.  </p>
            <!--
            <p> msg : {{msg}} </p>
            <p> title : {{title}} </p>
            <p> content : {{content}} </p>
            <p> pref(pass in from props) : {{pref}} </p>
            <p> preference(final effects) : {{preference}} </p>
            <p> sortOrders : {{sortOrders}} </p>
            <p> sortKey : {{sortKey}} </p>
            <p> searchQuery : {{searchQuery}} </p>
            -->
            <p> filteredContent : {{filteredContent.length}} </p>
            <p> detailContent : {{detailContent.length}} </p>
            <p> showDetails : {{showDetails}} </p>
            <p> location : {{location}} </p>
            <p> showCreator : {{showCreator}} </p>
            <p> titleKey : {{titleKey}}</p>
        </div>
        <!--
        <Table stripe :columns="testTitle" :data="testData">
        </Table>
        <Table stripe :columns="titleKey" :data="filteredContent">
        </Table>
        -->
    </div>
</template>

<script>
import BuyDetail from './buyDetail.vue'
import Preference from '../../../utils/Preference.vue'
import Creator from './Creator.vue'
import TableExpandRow from '../../../utils/TableExpandRow.vue'

export default {
    components : {
        BuyDetail,
        Preference,
        Creator,
        TableExpandRow
    },
    props: ['location', 'msg', 'title', 'content', 'initdata', 'pref', 'cbset', 'filterList', 'stores', 'subtitle'],
    data : function(){
        return {
            sortKey : '',
            sortOrders : {},
            searchQuery : '',
            detailContent : {},
            debug : false,
            showPref : false,
            clearCache : false,
            allListObj : {
                displayName : "全部",
                filtercb : obj => {return true},
            },
            labelFiltercb : obj => {return true},
            showCreator : false,
            
            showDetails : false,
            clickedIndex : -1,
        }
    },
    computed : {
        //---- "put NO-Pref columns into expand" : add expandKey for TableExpandRow template
        expandKey : function () {
            var ret = []
            var readStr = localStorage.getItem(this.location)//! conflict with computed state, cant update
            var prefobj = JSON.parse(readStr || "{}") 
            var prefarray = prefobj["pref"] || []
            for (var i in prefarray) {
                if (prefarray[i].value == false) {//only NO-Pref item get into expand
                    ret.push({
                        key : prefarray[i].item,
                        name : prefarray[i].displayName
                    })
                }
            }
            return ret
        },
        //---- by CHEN 17.6.5
        titleKey : function(){
            var ret = []
            //---- "put NO-Pref columns into expand" : add expand
            ret.push({
                type: 'expand',
                width: 70,
                render: (h, params) => {
                    return h(TableExpandRow, {
                        props: {
                            expandKey : this.expandKey,
                            row : params.row
                        }
                    })
                }
            })
            //---- by CHEN 17.6.5
            for (var i in this.preference){
                var t = {}
                t.key = this.preference[i]
                t.title = this.titleMap[t.key]
                //t.width = 100
                t.sortable = true
                ret.push(t)
            }
            //---- "put NO-Pref columns into expand" : add detail-button
            ret.push({
                title: '操作',
                key: 'action',
                width: 80,
                align: 'center',
                render: (h, params) => {
                    return h('div', [
                        h('Button', {
                            props: {
                                type: 'primary',
                                size: 'small'
                            },
                            style: {
                                marginRight: '5px'
                            },
                            on: {
                                click: () => {
                                    this.clickItem(params.row)
                                }
                            }
                        }, '查看')
                    ])
                }
            })
            //---- by CHEN 17.6.5
            //console.log('titleKey', ret)
            return ret
        },
        preference : function(){
            if (this.clearCache)localStorage.removeItem(this.location)
            var shw = this.showPref
                shw = !shw
            var readStr = localStorage.getItem(this.location)
            console.log('preference in listview refresh', readStr)
            var prefobj = JSON.parse(readStr || "{}") 
            var prefarray = prefobj["pref"] || []
            var ret = []
            console.log("preference list prefarray", prefarray)
            if (typeof(prefarray) == undefined || prefarray.length == 0){
                console.log('preference in listview branch 1', this.title)
                if (this.title && Object.values(this.title).length >= 1){ //To be better
                    for (var item in this.title){
                        ret.push(this.title[item].item)
                    }
                    console.log('preference in listview branch 2')
                }
            }else{
                console.log('preference in listview branch 3', prefarray)
                for (var item in prefarray){
                    if (prefarray[item].value == true){
                        ret.push(prefarray[item].item)
                    }
                }
            }
            console.log('preference in listview branch ret:', ret)
            return {
                ...ret
            }
        },
        titleMap : function(){
            var ret = {}
            for (var index in this.title){
                ret[this.title[index].item] = this.title[index].displayName
            }
            console.log('computed titleMap', ret)
            return ret
        },
        filteredContent : function() {
            console.log('filteredContent computed')
            var sortKey = this.sortKey
            //var filterkey = this.filterkey && this.filterkey.tolowercase()
            var filterKey = this.searchQuery && this.searchQuery.toLowerCase()
            if (typeof(this.sortOrders[sortKey]) == undefined){
                this.initSortOrders()
            }
            var order = this.sortOrders[sortKey] || 1
            var data = this.content
            var _this = this
            var tmp = this.labelFiltercb
            console.log('filteredList size: ', this.filteredList)
            if (this.filteredList.length > 0){
                console.log('label filter change the data from', data.length, '=>')
                data = data.filter(function (row){
                    console.log('consider row', row)
                    return _this.labelFiltercb(row)
                })
                console.log('label filter change the data to => ', data.length)
            }
            if (filterKey) {
                data = data.filter(function (row) {
                    return Object.keys(row).some(function (key) {
                        return String(row[key]).toLowerCase().indexOf(filterKey) > -1
                    })
                })
            }
            //console.log('sortKey ', sortKey, 'sortorder', order)
            if (sortKey) {
                data = data.slice().sort(function (a, b) {
                    a = a[sortKey]
                    b = b[sortKey]
                    return (a === b ? 0 : a > b ? 1 : -1) * order
                })
            }
            //console.log('filteredContent computed end')
            return data
        },
        filteredList : function(){
            var ret = []
            if (this.filterList && this.filterList.length > 0){
                ret.push(this.allListObj)
            }
            for (var key in this.filterList){
                ret.push(this.filterList[key])
            }
            return ret
        },
    },
   filters: {
       capitalize: function (str) { //TODO: why sometimes str is null
           if (str)
               return str.charAt(0).toUpperCase() + str.slice(1)
            else return str
       }
   },
    watch : {
        filteredContent : function(x){
            if (this.clickedIndex >= 0 && this.clickedIndex < this.filteredContent.length){
                this.detailContent = x[this.clickedIndex]
            }else {
                this.showDetails = false
            }
        },
        content : function(x){
        }
    },
    created : function(){
        console.log('created this', this)
        if (this.$store.state.sourceCompanyList.title.length < 1){
//            this.$store.dispatch('getSourceCompanyList')
        }
    },
   methods: {
        sortBy : function(key) {
           //console.log('sortBy', key)
           this.sortKey = key
           this.sortOrders[key] = this.sortOrders[key] * -1
        },
        initSortOrders : function() {
            var sortOrders = {}
            //console.log('listview method initSortOrders', Object.keys(this.title))
            var _this = this
            Object.keys(this.title).forEach(function (key) {
                //console.log('sort key', key)

                sortOrders[_this.title[key].item] = 1
            })
            //console.log('listview method initSortOrders :', sortOrders, Object.keys(sortOrders))
            //this.$set('sortOrders', sortOrders)
            this.sortOrders = sortOrders
            return sortOrders
        },
        clickItem : function(item) { //item, index
            console.log('on-row-click 1',  item)
            this.detailContent = item //this.filteredContent[index]
            var i = -1;
             for (var ind in this.filteredContent){
                if (this.filteredContent[ind].id == item.id){
                i = ind
             break
                 }
             }
            this.clickedIndex = i
            console.log('on-row-click 2', this.clickedIndex,  item)
            this.showDetails = true

            //---- "separate BuyDetail from BuyListView's modal" : emit clickShowDetail-event when click item
            this.$emit('clickShowDetail', item)
            //---- by CHEN 17.6.6
       },
       createAction(){
           this.detailContent = {}
           this.showCreator = true
           this.$store.dispatch('getEquipmentList')
       },
       showLogTips(){
           this.$store.dispatch('showMsg', '此功能暂不开放', 'info')
       },
       showPrefs(){
           console.log('showPrefs', this.showPref)
           this.showPref = !this.showPref
           console.log('showPrefs', this.showPref)
       },
       handleDelete : function(item, index){
           this.cbset.delete(item)
       },
       filterByLabel(obj){
           console.log('filterByLabel', obj, 'filteredList.length : ', this.filteredList.length)
           this.labelFiltercb = obj.filtercb
       },
       mounted(){
           $('table').tablesort()
            this.$store.dispatch('getEquipmentList')
            this.$store.dispatch('getSourceCompanyList')
       },
   }
}
</script>

<style>
/*
table {
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
  margin-left:auto;
  margin-right:auto;
}

.table-container{
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
  width: 100%;
  height:90%;
  overflow: scroll;
}

th {
  background-color: #42b983;
  color: rgba(255,255,255,0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

tr {
    cursor: pointer;
}
tr:hover{
    background-color: #42b983!important;
}

table tr:nth-child(odd){
    background: #ccc;
}
table tr:hover tr:nth-child(odd){
    background: none;
}
*/

/*
tr:hover td{
    background: none;
}
*/

/*
td {
  background-color: #f9f9f9;
}
*/

/*
td:hover{
    background-color: #32a963!important;
}

th, td {
  min-width: 120px;
  padding: 10px 20px;
}

th.active {
  color: #fff;
}

th.active .arrow {
  opacity: 1;
}
*/

/*
.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-left: 5px;
  opacity: 0.66;
}

.arrow.asc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.arrow.dsc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
}
*/

/*
td{
    color : #666;
    background-color : #aaa;
}
.ivu-table{
    background-color : #aaa;
}
.ivu-table-cell{
    background-color : #bbb;
    color : #111;
    font-color : #444;
}
                    */

</style>

