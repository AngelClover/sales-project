<template>
  <div id="app" class="ui container">
      <!--
      <div>
          <p>
          Hello, {{name}}
          </p>
      </div>
      -->
    <app-sidebar> </app-sidebar>
      <AppNav></AppNav>
      <!--
      <router-view></router-view>
      -->
      <AppView></AppView>
      <Toaster></Toaster>
  </div>
</template>

<script>
//import Hello from './components/Hello'
import AppNav from '../frame/app-nav.vue'
import AppView from '../frame/app-view.vue'
import AppSidebar from '../frame/app-sidebar.vue'
import Home from './Home.vue'
import Toaster from './toaster/index.vue'
import {isLogin} from '../utils/authService'
//import 'sidebarjs'

export default {
    data: () => {
        return {
            name: 'app'
        }
    },
    components : {
        AppNav,
        AppView,
        Home,
        Toaster,
        AppSidebar,
    },
    mounted(){
        console.log('i mounted dropdown in app.vue')
        $('.ui .dropdown').dropdown()
    }

}
</script>

