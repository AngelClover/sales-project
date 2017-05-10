<template>
    <div>
    <Row>
    <br/>
        <h1 class=hellotext style="margin:20px">
            欢迎光临，请点击左上角菜单或者下方图标开始。 <br/>
        </h1>
    </Row>
                    <div v-if="userInfo.module">
    <Row>
    <Card style="width:220px;margin:20px;display:inline-block" v-show="userInfo.module.indexOf('purchase') >= 0">
    <router-link to="/buy">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>采购订单</h3>
    </div>
    </router-link>
    </Card>

    <Card style="width:220px;margin:20px;display:inline-block" v-show="userInfo.module.indexOf('sale') >= 0">
    <router-link to="/sale">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>销售订单</h3>
    </div>
    </router-link>
    </Card>

    <Card style="width:220px;margin:20px;display:inline-block" v-show="userInfo.module.indexOf('equipment') >= 0">
    <router-link to="/equipment">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>首营设备</h3>
    </div>
    </router-link>
    </Card>

    <Card style="width:220px;margin:20px;display:inline-block" v-show="userInfo.module.indexOf('store') >= 0">
    <router-link to="/storehouse">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>仓库管理</h3>
    </div>
    </router-link>
    </Card>

    <div v-if="userInfo.module.length < 1">
        <h1 style="margin:20px">
        你好像没有权限，请适当联系管理员。
        </h1>
    </div>

    </Row>
                    </div>
                    <div v-else>
                        <h1 style="margin:20px">
                        获取不到你的权限，请适当联系管理员。
                        </h1>>
                    </div>
    </div>
</template>

<script>
export default {
    data: () => {
        return {}
    },
    computed : {
        userInfo : function(){
            console.log('userInfo ', this.$store.getters.getMe)
            return this.$store.getters.getMe || {module:[]}
        }
    },
}
</script>
