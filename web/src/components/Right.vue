<template>
    <div class="right">
        <img v-if="first==true" ref="img" src="../../public/img/house_price.jpg" alt="春物">
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
        <div v-if="first==false" class="download" @click="downloadJson">
            <b>下载</b>
        </div>
    </div>
</template>

<style>
    .right {
        position: relative;
    }
    .download{
        float: right;
        cursor: pointer;
        color: red;
        margin-bottom: 20px;
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
        methods: {
            downloadJson:function (){
                let content = new Blob([JSON.stringify(this.result)])
                //生成url对象
                let urlObject = window.URL || window.webkitURL || window
                let url = urlObject.createObjectURL(content)
                //生成<a></a>DOM元素
                let el = document.createElement('a')
                //链接赋值
                el.href = url
                el.download = "接口.txt"
                //必须点击否则不会下载
                el.click()
                //移除链接释放资源
                urlObject.revokeObjectURL(url)
            }
        },
        components: {
            Light,
            Foreign,
            Movie,
            House
        }

    }

</script>

