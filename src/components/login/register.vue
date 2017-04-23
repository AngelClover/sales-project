<template>
<div class="ui middle aligned three columns center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <div class="content">
          用户注册
      </div>
    </h2>
    <!--
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
    -->
    
    <Form ref="formInline" :model="formInline" :rules="ruleInline" label-position="left" :label-width="100">
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
        <Form-item prop="confirmPassword" label="确认密码">
            <Input type="password" v-model="formInline.confirmPassword" placeholder="请输入确认密码">
            <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item prop="email" label="电子邮箱">
            <Input type="email" v-model="formInline.email" placeholder="请输入电子邮箱">
            <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item prop="nickname" label="昵称">
            <Input type="text" v-model="formInline.nickname" placeholder="请输入昵称">
            <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item>
            <Button type="primary" @click="handleSubmit('formInline')">注册</Button>
        </Form-item>
    </Form>
  </div>
  <Toaster></Toaster>
</div>
</template>

<script>
import Toaster from '../toaster'
export default {
    data () {
        const validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                if (this.formInline.confirmPassword !== '') {
                    // 对第二个密码框单独验证
                    this.$refs.formInline.validateField('confirmPassword');
                }
                callback();
            }
        };
        const validatePassCheck = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再次输入密码'));
            } else if (value !== this.formInline.password) {
                callback(new Error('密码与确认密码不一致!'));
            } else {
                callback();
            }
        };
        return {
            username : "",
            password : "",
            password2 : "",
            nickname : "",
            email : "",
            error : false,
            msg : "",
            formInline: {
                user: '',
                password: '',
                confirmPassword: '',
                email: '',
                nickname: '',
            },
            ruleInline: {
                user: [
                { required: true, message: '请填写用户名', trigger: 'blur' },
                {type: 'string', min: 3, message: '用户名长度不能小于3位', trigger: 'blur'}
                ],
                password: [
                { required: true, message: '请填写密码', trigger: 'blur' },
                { type: 'string', min: 6, message: '密码长度不能小于6位', trigger: 'blur' },
                { validator: validatePass, trigger: 'blur'},
                ],
                confirmPassword: [
                { required: true, message: '请填写确认密码', trigger: 'blur' },
                { type: 'string', min: 6, message: '确认密码长度不能小于6位', trigger: 'blur' },
                { validator: validatePassCheck, trigger: 'blur' },
                ],
                email: [
                { type: 'email', message: '电子邮箱合适有误，例abc@123.com', trigger: 'blur' }
                ],
                nickname: [
                { type: 'string', message: '', trigger: 'blur' }
                ],
            }
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

