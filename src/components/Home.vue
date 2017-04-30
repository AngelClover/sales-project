<template>
    <div>
    <Row>
    <br/>
        <h1 class=hellotext style="margin:20px">
            欢迎光临，请点击左上角菜单或者下方图标开始。 <br/>
        </h1>
    </Row>
    <Row>
    <Card style="width:220px;margin:20px;display:inline-block">
    <router-link to="/buy">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>采购订单</h3>
    </div>
    </router-link>
    </Card>

    <Card style="width:220px;margin:20px;display:inline-block">
    <router-link to="/sale">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>销售订单</h3>
    </div>
    </router-link>
    </Card>

    <Card style="width:220px;margin:20px;display:inline-block">
    <router-link to="/equipment">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>首营设备</h3>
    </div>
    </router-link>
    </Card>

    <Card style="width:220px;margin:20px;display:inline-block">
    <router-link to="/storehouse">
    <div style="text-align:center">
        <img src="../../images/logo.png">
        <h3>仓库管理</h3>
    </div>
    </router-link>
    </Card>

    </Row>
</template>

<script>
export default {
    data: () => {
        return {}
    }
}
</script>
