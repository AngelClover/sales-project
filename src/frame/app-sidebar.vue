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
                <Menu theme="light" width=auto :open-names="openNames">
                    <Menu-item class=title name=home>
                        <p> <router-link to="/home"> Home </router-link> </p>
                    </Menu-item>
                    <div v-if="userInfo.module">
                    <Submenu v-show="userInfo.module.indexOf('equipment') >= 0" name="source">
                        <template slot="title"> <p>首营审批</p> </template>
                        <Menu-item name=equipment>
                            <p> <router-link to="/equipment"><Icon type="checkmark-circled"></Icon>首营设备</router-link> </p>
                        </Menu-item>
                        <Menu-item name=sourcecompany>
                            <p> <router-link to="/sourcecompany"> <Icon type="person-stalker"></Icon> 首营企业</router-link> </p>
                        </Menu-item>
                    </Submenu>
                        <Menu-item name=sourcecustomer>
                            <p> <router-link to="/sourcecustomer"> <Icon type="person-stalker"></Icon> 客户管理</router-link> </p>
                        </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('purchase') >= 0" name=buy>
                        <div class="title">
                            <p> <router-link to="/buy"><Icon type="archive"></Icon> 采购订单管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('sale') >= 0" name=sale>
                        <div class="title">
                            <p> <router-link to="/sale"><Icon type="forward"></Icon> 销售订单管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('store') >= 0" name=store>
                        <div class="title">
                            <p> <router-link to="/storehouse"> <Icon type="cube"></Icon> 仓库管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('repair') >= 0" name=repair>
                        <div class="title">
                            <p> <router-link to="/repair"> <Icon type="wrench"></Icon> 维修管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('logistic') >= 0" name=logistic>
                        <div class="title">
                            <p> <router-link to="/logistic"><Icon type="model-s"></Icon> 物流管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('finance') >= 0" name=finance>
                        <div class="title">
                            <p> <router-link to="/finance"> <Icon type="social-usd"></Icon>  财务管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item v-show="userInfo.module.indexOf('administer') >= 0" name=administer>
                        <div class="title">
                            <p> <router-link to="/userauth"> <Icon type="person"></Icon> 用户权限管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    <Menu-item name=upload>
                        <div class="title">
                            <p> <router-link to="/upload"> <Icon type="file"></Icon> 上传文件管理 </router-link> </p>
                        </div>
                    </Menu-item>
                    </div>
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
            openNames : ['source']
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
.title .p .a{
    color:#ffffff;
}
</style>
