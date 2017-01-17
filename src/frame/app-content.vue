<template>
    <div class="ten wide column">
        <div class="ui text container">
            <!--
                <div class="header">
                <h1>main page</h1>
                </div>
                <div class="ui divider">

                </div>
                <div class="overlayer" id='iconmenu'>
                <div class="ui labeled icon menu">
                <a class="item"><i class="twitter icon"></i> Tweet</a>
                <a class="item"><i class="facebook icon"></i> Share</a>
                <a class="item"><i class="mail icon"></i> E-mail</a>
                </div>
                </div>
                <br/>
                <div class="eight wide column">

                <div class="content">
                Welcome
                </div>
                </div>
            -->
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
export default {
    methods : {
        created : () => {
        }
    }
}
</script>

<style>
</style>
