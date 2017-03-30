<template>
        <!--
            <p>
            sidebar
            </p>
        -->
        <!--
            <div class="ui vertical sidebar three wide column overlay left">
        -->
            <div class="ui vertical inverted sidebar menu left leftmenu">
                <!--
                <div class="ui styled accordion">
                -->
                    <!--
                    <div class="title">
                        <i class="ui dropdown icon"></i> labal 1
                    </div>
                    <div class="content">
                        <div class="accordion transition hidden">
                            <p> 1.1 </p>
                            <p> 1.2 </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('home') >= 0" class=title>
                    -->
                <Menu theme="light" width=auto>
                    <Menu-item class=title name=home>
                        <p> <router-link to="/home"> Home </router-link> </p>
                    </Menu-item>
                    <Submenu v-show="userInfo.module.indexOf('equipment') >= 0">
                            <Icon type="IOS paper"></Icon> 首营审批
                            <Menu-item name=equipment>
                                <p> <router-link to="/equipment">首营设备</router-link> </p>
                            </Menu-item>
                            <Menu-item name=sourcecompany>
                                <p> <router-link to="/sourcecompany">首营企业</router-link> </p>
                            </Menu-item>
                    </Submenu>
                    <Menu-item v-show="userInfo.module.indexOf('purchase') >= 0" name=buy>
                        <div class="title">
                            <p> <router-link to="/buy"> 采购订单管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('sale') >= 0" name=sale>
                        <div class="title">
                            <p> <router-link to="/sale"> 销售订单管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('store') >= 0" name=store>
                        <div class="title">
                            <p> <router-link to="/storehouse"> 仓库管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('repair') >= 0" name=repair>
                        <div class="title">
                            <p> <router-link to="/repair"> 维修管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('logistic') >= 0" name=logistic>
                        <div class="title">
                            <p> <router-link to="/logistic"> 物流管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('finance') >= 0" name=finance>
                        <div class="title">
                            <p> <router-link to="/finance"> 财务管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('administer') >= 0" name=administer>
                        <div class="title">
                            <p> <router-link to="/userauth"> 用户权限管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <!--
                </div>
                    -->
                </Menu>
            </div>
</template>

<script>
//import '../semantic/dist/semantic.min.css'
//import '../semantic/dist/semantic.min.js'
export default {
    data : function (){
        return {
            //module : ['home', 'buy', 'finance', 'sale', 'logistic', 'repair', 'source', 'sink', 'store']
            //module : ['home', 'buy', 'sale', 'logistic', 'repair', 'source', 'sink', 'storehouse']
        }
    },
    computed : {
        userInfo : function(){
            console.log('userInfo ', this.$store.getters.getMe)
            return this.$store.getters.getMe || {module:[]}
        }
    },
    created (){
        console.log('userinfo', this.userInfo.module)
        /*
        $('.accordion') .accordion({
                selector: {
                    trigger: '.title .icon'
                }
            })
        ;
        */
        //$('#triggereg').accordion()
    }
}
</script>

<style>
.sidebar.left {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
}
.sidebars > .sidebar {
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.64);
    position: fixed;
    color: white;
    padding: 30px;
    font-size: 2em;
    text-align: center;
}
.title .p{
    color:#ffffff;
}
</style>
