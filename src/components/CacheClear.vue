<template>
    <div align=center class="cacheclear">
        <button @click=clear class='ui primary button'>
            clear
        </button>
        <div v-show=show>
            cache cleared.
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            show:false
        }
    },
    methods :{
        clear(){
            localStorage.clear()
            console.log('localStorage clear')
            this.$store.dispatch('showMsg', 'cache clear', 'success')
            this.show = !this.show
        },
        mounted(){
            this.clear()
        }
    }
}
</script>

<style>
.cacheclear{
    margin:100px;
}
</style>

