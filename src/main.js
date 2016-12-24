// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
//import VueValidator from 'vue-validator'
//import { sync } from 'vuex-router-sync'
//import store from './vuex/store'
//import routes from './routes'
//import App from './App'
import App from './components/App.vue'
//import AppNav from './components/AppNav.vue'
import './semantic/dist/semantic.css'
//import './semantic/dist/semantic.js'
//

Vue.use(VueRouter)
//Vue.use(VueValidator)
//Object.keys(filters).forEach(k => Vue.filter(k, filters[k]))
/*
const router = new VueRouter({
  history: true,
  saveScrollPosition: true,
  suppressTransitionError: true
})
configRouter(router)
*/
//sync(store, router)
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }
const routes = [
      { path: '/foo', component: Foo },
      { path: '/bar', component: Bar }
]
const router = new VueRouter({
    routes
})
console.log(router);

//router.start(Vue.extend(App), '#root')
//window.router = router
const app = new Vue({
    router,
    components: {
        App
    }
}).$mount('#root')
console.log("Angel print")
console.log(app);
/*
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
*/
