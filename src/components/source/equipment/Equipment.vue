<template>
    <div>
        <p>
            this is equipment page.
        </p>
        <p>
        added
        </p>
        <p>
        -----------ListView below----------
        </p>
        <ListView msg="asd" :title=title :content=content :pref=preference>
        </ListView>
    </div>
</template>

<script>
import ListView from '../../../utils/ListView.vue'
//import api from '../../../api'
import { getEquipmentList } from '../../../vuex/actions'
import { mapGetters, mapActions } from 'vuex'
export default {
    /*
    data : function (){
        var title = {
            "a" : "A",
            "b" : "B",
            "c" : "C",
            "d" : "D"
        }
        var content = []
        for (var i = 0; i< 10; ++i){
            var tmp = this.createContent(title, i.toString())
            content.push(tmp)
        }
        //var preference = ["a", "d", "c"]
        var preference = []
        //for (var item in title){
          //  preference.push(item)
        //}
        var tmpdata = {}
        api.getEquipment().then(function(res){
            console.log('inside res', res)
            tmpdata = res.data.data
            console.log('inside data', res.data)
            console.log('inside body', res.body)
            console.log('tmpdata inside body', tmpdata)
        }, function(res){
            console.log("get equip error")
        })

        console.log('tempdata', tmpdata)
        return {
            //title,
            //content,
            preference
        }
    },
*/
    components : {
        ListView
    },
    /*
    vuex : {
        getters : {
            title : ({equipmentList}) => equipmentList.title,
            content : ({equipmentList}) => equipmentList.content,
            preference : ({equipmentList}) => equipmentList.preference,

        },
        actions : {
            getEquipmentList
        }
    },
    */
    computed : {
    /*
        ...mapGetters([
            'title',
            'content',
            'preference'
        ])
    */
        title() {
            return this.$store.state.equipmentList.title
        },
        content() {
            return this.$store.state.equipmentList.content
        },
        preference() {
            return this.$store.state.equipmentList.preference
        }


    },
    created : function(){
        console.log('created this', this)
        //console.log(getEquipmentList)
        //if (this.$store.state.equipmentList.title.length < 1){
        if (this.$store.state.equipmentList.title.length < 1){
            this.$store.dispatch('getEquipmentList')
            //getEquipmentList()
            //getEquipmentList()
        }
    },
    methods : {
        createContent : (title, suffix)=>{
            var ret = {}
            for (var item in title){
                ret[item] = title[item] + suffix
            }
            return ret
        },
        getEquipmentList, 
        /*
        ...mapActions([
                getEquipmentList
        ])
        */
    },

}
</script>

<style>
</style>

