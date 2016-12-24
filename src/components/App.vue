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
      <AppView></AppView>
  </div>
</template>

<script>
//import Hello from './components/Hello'
import AppNav from '../frame/app-nav.vue'
import AppView from '../frame/app-view.vue'

export default {
    data: () => {
        return {
            name: 'app'
        }
    },
    components : {
        AppNav,
        AppView
    }

}
</script>

