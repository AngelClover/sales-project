<template>
    <div>
        <vue-toast ref='toast'></vue-toast>
    </div>
</template>

<script>
import 'vue-toast/dist/vue-toast.min.css'
import VueToast from 'vue-toast'

export default {
    data: function() {
        return {}
    },
    components: { VueToast },
    computed : {
        msg (){
            console.log('toast computed getters', this.$store.getters.getMessage)
            return this.$store.getters.getMessage
        }
    },
    watch :{
        'msg' : {
            handler : function(val, old){
                if(val.content !== ''){
                    this.showToastr(val.content, val.type)
                    this.hideMsg()
                }
            }
        }
    },
    methods:{
        showToastr(content, type='error', position='bottom right'){
          this.$refs.toast.setOptions({ maxToasts:3, position: position })
          this.$refs.toast.showToast(content, {
            theme: type,
            timeLife: 5000,
            closeBtn: false
          })
        },
        hideMsg(){
            console.log('hide msg')
            this.$store.dispatch('hideMsg')
        }
    },
    created(){
        console.log("toaster created")
    }

}
</script>

<style>
</style>

