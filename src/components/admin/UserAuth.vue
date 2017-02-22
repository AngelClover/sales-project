<template>
    <div>
        <div>
            <table>
                <th>用户名</th>
                <th>权限 </th>
                <tbody>
                    <tr v-for="user in userList">
                        <td>{{user.user.username || user.user.email}}({{user.user.nickname}}) </td>
                        <td>{{user.user.modelList}}</td>
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

