<template>
    <div >
        <Row>
        <div class="layout-breadcrumb">
            <Breadcrumb>
            <Breadcrumb-item href="#">首页</Breadcrumb-item>
            <Breadcrumb-item>{{displayLocationName}}</Breadcrumb-item>
            </Breadcrumb>
        </div>
        </Row>
        <br/>
        <Row type=flex>
        <app-content> </app-content>
        </Row>
        <br/>
        <Row>
            <Col span=24>
        <center>
            <div class="layout-copy">
                <p>
                2017 &copy; 天津市汇天利商贸有限公司
                </p>
            </div>
        </center>
            </Col>
        </Row>
    </div>
</template>

<script>
import AppSidebar from './app-sidebar.vue'
import AppContent from './app-content.vue'

export default {
    components : {
        AppSidebar,
        AppContent
    },
    data(){
        return {
            displayLocationName : "当前页面",
            transDict : {
                'sale' : "销售管理",
                'buy' : "采购管理",
                'equipment' : "首营设备管理",
                'sourcecompany' : "首营企业管理",
                'storehouse' : "仓库管理",
                'repair' : "维修管理",
                'logistic' : "物流管理",
                'finance' : "财务管理",
                'administer' : "用户权限管理",
            }
        }
    },
    computed : {
        displayName : function(){
            var path = this.$store.state.route.path
            for (var item in this.transDict){
                if (path == item)
                    this.displayLocationName = this.transDict[item]
            }
            console.log("breadcump ", path, "->", this.displayLocationName)
            return this.displayLocationName
        },
        routeName() {
            console.log('bread')
            return this.$store.state.route.path
        }
    }
}

</script>

<style>
.layout-breadcrumb{
    padding: 30px 15px 0;
}
.layout-copy{
    text-align: center;
    padding: 10px 0 20px;
    color: #9ea7b4;
}
.clear{ clear:both} 
</style>
