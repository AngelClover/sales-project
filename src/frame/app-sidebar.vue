<template>
        <!--
            <p>
            sidebar
            </p>
        -->
            <div class="three wide column overlay">
                <div class="ui styled accordion">
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
                    <div class=title>
                        <p>
                        <router-link to="/home">
                            Home
                        </router-link>
                        </p>
                    </div>
                    <div v-show="userInfo.module.indexOf('equipment') >= 0">
                        <div id="triggereg" class="accordion">
                            <div class="active title">
                                <i class="ui dropdown icon"></i> 首营审批
                            </div>
                            <div class="active content">
                                <div class="accordion transition ">
                                    <p> <router-link to="/equipment">首营设备</router-link> </p>
                                    <p> <router-link to="/sourcecompany">首营企业</router-link> </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('purchase') >= 0">
                        <div class="title">
                            <p> <router-link to="/buy"> 采购订单管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('sale') >= 0">
                        <div class="title">
                            <p> <router-link to="/sale"> 销售订单管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('store') >= 0">
                        <div class="title">
                            <p> <router-link to="/storehouse"> 仓库管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('repair') >= 0">
                        <div class="title">
                            <p> <router-link to="/repair"> 维修管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('logistic') >= 0">
                        <div class="title">
                            <p> <router-link to="/logistic"> 物流管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('finance') >= 0">
                        <div class="title">
                            <p> <router-link to="/finance"> 财务管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="userInfo.module.indexOf('administer') >= 0">
                        <div class="title">
                            <p> <router-link to="/userauth"> 用户权限管理 </router-link> </p>
                        </div>
                    </div>
                </div>
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
</style>
