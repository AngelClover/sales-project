<template>
        <!--
            <p>
            sidebar
            </p>
        -->
            <div class="three wide column overlay">
                <div class="ui styled accordion">
                    <div class="title">
                        <i class="ui dropdown icon"></i> labal 1
                    </div>
                    <div class="content">
                        <div class="accordion transition hidden">
                            <p> 1.1 </p>
                            <p> 1.2 </p>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('home') >= 0" class=title>
                        <p>
                        <router-link to="/home">
                            Home
                        </router-link>
                        </p>
                    </div>
                    <div v-show="modelList.indexOf('source') >= 0">
                        <div class=title>
                            <i class="ui dropdown icon"></i> 首营审批
                        </div>
                        <div class=content>
                            <div class="accordion transition ">
                                <p> <router-link to="/equipment">首营设备</router-link> </p>
                                <p> <router-link to="/sourcecompany">首营企业</router-link> </p>
                            </div>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('buy') >= 0">
                        <div class="title">
                            <p> <router-link to="/buy"> 采购订单管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('sale') >= 0">
                        <div class="title">
                            <p> <router-link to="/sale"> 销售订单管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('storehouse') >= 0">
                        <div class="title">
                            <p> <router-link to="/storehouse"> 仓库管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('repair') >= 0">
                        <div class="title">
                            <p> <router-link to="/repair"> 维修管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('logistic') >= 0">
                        <div class="title">
                            <p> <router-link to="/logistic"> 物流管理 </router-link> </p>
                        </div>
                    </div>
                    <div v-show="modelList.indexOf('finance') >= 0">
                        <div class="title">
                            <p> <router-link to="/finance"> 财务管理 </router-link> </p>
                        </div>
                    </div>
                </div>
            </div>
</template>

<script>
export default {
    data : function (){
        return {
            //modelList : ['home', 'buy', 'finance', 'sale', 'logistic', 'repair', 'source', 'sink', 'store']
            modelList : ['home', 'buy', 'sale', 'logistic', 'repair', 'source', 'sink', 'store']
        }
    },
    computed : {
        renderHome : function(){
            console.log("modelList", this.modelList)
            console.log("indexOf", this.modelList.indexOf('Home'))
                return this.modelList.indexOf('Home') >= 0
        }
    }
}
</script>

<style>
</style>
