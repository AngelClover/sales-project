<template>
<div class="ui middle aligned three columns center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <div class="content">
          用户信息修改
      </div>
    </h2>
    <!--
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
    -->

    <Form ref="formInline" :model="formInline" :rules="ruleInline" label-position="left" :label-width=100>
        <Form-item prop="username" label="用户名">
            <Label> {{userInfo.username}}</Label>
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
            <Input type="text" v-model="formInline.email" placeholder="请输入电子邮箱">
            <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item prop="nickname" label="昵称">
            <Input type="text" v-model="formInline.nickname" placeholder="请输入昵称">
            <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </Form-item>
        <Form-item>
            <Button type="primary" @click="handleSubmit('formInline')">修改</Button>
            <Button type="ghost"><p class="reg"><router-link to="/">返回</router-link></p></Button>
        </Form-item>
    </Form>
  </div>
  <Toaster></Toaster>
</div>
</template>

<script>
import Toaster from '../toaster'
export default {
    data (){
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
            //TODO : 怎样跳过validate的require验证,不输入密码直接修改邮箱
            ruleInline: {
                password: [
                { type: 'string', min: 6, message: '密码长度不能小于6位', trigger: 'blur' },
                { validator: validatePass, trigger: 'blur'},
                ],
                confirmPassword: [
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
        },
        handleSubmit (name) {
            this.$refs[name].validate((valid) => {
                if (valid) {
                    this.$Message.success('提交成功!');
                    console.log("username :", this.userInfo.username);
                    this.$store.dispatch('updateUserInfo', {
                        id: this.userInfo.id,
                        username: this.userInfo.username,
                        email: this.formInline.email,
                        nickname: this.formInline.nickname,
                        password: this.formInline.password,
                        password2: this.formInline.confirmPassword
                    })
                } else {
                    this.$Message.error('表单验证失败!');
                }
            })
        },
    }
}
</script>

<style>
</style>

