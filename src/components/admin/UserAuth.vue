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
            //attr: ["read", "write", "approve"],
        }
    },
    computed : {
        userList() {
            return this.$store.getters.getUserList
        },
        loading(){
            if (this.userList.length > 0 && this.userList[0] && this.userList[0].permission) return false;
            else return true;
        },
        permissionList(){
            return this.$store.getters.getPermissionList
        }
    },
    created(){
        if (this.userList.length < 1){
            this.getUserInfoList()
        }
        //if (this.$store.getPermissionList < 1){
            this.$store.dispatch('getPermissionList')
        //}
    },
    methods : {
        getUserInfoList(){
            this.$store.dispatch('getUserInfoList')
        },
        updateUserInfo(content){
            this.$store.dispatch('updateUserInfo', content)
            this.getUserInfoList()
        },
        saveUserInfo(content){
            this.$store.dispatch('saveUserInfo', content)
            this.getUserInfoList()
        },
        removeUserInfo(content){
            this.$store.dispatch('removeUserinfo', {id:content.id})
            this.getUserInfoList()
        },
        getPerList(){
            var dat = {"equipment":"设备", "enterprise":"企业", "purchase":"采购", "sale":"销售", "store":"库管", "logistic":"物流", "repair":"维修", "finance":"财务", "customer": "客户" }
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
            //this.tmpDetailContent = utils.deepCopy(this.detailContent)
            //this.tmpDetailContent = us.pick(this.detailContent, "permission")
            this.tmpDetailContent = utils.deepClone(this.detailContent)
            this.showAuthDetail = true
        },
        closeDetail(){
            console.log("underscore equal", us.isEqual(this.tmpDetailContent, this.detailContent))
            if (us.isEqual(this.tmpDetailContent, this.detailContent)){
                console.log("closedetail for equal, no need to send request")
            }else{
                var payload = this.tmpDetailContent
                console.log("underscore info detail payload", JSON.stringify(payload))
                this.addAuth(this.tmpDetailContent, this.detailContent)
                this.removeAuth(this.tmpDetailContent, this.detailContent)
                //this.$store.dispatch('updateUserInfo', payload)
            }
            //setTimeout(this.getUserInfoList(), 5000) //But no use....
            this.showAuthDetail = false
        },
        addAuth(target, source){
            var payload = {
                "permissions" : []
            }
            //console.log("permissionList in getters", this.permissionList)
            for (var index in this.permissionList){
                var key = this.permissionList[index][0]
                for(var at in this.permissionList[index][1]){
                    if (target.permission[key][at] && !source.permission[key][at]){
                        payload.permissions.push(this.permissionList[index][1][at])
                    }
                }
            }
            if (payload.permissions.length > 0){
                payload.id = target.id //userid
                console.log('add Auth', payload)
                this.$store.dispatch('addPermissions', payload)
            }
        },
        removeAuth(target, source){
            var payload = {
                "permissions" : []
            }
            //console.log("permissionList in getters", this.permissionList)
            for (var index in this.permissionList){
                var key = this.permissionList[index][0]
                for(var at in this.permissionList[index][1]){
                    if (!target.permission[key][at] && source.permission[key][at]){
                        payload.permissions.push(this.permissionList[index][1][at])
                    }
                }
            }
            if (payload.permissions.length > 0){
                payload.id = target.id //userid
                console.log('remove Auth', payload)
                this.$store.dispatch('removePermissions', payload)
            }
        }
    }
}
</script>

<style>
</style>

