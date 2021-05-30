<template>
    <div class="detail">
        <div class="top">
            <div class="left">
                <img :src="detail_data.cover" alt="" class="detail_light_img">
                <div class="detail_light_detail">
                    <b @click="enterDetail(item)">{{ detail_data.title }}</b>
                    <p>作者:{{ detail_data.author }}</p>
                    <p>状态:{{ detail_data.status }}</p>
                    <p>分类:{{ detail_data.classification }}</p>
                    <p>最后更新:{{ detail_data.update }}</p>
                    <p>长度:{{ detail_data.length }}</p>
                    <p>阅读量:{{ this_read_amount }}</p>
                    <p>收藏量:{{ this_collection_amount }}</p>
                    <p>下载量:{{ this_download_amount }}</p>
                </div>
            </div>
            <div class="right">
                <div class="light_user">
                    用户信息
                    <div class="user_read">
                        <p>我的阅读:</p>
                        <select name="" id="" @change="">
                            <option v-for="item in read_amount" :value="item.value">{{ item.text }}</option>
                        </select>
                    </div>
                    <div class="user_collection">
                        <p>我的收藏:</p>
                        <select name="" id="" @change="">
                            <option v-for="item in collection_amount" :value="item.value">{{ item.text }}</option>
                        </select>
                    </div>
                    <div class="user_download">
                        <p>我的下载:</p>
                        <select name="" id="" @change="">
                            <option v-for="item in download_amount" :value="item.value">{{ item.text }}</option>
                        </select>
                    </div>
                </div>
                <div class="light_search">
                    搜索模块
                    <ul>
                        <li>
                            标题:
                            <input type="text" class="title_text" ref="search_title">
                        </li>
                        <li>
                            作者:
                            <input type="text" class="author_text" ref="search_author">
                        </li>
                        <li>
                            文库:
                            <input type="text" class="classification_text" ref="search_classification">
                        </li>
                        <li>
                            <input type="submit" class="submit" @click="searchFunc">
                        </li>
                    </ul>
                </div>
                <div class="light_recommend">
                    推荐模块
                    <div class="recommend_read">
                        <div>阅读推荐:</div>
                        <p>{{ read_top.title }}</p>
                    </div>
                    <div class="recommend_collection">
                        <div>收藏推荐:</div>
                        <p>{{ collection_top.title }}</p>
                    </div>
                    <div class="recommend_download">
                        <div>下载推荐:</div>
                        <p>{{ download_top.title }}</p>
                    </div>

                </div>

            </div>

        </div>
        <div class="bottom">
            <div class="operation">
                <div class="operation_read" @click="readFunc">
                    <a :href="detail_data.read" target="_blank">阅读</a>
                </div>
                <div class="operation_collection" @click="collectFunc">
                    收藏
                </div>
                <div class="operation_download" @click="downloadFunc">
                    <a :href="detail_data.download" target="_blank">下载</a>
                </div>
            </div>
            <div class="comment">
                <span>
                    评论
                </span>
                <div class="old_comment">
                    <ul>
                        全部评论
                        <li v-for="item in comment_data">
                            <p>{{ item.username }}：</p>
                            <div>
                                {{ item.comment }}
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="new_comment">
                    <div>
                        我要评论
                        <div>
                            <input type="text" ref="comment_txt" class="comment_text">
                            <input type="submit" value="评论" class="comment_submit" @click="commentFunc">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style type="text/css">
    .operation_download a {
        color: black;
        text-decoration: none;
    }

    .operation_read a {
        color: black;
        text-decoration: none;
    }

    .comment_submit {
        width: 50px;
        float: right;
        margin-top: 2px;
    }

    .comment_text {
        width: 500px;
        margin-right: 10px;
    }

    .new_comment div {
        width: 100%;
        margin-top: 3px;
        list-style: none;
        border: 1px solid #bababa;
    }

    .new_comment {
        width: 100%;
        float: left;
        margin-top: 10px;
    }

    .old_comment ul li div {
        margin-left: 40px;
    }

    .old_comment ul li p {
        float: left;
    }

    .old_comment ul li {
        border: 1px solid #bababa;
    }


    .old_comment ul {
        width: 100%;
        margin-top: 3px;
        list-style: none;
        border: 1px solid #bababa;
    }

    .old_comment {
        width: 100%;
        float: left;
    }

    .comment span {
        margin-left: 250px;
    }

    .comment {
        margin-top: 10px;
        width: 100%;
    }

    .operation div {
        margin-top: 10px;
        float: left;
        margin-left: 100px;
        cursor: pointer;
    }

    .operation {
        width: 100%;
        height: 40px;
        border: 1px solid #bababa;
    }

    .bottom {
        width: 600px;
        height: 300px;
        margin-top: 20px;
    }

    .recommend_download div {
        float: left;
    }

    .recommend_download p {
        cursor: pointer;
        margin-left: 80px;
    }

    .recommend_download {
        margin-top: 5px;
    }

    .recommend_collection {
        margin-top: 5px;
    }

    .recommend_collection div {
        float: left;
    }

    .recommend_collection p {
        cursor: pointer;
        margin-left: 80px;
    }

    .recommend_read div {
        float: left;
    }

    .recommend_read p {
        margin-left: 80px;
        cursor: pointer;
    }

    .recommend_read {
        margin-top: 5px;
    }

    .submit {
        width: 80px;
        margin-left: 10px;
    }

    .light_search ul li {
        margin-top: 5px;
    }

    .light_search ul {
        list-style: none;
    }

    .user_download p {
        float: left;
    }

    .user_download select {
        float: left;
        margin-left: 10px;
        margin-top: 4px;
        width: 120px;
    }

    .user_download {
        margin-top: 5px;
    }

    .user_collection p {
        float: left;
    }

    .user_collection select {
        float: left;
        margin-left: 10px;
        margin-top: 4px;
        width: 120px;
    }

    .user_collection {
        margin-top: 5px;
    }

    .user_read p {
        float: left;
    }

    .user_read select {
        float: left;
        margin-left: 10px;
        margin-top: 4px;
        width: 120px;
    }

    .user_read {
        margin-top: 5px;
    }

    .light_user {
        width: 100%;
        border: 1px solid #bababa;
        height: 140px;
    }

    .light_search {
        width: 100%;
        border: 1px solid #bababa;
        height: 140px;
        margin-top: 5px;
    }

    .light_recommend {
        width: 100%;
        border: 1px solid #bababa;
        height: 110px;
        margin-top: 5px;
    }

    .light_user div {
        height: 35px;
    }

    .top {
        width: 1000px;
        height: 300px;
    }

    .top .left {
        width: 600px;
        height: 100%;
    }

    .top .right {
        width: 350px;
        float: right;
        height: 100%;

    }

    .detail_light_img {
        float: left;
    }

    .detail_light_detail {
        float: left;
        margin-left: 10px;
    }

    .detail_light_detail p {
        margin-top: 15px;
    }

</style>

<script type="text/javascript">
    import Msg from './msg'

    export default {
        data() {
            return {
                userId: '',  // 用户名
                detail_data: '',  // 页面该小说的具体内容
                this_read_amount: 2,  // 该小说的阅读量
                this_collection_amount: 3,  // 该小说的收藏量
                this_download_amount: 10,  // 该小说的下载量
                read_amount: [
                    {
                        'value': '',
                        'text': '文学少女'
                    },
                    {
                        'value': '',
                        'text': '月色真美'
                    }
                ],  // 用户的阅读
                collection_amount: [
                    {
                        'value': '',
                        'text': 'Just Because'
                    },
                    {
                        'value': '',
                        'text': '实教'
                    }
                ],  // 用户的收藏
                download_amount: [
                    {
                        'value': '',
                        'text': '春物'
                    },
                    {
                        'value': '',
                        'text': 'Air'
                    }
                ],  // 用户的下载
                read_top: {
                    'title':'日常'
                },  // 阅读榜单
                collection_top: {
                    'title':'overload'
                },  // 收藏榜单
                download_top: {
                    'title':'神的记事本'
                },  // 下载榜单
                comment_data: [
                    {
                        'username': 'Kaede枫',
                        'comment': '已经完结'
                    },
                    {
                        'username': 'Akie秋',
                        'comment': '已经完结'
                    }
                ],  // 评论列表
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('detail_data', function (res) {
                _this.detail_data = res  // 取得该小说的具体内容
                _this.userId = _this.$store.getters.getId  // 取得用户名
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let url = 'http://60.205.201.200/operation/'
                _this.$http.get(url, {headers: headers}).then(function (res) {
                    _this.initializeParam()
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            })
        },
        methods: {
            getCookie(name) {  // 验证403错误
                let value = '; ' + document.cookie
                let parts = value.split('; ' + name + '=')
                if (parts.length === 2) return parts.pop().split(';').shift()
            },
            duplicateRemove(param) {
                let arr = []
                for (let i = 0; i < param.length; i++) {
                    if (arr.indexOf(param[i]) == -1) {
                        arr.push(param[i])
                    }
                }
                return arr;
            },
            initializeParam() {
                this.getReadOperation()
                this.getCollectionOperation()
                this.getDownloadOperation()
                this.getCommentOperation()
                this.getRecommend()

            },

            getTop(param,type){  // 用来提取数量最大的数即阅读、收藏、下载
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let index=[]  // 用来存储个数
                let detail_id=[]  // 用来存储对应的小说id
                for(let i of param){
                    let id=i.novel_id
                    if (detail_id.indexOf(id)==-1){
                        detail_id.push(id)
                        index.push(1)
                    }else {
                        index[detail_id.indexOf(id)]=index[detail_id.indexOf(id)]+1
                    }
                }
                let num_max_value=Math.max.apply(null,index)  // 取得存储个数中最大的数值
                let num_max_index=index.indexOf(num_max_value)  // 取得最大个数的索引值
                let top_id=detail_id[num_max_index]  // 取得该数量最大的小说id
                let novel_url = 'http://60.205.201.200/hot_novel/?id='+top_id  // 请求该id获取具体的小说内容
                _this.$http.get(novel_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results'][0]  // 取得筛选的结果返回
                    if(type=='read'){
                        _this.read_top=temp
                    }else if (type=='collection'){
                        _this.collection_top=temp
                    }else{
                        _this.download_top=temp
                    }
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },
            getRecommend(){  // 用来获取推荐榜单，先获取对应的数据表内容，然后传给其他函数处理
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let recommendRead_url = 'http://60.205.201.200/operation/?read=1'  // 获取有阅读的所有url
                let recommendCollection_url = 'http://60.205.201.200/operation/?collection=1'  // 获取有收藏的所有url
                let recommendDownload_url = 'http://60.205.201.200/operation/?download=1'  // 获取有下载的所有url

                _this.$http.get(recommendRead_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']
                    _this.getTop(temp,'read')
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })

                _this.$http.get(recommendCollection_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']
                    _this.getTop(temp,'collection')
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })

                _this.$http.get(recommendDownload_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']
                    _this.getTop(temp,'download')
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },

            getCommentOperation() {
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let comment_url = 'http://60.205.201.200/operation/?novel_id=' + _this.detail_data.id  // 取得数据表中novel_id为该小说的所有数据
                _this.comment_data.splice(0, _this.comment_data.length)
                _this.$http.get(comment_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']
                    let temp_result=[]
                    for(let i of temp){
                        if (i.comment){
                            temp_result.push(i)  // 如果该条记录有评论，才加入列表中
                        }
                    }
                    _this.comment_data=temp_result
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },
            getReadOperation() {
                // 先获取表中所有该用户的记录，去重剔除重复的小说id，请求取得其内容，然后放在对应的变量中
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let read_url = 'http://60.205.201.200/operation/?username=' + _this.userId + '&read=1'  // 取得数据表中用户名为该用户的所有数据
                _this.$http.get(read_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']  // 用来存储获取的数据后面做其他提取
                    let novel_read = []  // 用来存储表中所有小说的id
                    for (let i of temp) {
                        novel_read.push(i.novel_id)
                    }
                    _this.read_amount.splice(0, _this.read_amount.length)
                    novel_read = _this.duplicateRemove(novel_read)  // 调用去重的函数
                    for (let i of novel_read) {
                        let novel_data_url = 'http://60.205.201.200/hot_novel/?id=' + i  // 根据其novel_id获取具体的小说内容
                        _this.$http.get(novel_data_url, {headers: headers}).then(function (res) {
                            _this.read_amount.push({
                                'value': '',
                                'text': res['data']['results'][0].title
                            })  // 直接将该内容添加到用户信息的阅读参数中
                        })
                    }

                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },
            getCollectionOperation() {
                // 先获取表中所有该用户的记录，去重剔除重复的小说id，请求取得其内容，然后放在对应的变量中
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let collection_url = 'http://60.205.201.200/operation/?username=' + _this.userId + '&collection=1'  // 取得数据表中用户名为该用户的所有数据
                _this.$http.get(collection_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']  // 用来存储获取的数据后面做其他提取
                    let novel_read = []  // 用来存储表中所有小说的id
                    for (let i of temp) {
                        novel_read.push(i.novel_id)
                    }
                    _this.collection_amount.splice(0, _this.collection_amount.length)
                    novel_read = _this.duplicateRemove(novel_read)  // 调用去重的函数
                    for (let i of novel_read) {
                        let novel_data_url = 'http://60.205.201.200/hot_novel/?id=' + i  // 根据其novel_id获取具体的小说内容
                        _this.$http.get(novel_data_url, {headers: headers}).then(function (res) {
                            _this.collection_amount.push({
                                'value': '',
                                'text': res['data']['results'][0].title
                            })  // 直接将该内容添加到用户信息的收藏参数中
                        })
                    }

                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },
            getDownloadOperation() {
                // 先获取表中所有该用户的记录，去重剔除重复的小说id，请求取得其内容，然后放在对应的变量中
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                let download_url = 'http://60.205.201.200/operation/?username=' + _this.userId + '&download=1'  // 取得数据表中用户名为该用户的所有数据
                _this.$http.get(download_url, {headers: headers}).then(function (res) {
                    let temp = res['data']['results']  // 用来存储获取的数据后面做其他提取
                    let novel_read = []  // 用来存储表中所有小说的id
                    for (let i of temp) {
                        novel_read.push(i.novel_id)
                    }
                    _this.download_amount.splice(0, _this.download_amount.length)
                    novel_read = _this.duplicateRemove(novel_read)  // 调用去重的函数
                    for (let i of novel_read) {
                        let novel_data_url = 'http://60.205.201.200/hot_novel/?id=' + i  // 根据其novel_id获取具体的小说内容
                        _this.$http.get(novel_data_url, {headers: headers}).then(function (res) {
                            _this.download_amount.push({
                                'value': '',
                                'text': res['data']['results'][0].title
                            })  // 直接将该内容添加到用户信息的下载参数中
                        })
                    }

                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },

            commentFunc: function () {
                let _this = this
                let value = this.$refs.comment_txt.value  // 取得评论input中的值
                if (value) {
                    let headers = {
                        'Authorization': 'Token ' + _this.$store.getters.getToken,
                        'Content-Type': 'application/json',
                        'X-CSRFToken': _this.getCookie('csrftoken')
                    }
                    let url = 'http://60.205.201.200/operation/'
                    let comment_data = {
                        'username': _this.userId,
                        'novel_id': _this.detail_data['id'],
                        'comment': value
                    }
                    _this.$http.post(url, comment_data, {headers: headers}).then(function (res) {
                        _this.$message.success('评论成功')
                        _this.$refs.comment_txt.value = ''  // 评论成功则情况input中的内容
                        _this.getCommentOperation()  // 调用获取评论的函数
                    }).catch(function (error) {
                        _this.$message.error('请重新登录')
                        _this.$router.push('/')
                    })
                } else {
                    this.$message.error('请输入正确的内容')
                }
            },
            readFunc: function () {
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json',
                    'X-CSRFToken': _this.getCookie('csrftoken')
                }
                let url = 'http://60.205.201.200/operation/'
                let read_data = {
                    'username': _this.userId,
                    'novel_id': _this.detail_data['id'],
                    'read': 1
                }
                _this.$http.post(url, read_data, {headers: headers}).then(function (res) {
                    _this.$message.success('成功跳转到阅读界面')
                    _this.getReadOperation()
                    _this.getRecommend()
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },
            collectFunc: function () {
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json',
                    'X-CSRFToken': _this.getCookie('csrftoken')
                }
                let url = 'http://60.205.201.200/operation/'
                let collect_data = {
                    'username': _this.userId,
                    'novel_id': _this.detail_data['id'],
                    'collection': 1
                }
                _this.$http.post(url, collect_data, {headers: headers}).then(function (res) {
                    _this.$message.success('收藏成功')
                    _this.getCollectionOperation()
                    _this.getRecommend()
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },
            downloadFunc: function () {
                let _this = this
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json',
                    'X-CSRFToken': _this.getCookie('csrftoken')
                }
                let url = 'http://60.205.201.200/operation/'
                let collect_data = {
                    'username': _this.userId,
                    'novel_id': _this.detail_data['id'],
                    'download': 1
                }
                _this.$http.post(url, collect_data, {headers: headers}).then(function (res) {
                    _this.$message.success('成功跳转到下载界面')
                    _this.getDownloadOperation()
                    _this.getRecommend()
                }).catch(function (error) {
                    _this.$message.error('请重新登录')
                    _this.$router.push('/')
                })
            },

            searchFunc: function () {
                let _this = this
                let title = _this.$refs.search_title.value  // 获取搜索标题
                let author = _this.$refs.search_author.value  // 获取搜索作者
                let classification = _this.$refs.search_classification.value // 获取搜索文库
                let headers = {
                    'Authorization': 'Token ' + _this.$store.getters.getToken,
                    'Content-Type': 'application/json'
                }
                _this.$refs.search_title.value = ''
                _this.$refs.search_author.value = ''
                _this.$refs.search_classification.value = ''  // 清空
                let isSearch = false  // 用来记录是否输入了搜索内容

                let url_continued = 'http://60.205.201.200/hot_novel/?'  // 初始网页
                if (title) {
                    url_continued = url_continued + '&title=' + title
                    isSearch = true
                }
                if (author) {
                    url_continued = url_continued + '&author=' + author
                    isSearch = true
                }
                if (classification) {
                    url_continued = url_continued + '&classification=' + classification
                    isSearch = true
                }  // 拼接网页

                if (isSearch) {  // 输入了内容就检索
                    _this.$http.get(url_continued, {headers: headers}).then(function (res) {
                        let data = res['data']['results']
                        if (data.length == 0) {
                            _this.$message.info('没有检索到对应内容')
                        } else {
                            _this.$message.success('检索成功')
                            Msg.$emit('search_module',res)
                        }

                    }).catch(function (error) {
                        _this.$message.error('请重新登录')
                        _this.$router.push('/')
                    })
                } else {
                    _this.$message.warning('请输入后再操作')
                }
            },
        }
    }

</script>