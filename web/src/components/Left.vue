<template>
    <div class="left">
        <div class="title">
            <b>接口列表</b>
        </div>
        <ul class="menu">
            <li @click="getNovel">轻小说</li>
            <li @click="getForeignCurrency">外汇</li>
            <li @click="getMovie">电影</li>
            <li @click="getHousePrice">房价</li>
        </ul>
    </div>
</template>

<script type="text/javascript">
    import Msg from './msg.js'
    export default {
        data(){
            return{

            }
        },
        methods:{
            isExistsToken:function (){  // 用来判断当前token是否还存在
                let _this=this
                let token=this.$store.getters.getToken // 先查看token是否存在
                if (!token){  // 不存在，弹出错误信息，返回空
                    _this.$message.error('请重新登录')
                    return ''
                }else {  // 存在，返回token
                    return token
                }
            },
            getNovel:function (){
                let _this=this
                let token=this.isExistsToken()  // 调用判断token的函数
                if (token){
                    Msg.$emit('type','hot_novel')
                }else {
                    _this.$router.push({path:'/'})  // 跳转到登录页面进行登录
                }
            },
            getForeignCurrency:function (){
                let _this=this
                let token=this.isExistsToken()  // 调用判断token的函数
                if (token){
                    Msg.$emit('type','foreign_currency')
                }else {
                    _this.$router.push({path:'/'})  // 跳转到登录页面进行登录
                }
            },
            getMovie:function (){
                let _this=this
                let token=this.isExistsToken()  // 调用判断token的函数
                if (token){
                    Msg.$emit('type','movie')
                }else {
                    _this.$router.push({path:'/'})  // 跳转到登录页面进行登录
                }
            },
            getHousePrice:function (){
                let _this=this
                let token=this.isExistsToken()  // 调用判断token的函数
                if (token){
                    Msg.$emit('type','house_price')
                }else {
                    _this.$router.push({path:'/'})  // 跳转到登录页面进行登录
                }
            },
        }
    }
</script>

<style>
    .left{
        position: relative;
    }
    .title{
        cursor: pointer;
        color: red;
    }
    .menu li{
        list-style: none;
        color: green;
        height: 50px;
        margin-top: 20px;
        margin-bottom: 20px;
        line-height: 50px;
        cursor: pointer;
    }
</style>