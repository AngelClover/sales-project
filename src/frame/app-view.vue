<template>
    <div class="ui grid">
        <app-sidebar> </app-sidebar>
        <app-content> </app-content>
        <!--
        <div class="three wide column overlay">
            <div class="ui styled accordion">
                <div class="title">
                    <i class="ui dropdown icon"></i>
                    labal 1
                </div>
                <div class="content">
                    <div class="accordion transition hidden">
                        <p> 1.1 </p>
                        <p> 1.2 </p>
                    </div>
                </div>
                <div class="title">
                    label 2
                </div>
                <div class="title">
                    label 3
                </div>
            </div>
        </div>
            <div class="ten wide column">
                <div class="ui text container">
                    <router-view>
                </div>
            </div>
        -->
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
