<template>
  <div id="app" class="ui container">
      <!--
      <div>
          <p>
          Hello, {{name}}
          </p>
      </div>
      -->
      <AppNav></AppNav>
      <!--
      <router-view></router-view>
      -->
      <AppView></AppView>
  </div>
</template>

<script>
//import Hello from './components/Hello'
import AppNav from '../frame/app-nav.vue'
import AppView from '../frame/app-view.vue'
import Home from './Home.vue'
import Toaster from './Toaster/index.vue'
import {isLogin} from '../utils/authService'

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
        Toaster
    },
    mounted(){
        /*
        console.log("app mounted")
        if (isLogin() !== true){
            this.$router.push('/login')
        }
        */
    }

}
</script>

