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
                            <div class="accordion transition hidden">
                                <p> <router-link to="/equipment">首营设备</router-link> </p>
                                <p> <router-link to="/sourcecompany">首营企业</router-link> </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
</template>

<script>
export default {
    data : function (){
        return {
            modelList : ['home', 'buy', 'finance', 'sale', 'logistic', 'repair', 'source', 'sink', 'store']
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
