<template>
    <div>
        <div>
            <table>
                <th>用户名</th>
                <th>权限 </th>
                <th v-for="per in userList[0].permission">
                <tbody>
                    <tr v-for="user in userList">
                        <td>{{user.username || user.email || user.nickname}} </td>
                        <td>{{user.permission }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            tempItems : []
        }
    },
    computed : {
        userList() {
            return this.$store.getters.getUserList
        },
        authList() {
            var ret = []
            for (var i in user){
                ret.push(user[i].permission)
            }
        }
    },
    created(){
        if (this.userList.length < 1){
            this.$store.dispatch('getUserInfoList')
        }
    },
    methods : {
    }
}
</script>

<style>
</style>

