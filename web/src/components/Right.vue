<template>
    <div class="right">
        <div v-if="key=='hot_novel'">
            <Light></Light>
        </div>
        <div v-if="key=='foreign_currency'">
            {{ key }}
        </div>
        <div v-if="key=='movie'">
            {{ key }}
        </div>
        <div v-if="key=='house_price'">
            {{ key }}
        </div>
    </div>
</template>

<style>
    .right{
        position: relative;
    }
    .right img{
        width: 1000px;
        height: 300px;
    }
</style>

<script type="text/javascript">
    import Msg from './msg.js'
    import Light from './Light'

    export default {
        data() {
            return {
                key: '',
                result:[]
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('type', function (res) {
                _this.key = res
                //<img ref="img" src="../../public/img/1.jpg" alt="春物">
                //_this.$refs.img['src']=require('../../public/img/'+res+'.jpg')  // 利用left组件传递的值构造图片地址
                let headers={
                    'Authorization':'Token '+_this.$store.getters.getToken,
                    'Content-Type':'application/json'
                }
                let url='http://60.205.201.200/'+res+'/'  // 利用left组件传递的值构造目标服务器的地址
                _this.$http.get(url,{headers:headers}).then(function (res){
                    _this.result=res['data']['results']
                    Msg.$emit('data',_this.result)
                    Msg.$emit('next',res['data']['next'])
                    Msg.$emit('previous',res['data']['previous'])
                })
            })
            Msg.$on('page',function (url){
                let headers={
                    'Authorization':'Token '+_this.$store.getters.getToken,
                    'Content-Type':'application/json'
                }
                _this.$http.get(url,{headers:headers}).then(function (res){
                    _this.result=res['data']['results']
                    Msg.$emit('data',_this.result)
                    Msg.$emit('next',res['data']['next'])
                    Msg.$emit('previous',res['data']['previous'])
                })
            })
        },
        methods:{

        },
        components:{
            Light
        }

    }

</script>.

