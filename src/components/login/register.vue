<template>
<div class="ui middle aligned three columns center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <div class="content">
          用户注册
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" placeholder="用户名" v-model="username" @input="check">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" placeholder="email" v-model="email" @input="check">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" placeholder="密码" v-model="password" @input="check">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" placeholder="确认密码" v-model="password2" @input="check">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="flag icon"></i>
            <input type="text" placeholder="昵称" v-model="nickname" @input="check">
          </div>
        </div>
        <div class="ui fluid large teal submit button" @click="register">注册</div>
      </div>

    </form>
      <div class="ui error message" v-show="error">
          {{msg}}
      </div>
  </div>
  <Toaster></Toaster>
</div>
</template>

<script>
import Toaster from '../toaster'
export default {
    data : () => {
        return {
            username : "",
            password : "",
            password2 : "",
            nickname : "",
            email : "",
            error : false,
            msg : ""
        }
    },
    components : {
        Toaster
    },
    methods : {
        check : function(){
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
            if (this.password2.length < 6){
                this.error = true
                this.msg = "确认密码不得小于六位"
                return 
            }
            if (this.password != this.password2){
                this.error = true
                this.msg = "密码与确认密码不一致，请重新输入"
                return 
            }
            var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
            if (req.test(this.email) != true){
                this.error = true
                this.msg = "电子邮箱格式有误, 例如:aaa@bbb.com"
                return
            }
            this.error = false
            this.msg = ""
        },
        register : function(){
            this.$store.dispatch('register', {
                username: this.username,
                email: this.email,
                nickname: this.nickname,
                password: this.password,
                password2: this.password2
            })
        }
    }
}
</script>

<style>
</style>

