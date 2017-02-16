<template>
    <div>
        <!--<view-router></view-router>-->
    <Toaster></Toaster>
    </div>
</template>

<script>
import Toaster from './Toaster/index.vue'
import {isLogin} from '../utils/authService'
export default {
    data: function() {
        return {}
    },
    components : {
        Toaster
    },
}
</script>

<style>
</style>

