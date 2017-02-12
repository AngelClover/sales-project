<template>
<div class="ui middle aligned three columns center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <div class="content">
          用户登录
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" placeholder="用户名" v-model="username">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" placeholder="密码" v-model="password">
          </div>
        </div>
        <div class="ui fluid large teal submit button" @click="login">登录</div>
      </div>

      <div class="ui error message" v-show=error>
          {{msg}}
      </div>
      <div >
          {{$store.getters.getToken}}
      </div>

    </form>

    <div class="ui fluid teal button">
        <p> <router-link to="/register"> 注册 </router-link> </p>
    </div>
  </div>
</div>
</template>

<script>
export default {
    data : function() {
        return {
            username: "",
            password: "",
            error: false,
            msg: ""
        }
    },
    methods : {
        login : function(){
            if (this.username.length < 3){
                this.error = true
                this.msg = "用户名不能小于三位"
                return
            }
            if (this.password.length < 6){
                this.error = true
                this.msg = "密码不得小于六位"
                return 
            }
            this.error = false
            this.msg = ""
            console.log(this.username, this.password, this.error, this.msg)
            this.$store.dispatch('getLogin', {username:this.username, password:this.password})
        }
    },
    created(){
        console.log("login created")
    }
}
</script>

<style>
</style>

