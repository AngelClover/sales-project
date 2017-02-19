<template>
    <div class="ui container">
        <div class="ui menu inverted" id="headermenu">
            <div class="header item">国泰安华</div>
            <!--
            <div class="right item" @click=logout>logout </div>
            -->
            <div class="right menu">
                <div class="ui dropdown item">
                    {{displayName}}
                    <i class="dropdown icon"></i>
                    <div class="menu">
                        <div class="divider"></div>
                        <div class="item"><p>
                            <router-link to='/userinfomodify'>资料修改</router-link>
                            </p></div>
                        <div class="divider"></div>
                        <div class="item" @click=logout>注销</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {signOut} from '../utils/authService'
export default {
    data: () => {
        return {
            name : 'app-nav'
        }
    },
    computed : {
        displayName(){
            console.log('display name', this.$store.getters.getMe)
            return this.$store.getters.getMe.username
        }
    },
    methods :{
        created(){
            //TODO ; no called
            console.log('i created dropdown')
            $('.ui .dropdown').dropdown()
        },
        mounted(){
            //TODO ; no called
            console.log('i mounted dropdown')
            $('.ui .dropdown').dropdown()
        },
        logout(){
            signOut()
            this.$store.dispatch('showMsg', '登出成功', 'success')
            this.$store.dispatch('logOut')
            console.log('wait =============>')
            setTimeout(this.$router.go('/'), 5000)
        }
    }
}
</script>

<style>
</style>
