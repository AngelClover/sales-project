/*
export default function(router) {
    router.map ({
        '/': { 
            name: 'home',
            component: Foo
            //component: require('./components/Home.vue')
        }
    }
    )
}
*/

import Home from './components/Home.vue'
import NotFound from './components/NotFound.vue'
import BuyOrder from './components/buy/order/BuyOrder.vue'
import Finance from './components/finance/Finance.vue'
import Hello from './components/Hello.vue'
import Login from './components/login/login.vue'
import Register from './components/login/register.vue'
import Logistic from './components/logistic/Logistic.vue'
import Repair from './components/repair/Repair.vue'
import SaleOrder from './components/sale/order/SaleOrder.vue'
import SinkCompany from './components/sink/Company.vue'
import SourceCompany from './components/source/company/Company.vue'
import SourceCustomer from './components/source/customer/Customer.vue'
import SourceEquipment from './components/source/equipment/Equipment.vue'
import StoreHouse from './components/storehouse/StoreHouse.vue'

var routes = [
    //{path: '/home', component:  require('./components/Home.vue')},
    {path: '/', component:  Home},
    {path: '/home', name: 'home',  component:  Home},
    {path: '/buy', name: 'buy',  component:  BuyOrder},
    {path: '/finance', name: 'finance',  component:  Finance},
    {path: '/login', name: 'login',  component:  Login},
    {path: '/register', name: 'register',  component:  Register},
    {path: '/logistic', name: 'logistic',  component:  Logistic},
    {path: '/repair', name: 'repair',  component:  Repair},
    {path: '/sale', name: 'sale',  component:  SaleOrder},
    {path: '/sinkcompany', name: 'sinkcompany',  component:  SinkCompany},
    {path: '/sourcecompany', name: 'sourcecompany',  component:  SourceCompany},
    {path: '/sourcecustomer', name: 'sourcecustomer',  component:  SourceCustomer},
    {path: '/equipment', name: 'equipment',  component:  SourceEquipment},
    {path: '/storehouse', name: 'storehouse', component: StoreHouse},
    //{ path: '*', component: require('./components/NotFound.vue') }
    { path: '*', component: NotFound }
    
]
console.log(Home)

export default routes

/*
module.export = {
    routes
};
*/
/*
module.exports = function routeConfig(router){
    const Foo = { template: '<div>foo</div>' }
    router.map({
        '/home':{
            component: Foo
        }
    })
}
*/
