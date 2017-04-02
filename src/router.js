import Vue from 'vue'
import VueRouter from 'vue-router'
import { sync } from 'vuex-router-sync'
import store from './vuex/store'
import routes from './routes'
import {isLogin} from './utils/authService'

Vue.use(VueRouter)
const router = new VueRouter({
    routes
});
console.log(router);
sync(store, router)
router.beforeEach(function (to, from, next){
    //vm = transition.to.router.app.$root
    console.log('router in', from.path, '->', to.path)
    if (to.path == '/login' && isLogin()){
        console.log('router in /', from.path, '->', to.path)
        next('/')
    }
    if (isLogin() || to.path == '/login' || to.path == '/register'){
        next()
    }else{
        next(isLogin() ? '/' : '/login')
    }
})
router.afterEach(route => {
    $(".sidebar.left").sidebar('hide')
})

export default router
