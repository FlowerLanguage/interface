<template>
    <div id="login-container">
        <div style="text-align: center;height: 50px">
            登录
        </div>
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="账号" prop="user">
                <el-input id="sb" type="text" v-model="ruleForm.user" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
                <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
            </el-form-item>
            <!--      <el-form-item label="年龄" prop="age">-->
            <!--        <el-input v-model.number="ruleForm.age"></el-input>-->
            <!--      </el-form-item>-->
            <el-form-item>
                <el-button type="primary" @click="Login('ruleForm')">登录</el-button>
                <el-button @click="Register('ruleForm')">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "login",
        data() {
            let validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入账户'));
                } else {
                    if (this.ruleForm.pass !== '') {
                        this.$refs.ruleForm.validateField('pass');
                    }
                    callback();
                }
            };
            let validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    callback();
                }
            };
            return {
                ruleForm: {
                    user: '',
                    pass: '',
                },
                rules: {
                    user: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    pass: [
                        {validator: validatePass2, trigger: 'blur'}
                    ],
                },
                isLogin: false
            };
        },
        methods: {
            getCookie(name) {  // 验证403错误
                let value = '; ' + document.cookie
                let parts = value.split('; ' + name + '=')
                if (parts.length === 2) return parts.pop().split(';').shift()
            },
            Login(formName) {  // 登录函数
                let _user = this.ruleForm.user;
                let _pass = this.ruleForm.pass;
                let _this = this;
                let _token;
                if (_user && _pass) {
                    let url = 'http://60.205.201.200/account/token/get'  // 获取token服务器地址
                    let data = {
                        'username': _user,
                        'password': _pass,
                    }  // 登录账号时需要的参数
                    _this.$http.post(url, data,{headers:{'X-CSRFToken': this.getCookie('csrftoken')}}).then(function (res) {
                        _this.$message.success('登录成功');
                        _token = res.data.token;  // 获取登录后取得的token
                        _this.$store.commit('setToken', _token);  // 将获取的token存入store管路的状态中
                        _this.$store.commit('setId', _user);  // 将获取的userid存入store管路的状态中
                        _this.$router.push({path: '/home'});  // 登录成功后，跳转到主页
                    }).catch(error => {
                        _this.$message.error('请输入正确的账号或密码')
                    })
                } else {
                    _this.$message.error('请输入正确格式');
                }
            },
            Register(formName) {  // 注册函数
                let _user = this.ruleForm.user;
                let _pass = this.ruleForm.pass;
                let _this = this;
                if (_user && _pass) {  // 先判断是否输入了账号或密码
                    let url = 'http://60.205.201.200/account/user/register'  // 注册账号的服务器地址
                    let data = {
                        'username': _user,
                        'password': _pass,
                        'is_active': true
                    }  // 注册账号时需要的参数
                    _this.$http.post(url, data,{headers:{'X-CSRFToken': this.getCookie('csrftoken')}}).then(function (res) {
                        _this.$message.success("注册成功!!!");
                    }).catch(error => {
                        _this.$message.error('注册账号失败')
                    })
                } else {
                    this.$message.error('请输入正确格式');
                }
                this.$refs[formName].resetFields();  // 清除表单上的数据
            }
        }
    }
</script>

<style scoped>
    body {
        margin: 0;
    }

    #login-container {
        width: 400px;
        height: 290px;
        background: #e5e9f2;
        position: absolute;
        left: 50%;
        top: 50%;
        margin-left: -220px;
        margin-top: -170px;
        border-radius: 5px;
        padding-top: 40px;
        padding-right: 40px;
    }
</style>
