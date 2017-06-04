<template>
    <div class='layout'>
        <div class="layout-ceiling">
            <div class="layout-ceiling-main-left" @click=sidebarToogle>
                <a> 菜单 </a>  |
            </div>
            <div class="layout-ceiling-main">
                <span>
                    {{displayName}} | 
                    <router-link to='/register'>注册</router-link> |
                    <router-link to='/login'>登录</router-link> | 
                    <a @click=logout>注销</a>
                </span>
            </div>
        </div>
    <!--
    <div class="header-wrapper" id="header-wrapper" >
    <div class="ui container">
        <div class="ui menu inverted" id="headermenu">
            <div class="header item" @click="sidebarToogle">国泰安华</div>
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
    </div>
    -->

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
        },
        sidebarToogle(){
            //$(".sidebar.left").sidebar().trigger("sidebar:toggle");
            $(".sidebar.left").sidebar('toggle');
        }
    }
}
</script>

<style>
.header-wrapper{
    background: black
}
#header-wrapper{
    background: black
}
.layout{
border: 1px solid #d7dde4;
background: #f5f7f9;
position: relative;
border-radius: 4px;
overflow: hidden;
}
.layout-logo{
width: 100px;
height: 30px;
background: #5b6270;
border-radius: 3px;
float: left;
position: relative;
top: 15px;
left: 20px;
}
.layout-header{
height: 60px;
background: #fff;
box-shadow: 0 1px 1px rgba(0,0,0,.1);
}
.layout-copy{
text-align: center;
padding: 10px 0 20px;
color: #9ea7b4;
}
.layout-ceiling{
background: #464c5b;
padding: 10px 0;
overflow: hidden;
}
.layout-ceiling-main-left{
float: left;
margin-left: 15px;
}
.layout-ceiling-main-left a{
color: #ffffff;
}
.layout-ceiling-main{
float: right;
margin-right: 15px;
    color: #ffffff;
}
.layout-ceiling-main a{
color: #ffffff;
}
</style>
