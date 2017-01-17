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

var Foo = { template: '<div>foo</div>' }
var Bar = { template: '<div>bar</div>' }
var routes = [
    //{path: '/home', component:  require('./components/Home.vue')},
    {path: '/home', name: 'home',  component:  Home},
    {path: '/', component:  Home},
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
