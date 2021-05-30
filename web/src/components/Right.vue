<template>
    <div class="right">
        <!--<img v-if="first==false" ref="img" src="../../public/img/house_price.jpg" alt="春物">-->
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
        <div v-if="detail==true">
            <Detail></Detail>
        </div>
        <div v-if="download==true" class="download" @click="downloadJson">
            <b>下载</b>
        </div>
        <div v-if="refresh_switch==true" class="refresh" @click="refresh">
            <b>刷新</b>
        </div>

    </div>
</template>

<style>
    .right {
        position: relative;
    }

    .download {
        float: right;
        cursor: pointer;
        color: red;
        margin-bottom: 20px;
    }

    .download {
        float: left;
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
    import Book from './Book'
    import Detail from './Detail'

    export default {
        data() {
            return {
                key: '',  // 用来获取外汇类型
                result: [],  // 用来存储实际获取的数据
                download: false,  // 用来显示下载按钮
                detail: false,  // 用来控制轻小说系统应用具体界面
                detail_data: '',  // 进入轻小说系统应用的该本轻小说的具体内容
                refresh_switch: false,  // 用来控制显示刷新按钮，点击后才会将数据传给Detail组件

                previous_page: '',  // 用来接收轻小说模块的搜索内容
                next_page: ''  // 用来接收轻小说模块的搜索内容
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('type', function (res) {
                _this.key = res
                _this.detail = false
                _this.download = true
                //_this.$refs.img['src']=require('../../public/img/'+res+'.jpg')  // 利用left组件传递的值构造图片地址
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                if (res == 'movie') {  // 包含电影内容
                    let url = 'http://60.205.201.200/' + res + '/' + 'whole' + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    }).catch(function (error) {
                        _this.$message.error('请重新登录')
                        _this.$router.push('/')
                    })
                } else if (res == 'house_price') {  // 包含房价内容
                    let url = 'http://60.205.201.200/' + res + '/' + '202102' + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    }).catch(function (error) {
                        _this.$message.error('请重新登录')
                        _this.$router.push('/')
                    })
                } else { // 包含轻小说、外汇等内容
                    let url = 'http://60.205.201.200/' + res + '/'  // 利用left组件传递的值构造目标服务器的地址
                    _this.$http.get(url, {headers: headers}).then(function (res) {
                        _this.result = res['data']['results']
                        Msg.$emit('data', _this.result)
                        Msg.$emit('next', res['data']['next'])
                        Msg.$emit('previous', res['data']['previous'])
                    }).catch(function (error) {
                        _this.$message.error('请重新登录')
                        _this.$router.push('/')
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
                }).catch(function (error) {
                    _this.$message.error('不存在该路径')
                    _this.$router.push('/')
                })
            })
            Msg.$on('year', function (year) {
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
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            })
            Msg.$on('detail', function (res) {
                _this.detail = true
                _this.key = ''
                _this.detail_data = res
                _this.download = false
                _this.refresh_switch = true
            })
            Msg.$on('search_module', function (res) {
                _this.detail = false
                _this.key = 'hot_novel'
                _this.refresh_switch = true
                _this.result = res['data']['results']
                _this.previous_page = res['data']['previous']
                _this.next_page = res['data']['next']

            })
        },
        methods: {
            downloadJson: function () {
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
            },
            refresh: function () {
                if (this.key == 'hot_novel') {
                    Msg.$emit('data', this.result)
                    Msg.$emit('next', this.next_page)
                    Msg.$emit('previous', this.previous_page)

                } else {
                    Msg.$emit('detail_data', this.detail_data)
                }
                this.refresh_switch = false
            }
        },
        components: {
            Light,
            Foreign,
            Movie,
            House,
            Book,
            Detail
        }

    }

</script>

