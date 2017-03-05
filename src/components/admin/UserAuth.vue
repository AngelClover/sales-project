<template>
    <div>
        <div v-show="loading">
            no content
        </div>
        <div v-show="!loading">
            <table>
                <th>用户名</th>
                <!--
                <th>权限 </th>
                -->
                <!--
                <th v-for="(item,index) in userList[0].permission">
                    {{index}}
                </th>
                -->
                <th v-for="(item, index) in perList">
                    {{item.displayName}}
                </th>
                <tbody>
                    <tr v-for="user in userList" @click=clickRow(user)>
                        <td>{{user.username || user.email || user.nickname}} </td>
                        <!--<td>{{user.permission }}</td>-->
                        <!--
                        <td v-for="(item,index) in userList[0].permission">
                            {{index}}
                        </td>
                        -->
                        <td v-for="(item, index) in perList">
                            <div v-if="user.permission[item.attr]['read']">
                                <i class="checkmark icon"></i>
                            </div>
                            <div v-else>
                                <i class="remove icon"></i>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <AuthPanel :showAuthDetail=showAuthDetail :detailContent=tmpDetailContent @close="closeDetail" :perList=perList>
        </AuthPanel>
    </div>
</template>

<script>
import utils from '../../utils/utils.js'
import AuthPanel from '../../utils/AuthPanel.vue'
import us from 'underscore'
export default {
    components : {
        AuthPanel,
    },
    data: function() {
        return {
            tempItems : [],
            perList : this.getPerList(),
            showAuthDetail : false,
            detailContent : {},
            tmpDetailContent: {},
        }
    },
    computed : {
        userList() {
            return this.$store.getters.getUserList
        },
        loading(){
            if (this.userList.length > 0 && this.userList[0] && this.userList[0].permission) return false;
            else return true;
        }
    },
    created(){
        if (this.userList.length < 1){
            this.getUserInfoList()
        }
    },
    methods : {
        getUserInfoList(){
            this.$store.dispatch('getUserInfoList')
        },
        updateUserInfo(content){
            this.$store.dispatch('updateUserInfo', content)
            this.getuserinfolist()
        },
        saveUserInfo(content){
            this.$store.dispatch('saveUserInfo', content)
            this.getuserinfolist()
        },
        removeUserInfo(content){
            this.$store.dispatch('removeUserinfo', {id:content.id})
            this.getuserinfolist()
        },
        getPerList(){
            var dat = {"equipment":"设备", "enterprise":"企业", "purchase":"采购", "sale":"销售", "store":"库管", "logistic":"物流", "repair":"维修", "finance":"财务" }
            var ret = []
            for (var key in dat){
                ret.push({
                    attr: key,
                    displayName: dat[key]
                })
            }
            return ret
        },
        clickRow(item){
            this.detailContent = item
            this.tmpDetailContent = utils.deepCopy(this.detailContent)
            this.showAuthDetail = true
            console.log("underscore equal when create fake", us.isEqual(this.DetailContent, this.detailContent))
            console.log("underscore equal when create", us.isEqual(this.tmpDetailContent, this.detailContent))
        },
        closeDetail(){
            console.log("underscore equal", us.isEqual(this.tmpDetailContent, this.detailContent))
            if (us.isEqual(this.tmpDetailContent, this.detailContent)){
            }else{
                this.$store.dispatch('updateUserInfo', this.detailContent)
                this.getUserInfoList()
            }
            this.showAuthDetail = false
        }
    }
}
</script>

<style>
</style>

