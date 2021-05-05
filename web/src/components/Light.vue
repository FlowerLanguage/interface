<template>
    <div>
        <table class="light_grid">
        <caption>热门轻小说排行榜</caption>
        <tr>
            <td>
                <div v-for="item in sb" class="light_content">
                    <img :src="item.cover" alt="" class="light_img">
                    <div class="light_detail">
                        <b>{{ item.title }}</b>
                        <p>作者:{{ item.author }}/分类:{{ item.classification }}/状态:{{ item.status }}</p>
                        <p>最后更新:{{ item.update }}</p>
                        <p>长度:{{ item.length }}</p>
                    </div>
                </div>
            </td>
        </tr>
    </table>
    <div class="light_pages">
        <div class="light_previous" @click="previousPage">
            上一页
        </div>
        <div class="light_next" @click="nextPage">
            下一页
        </div>
    </div>
    </div>
</template>

<style>
    .light_grid {
        border-collapse: collapse;
        border: 1px solid #a4cded;
        padding: 3px;
        width: 1000px;
        display: table;
    }

    .light_grid caption {
        border: 1px solid #a4cded;
        background: #e9f1f8;
        vertical-align: middle;
        text-align: center;
        color: #054e86;
        font-weight: bold;
        font-size: 14px;
        margin: auto;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .light_content {
        margin-bottom: 15px;
        float: left;
        width: 480px;
        margin-right: 15px;
    }

    .light_content .light_img {
        width: 90px;
        height: 130px;
        float: left;
    }

    .light_detail {
        margin-left: 100px;
        height: 130px;
        text-align: left;
        display: block;
    }

    .light_detail b {
        font-size: 13px;
        font-weight: bold;
    }

    .light_detail p {
        line-height: 50%;
        display: block;
        margin-block-start: 0.5em;
        margin-block-end: 1em;
        margin-inline-start: 0px;
        margin-inline-end: 0px;
    }
    .light_pages{
        padding: 5px 0px;
        margin-bottom: 60px;
        font-weight: bold;
    }
    .light_previous{
        float: left;
        cursor: pointer;
    }
    .light_next{
        float: right;
        cursor: pointer;
    }

</style>

<script type="text/javascript">
    import Msg from './msg'

    export default {
        data() {
            return {
                sb: [],
                previous:'',
                next:''
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('data', function (res) {
                _this.sb = res
            })
            Msg.$on('next',function (res){
                _this.next=res
            })
            Msg.$on('previous',function (res){
                _this.previous=res
            })
        },
        methods:{
            previousPage:function (){
                Msg.$emit('page',this.previous)
                window.scrollTo(0,0)
            },
            nextPage:function (){
                Msg.$emit('page',this.next)
                window.scrollTo(0,0)
            }
        }

    }
</script>


