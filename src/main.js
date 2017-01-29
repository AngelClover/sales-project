// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
//import VueValidator from 'vue-validator'
import { sync } from 'vuex-router-sync'
import store from './vuex/store'
import routes from './routes'
//var routers = require('./routes')
//import App from './App'
import App from './components/App.vue'
//import AppNav from './components/AppNav.vue'
import './semantic/dist/semantic.css'
//import './semantic/dist/semantic.js'
import Home from './components/Home.vue'
import VueResource from 'vue-resource'
//

Vue.use(VueRouter)
Vue.use(VueResource)
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
const router = new VueRouter({
    routes
});
console.log(router);
sync(store, router)

//router.start(Vue.extend(App), '#root')
//window.router = router
new Vue({
    el: '#root',
    router,
    store,
    template: '<App/>',
    components: {
        App
    }
    //render: h => h(App)
    //...App
})
console.log("Angel print")
console.log(App);
console.log(app)
/*
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
*/
