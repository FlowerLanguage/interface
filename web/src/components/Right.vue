<template>
    <div class="right">
        <img v-if="first==true" ref="img" src="../../public/img/1.jpg" alt="春物">
        <div v-if="key=='hot_novel'">
            <Light></Light>
        </div>
        <div v-if="key=='foreign_currency'">
            <Foreign></Foreign>
        </div>
        <div v-if="key=='movie'">
            <Movie></Movie>
        </div>
        <div v-if="key=='house_price'">
            <House></House>
        </div>
    </div>
</template>

<style>
    .right {
        position: relative;
    }

</style>

<script type="text/javascript">
    import Msg from './msg.js'
    import Light from './Light'
    import Foreign from './Foreign'
    import Movie from './Movie'
    import House from './House'

    export default {
        data() {
            return {
                key: '',
                result: [],
                first:true
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('type', function (res) {
                _this.key = res
                 //_this.$refs.img['src']=require('../../public/img/'+res+'.jpg')  // 利用left组件传递的值构造图片地址
                _this.first=false  // 一旦点击左边元素就设置为false，不显示图片
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                if (res=='movie'){  // 包含电影内容
                    let url = 'http://60.205.201.200/' + res + '/' + 'whole' + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    })
                }else if(res=='house_price'){  // 包含房价内容
                    let url = 'http://60.205.201.200/' + res + '/' + '202102' + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    })
                }else { // 包含轻小说、外汇等内容
                    let url = 'http://60.205.201.200/' + res + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    })
                }
            })
            Msg.$on('page', function (url) {
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                _this.$http.get(url, {headers: headers}).then(function (res) {
                    _this.result = res['data']['results']
                    Msg.$emit('data', _this.result)
                    Msg.$emit('next', res['data']['next'])
                    Msg.$emit('previous', res['data']['previous'])
                })
            })
            Msg.$on('year',function (year){
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let url = 'http://60.205.201.200/' + _this.key + '/' + year + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    })
            })
        },
        methods: {},
        components: {
            Light,
            Foreign,
            Movie,
            House
        }

    }

</script>

