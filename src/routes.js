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

const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }
const routes = [
      { path: '/foo', component: Foo },
      { path: '/bar', component: Bar }
]

module.export = {
    routes
};
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
