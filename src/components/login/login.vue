<template>
<div class="ui middle aligned three columns center aligned grid">
  <div class="column">
    <h2 class="login-header">
      <div class="content">
          用户登录
      </div>
    </h2>
    <!--
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
    </form>
      <div class="ui error message" v-show="msg">
          {{msg}}
      </div>
    <div class="ui fluid teal button">
        <p> <router-link to="/register"> 注册 </router-link> </p>
    </div>
    -->

    <Form ref="formInline" :model="formInline" :rules="ruleInline" label-position="left" :label-width=100>
        <Form-item prop="username" label="用户名">
            <Input type="text" v-model="formInline.user" placeholder="请输入用户名">
            <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item prop="password" label="密码">
            <Input type="password" v-model="formInline.password" placeholder="请输入密码">
            <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item>
            <Button type="primary" @click="handleSubmit('formInline')">登录</Button>
            <Button type="ghost"><p class="reg"><router-link to="/register">注册</router-link></p></Button>
        </Form-item>
    </Form>
  </div>
  <Toaster></Toaster>
</div>
</template>

<script>
import Toaster from '../toaster'
export default {
    data : function() {
        return {
            username: "",
            password: "",
            error: false,
            msg: "",
            formInline: {
                user: '',
                password: ''
            },
            ruleInline: {
                user: [
                { required: true, message: '请填写用户名', trigger: 'blur' },
                {type: 'string', min: 3, message: '用户名长度不能小于3位', trigger: 'blur'}
                ],
                password: [
                { required: true, message: '请填写密码', trigger: 'blur' },
                { type: 'string', min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
                ]
            }
        }
    },
    components : {
        Toaster
    },
    methods : {
        login : function(){
            if (this.username.length < 1 && this.password.length < 1){
                this.error = true
                this.msg = "用户名或密码不能为空"
                return
            }
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
        },
        handleSubmit(name) {
            this.$refs[name].validate((valid) => {
                console.log("login valid", valid, this.formInline)
                if (valid) {
                    this.$Message.success('提交成功!');
                    this.$store.dispatch('getLogin', {username:this.formInline.user, password:this.formInline.password})
                } else {
                    this.$Message.error('表单验证不符合规则，请重新填写');
                }
            })
        }
    },
    created(){
        console.log("login created")
    }
}
</script>

<style>
a, .reg{
    color: #fff;
}
.login-header{
    margin: 20px;
}
</style>

