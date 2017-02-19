<template>
<div class="ui middle aligned three columns center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <div class="content">
          用户信息修改
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <div align=center>
            <label type="text" >
            <i class="user icon"></i>
                {{userInfo.username}}</label>
            </div>
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
        <div class="ui fluid large teal submit button" @click="update">修改 </div>
        <div class="ui button"><p>
            <router-link to='/'> 返回 </router-link>
            </p></div>
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
    computed : {
        userInfo(){
            this.email = this.$store.getters.getMe.email || ""
            this.nickname = this.$store.getters.getMe.nickName || ""
            return this.$store.getters.getMe
        }
    },
    components : {
        Toaster
    },
    methods : {
        check : function(){
            if (this.password || this.password2){
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
            }
            if (this.email){
                var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
                    if (reg.test(this.email) != true){
                        this.error = true
                            this.msg = "电子邮箱格式有误, 例如:aaa@bbb.com"
                            return
                    }
            }
            this.error = false
            this.msg = ""
        },
        update : function(){
            this.$store.dispatch('updateUserInfo', {
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

