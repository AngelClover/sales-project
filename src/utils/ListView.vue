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
                {{title[item].name | capitalize}}
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
            <button @click=createAction> + </button>
            <button @click=showLogTips> log </button>
        </div>

        <br/>

        <detail :showDetails=showDetails :detailTitle=title :detailContent=detailContent :actionType=actionType @close="showDetails = false;actionType = 'show'" :updatecb=updatecb :savecb=savecb :removecb=removecb>
        </detail>

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

export default {
    components : {
        Detail
    },
    props: ['msg', 'title', 'content', 'initdata', 'pref', 'savecb', 'updatecb', 'removecb'],
    /*
    data : function() {
        var preference = []
        if (this.pref == undefined || this.pref.length == 0){
            if (this.title && this.title.length > 1){
                for (var item in this.title){
                    preference.push(item)
                }
            }
        }else{
            preference = pref
        }
        return {
            preference
        }
    },
    */
    data : function(){
        return {
            sortKey : '',
            sortOrders : {},
            searchQuery : '',
            showDetails : false,
            detailContent : {},
            debug : false,
            actionType : 'show'
        }
    },
    computed : {
        preference : function(){
            console.log('preference in listview refresh', this)
            var ret = []
            if (this.pref == undefined || this.pref.length == 0){
                console.log('preference in listview branch 1', this.title)
                if (this.title && Object.values(this.title).length >= 1){ //To be better
                    for (var item in this.title){
                        ret.push(item)
                    }
                    console.log('preference in listview branch 2')
                }
            }else{
                console.log('preference in listview branch 3')
                ret = this.pref
            }
            console.log('preference in listview branch ret:', ret)
            return {
                ...ret
            }
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
       capitalize: function (str) {
           return str.charAt(0).toUpperCase() + str.slice(1)
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
            Object.keys(this.title).forEach(function (key) {
                sortOrders[key] = 1
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
    background-color: #42b983;
}

/*
tr:hover td{
    background: none;
}

td {
  background-color: #f9f9f9;
}
*/

td:hover{
    background-color: #32a963
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

