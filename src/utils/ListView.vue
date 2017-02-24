<template>
    <div>
        <slot name="titlename"> </slot>
        <div class="ui transparent left icon input">
                <input name="query" v-model="searchQuery" placeholder="Search.." type="text">
                <i class="search icon"></i>
        </div>
            <br/>
            <div class='table-container'>
        <table>
            <thead>
                <tr>
                    <!--
            <th v-for="(val, key, index) in title"> {{val}} </th>
                    -->
            <th v-for="(item, index) in preference"
                @click="sortBy(item)"
                :class="{ active : sortKey == item}" >
                {{titleMap[item] | capitalize}}
                <!--{{title[item.item] | capitalize}}-->
                <span class="arrow" :class="sortOrders[item] > 0 ? 'asc' : 'dsc'">
                </span>
            </th>
                </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in filteredContent" @click=clickItem(item)> 
                <!--
                <td v-for="(val, key, index) in title">{{item[key]}}</td>
                -->
                <td v-for="(prefitem, prefindex) in preference"> {{item[prefitem]}} </td>
            </tr>
            </tbody>
        </table>
            </div>

        <br/>
        <div class="ui buttom" align=center>
            <button @click=createAction class="ui green button"> 新建 </button>
            <button @click=showPrefs class="ui violet button"> 偏好设置 </button>
            <button @click=showLogTips class="ui red button"> 变更记录 </button>
        </div>

        <br/>

        <detail :showDetails=showDetails :detailTitle=title :detailContent=detailContent :actionType=actionType @close="showDetails = false;actionType = 'show'" :updatecb=updatecb :savecb=savecb :removecb=removecb>
        </detail>

        <Preference :showPref=showPref :oriTitle=title :location=location @close="showPref=false;">
        </Preference>

        <div v-show=debug>
        <p> -----------for debug below-------------- </p>
        <p> This is list view page.  </p>
        <p> msg : {{msg}} </p>
        <p> title : {{title}} </p>
        <p> content : {{content}} </p>
        <p> pref(pass in from props) : {{pref}} </p>
        <p> preference(final effects) : {{preference}} </p>
        <p> sortOrders : {{sortOrders}} </p>
        <p> sortKey : {{sortKey}} </p>
        <p> searchQuery : {{searchQuery}} </p>
        <p> filteredContent : {{filteredContent}} </p>
        <p> showDetails : {{showDetails}} </p>
        <p> detailContent : {{detailContent}} </p>
        </div>

    </div>
</template>

<script>
import Detail from './Detail.vue'
import Preference from './Preference.vue'

export default {
    components : {
        Detail,
        Preference
    },
    props: ['location', 'msg', 'title', 'content', 'initdata', 'pref', 'savecb', 'updatecb', 'removecb'],
    data : function(){
        return {
            sortKey : '',
            sortOrders : {},
            searchQuery : '',
            showDetails : false,
            detailContent : {},
            debug : false,
            actionType : 'show',
            showPref : false,
            clearCache : false,
        }
    },
    computed : {
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
            if (prefarray == undefined || prefarray.length == 0){
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
            //console.log('filteredContent computed')
            var sortKey = this.sortKey
            //var filterkey = this.filterkey && this.filterkey.tolowercase()
            var filterKey = this.searchQuery && this.searchQuery.toLowerCase()
            if (this.sortOrders[sortKey] == undefined){
                this.initSortOrders()
            }
            var order = this.sortOrders[sortKey] || 1
            var data = this.content
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
    },
   filters: {
       capitalize: function (str) { //TODO: why sometimes str is null
           if (str)
               return str.charAt(0).toUpperCase() + str.slice(1)
            else return str
       }
   },
   methods: {
       sortBy: function (key) {
           //console.log('sortBy', key)
           this.sortKey = key
           this.sortOrders[key] = this.sortOrders[key] * -1
       },
       initSortOrders : function(){
            var sortOrders = {}
            //console.log('listview method initSortOrders', Object.keys(this.title))
            var _this = this
            Object.keys(this.title).forEach(function (key) {
                console.log('sort key', key)

                sortOrders[_this.title[key].item] = 1
            })
            //console.log('listview method initSortOrders :', sortOrders, Object.keys(sortOrders))
            //this.$set('sortOrders', sortOrders)
            this.sortOrders = sortOrders
            return sortOrders
       },
       clickItem : function(item){
            this.detailContent = item
            this.showDetails = true
       },
       createAction(){
           this.actionType='create'
           this.showDetails = true
       },
       showLogTips(){
           this.$store.dispatch('showMsg', '此功能暂不开放', 'info')
       },
       showPrefs(){
           console.log('showPrefs', this.showPref)
           this.showPref = !this.showPref
           console.log('showPrefs', this.showPref)
       }

   }
}
</script>

<style>
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
  width: 80%;
  height:70%;
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

tr:hover td{
    background: none;
}

/*
td {
  background-color: #f9f9f9;
}
*/

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


</style>

