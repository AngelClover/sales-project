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
      <div>
          <router-link to='/home'> home </router-link>
      </div>
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

export default {
    data: () => {
        return {
            name: 'app'
        }
    },
    components : {
        AppNav,
        AppView,
        Home
    }

}
</script>

