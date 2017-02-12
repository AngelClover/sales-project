<template>
    <div class="ui container">
        <div class="ui menu inverted" id="headermenu">
            <div class="header item">Angela</div>
            <div class="right item" @click=logout>logout </div>
            <div class="right menu">
                <div class="ui dropdown item">
                    用户username
                    <i class="dropdown icon"></i>
                    <div class="menu">
                        <div class="item">签到</div>
                        <div class="divider"></div>
                        <div class="item">erp信息</div>
                        <div class="item">工作日记</div>
                        <div class="divider"></div>
                        <div class="item">注销</div>
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
    methods :{
        logout(){
            signOut()
            this.$router.go('/')
        }
    }
}
</script>

<style>
</style>
