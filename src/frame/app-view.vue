<template>
    <div class="ui grid">
        <app-sidebar> </app-sidebar>
        <app-content> </app-content>
    </div>
</template>

<script>
import AppSidebar from './app-sidebar.vue'
import AppContent from './app-content.vue'

export default {
    components : {
        AppSidebar,
        AppContent
    }
}

</script>

<style>
</style>
