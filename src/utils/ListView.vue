<template>
    <div>
        <table>
            <thead>
                <tr>
                    <!--
            <th v-for="(val, key, index) in title"> {{val}} </th>
                    -->
            <th v-for="(item, index) in preference"> {{title[item]}} </th>
                </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in content"> 
                <!--
                <td v-for="(val, key, index) in title">{{item[key]}}</td>
                -->
                <td v-for="(prefitem, prefindex) in preference"> {{item[prefitem]}} </td>
            </tr>
            </tbody>
        </table>


        <br/>

        <p> -----------for debug below-------------- </p>
        <p> This is list view page.  </p>
        <p> msg : {{msg}} </p>
        <p> title : {{title}} </p>
        <p> content : {{content}} </p>
        <p> pref(pass in from props) : {{pref}} </p>
        <p> preference(final effects) : {{preference}} </p>

    </div>
</template>

<script>
export default {
    props: ['msg', 'title', 'content', 'initdata', 'pref'],
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
        }
    }
}
</script>

<style>
</style>

