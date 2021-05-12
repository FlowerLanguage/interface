<template>
    <div class="movie">
        <div>
            <ul class="movie_year">
                <li v-for="item,index in year" @click="choiceYear(index)" :style="{'border-bottom':(index==select)?'2px solid red':'none'}">{{ item }}</li>
            </ul>
        </div>
        <div >
            <table class="movie_table">
                <thead>
                    <tr>
                        <th>排名</th>
                        <th>票房(万)</th>
                        <th>平均票价</th>
                        <th>场均人数</th>
                        <th>详情</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="movie_content" v-for="item in data">
                        <td>{{ item.name }}</td>
                        <td>{{ item.box }}</td>
                        <td>{{ item.avg_fare }}</td>
                        <td>{{ item.avg_players }}</td>
                        <td>{{ item.url }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="movie_pages">
        <div class="movie_previous" @click="previousPage">
            上一页
        </div>
        <div class="movie_next" @click="nextPage">
            下一页
        </div>
    </div>
    </div>
</template>

<style type="text/css">
    .movie{
        width: 1000px;
    }
    .movie_year li{
        list-style: none;
        float: left;
        margin-right: 45px;
        padding-bottom: 5px;

        cursor: pointer;
        width: auto;
    }
    .movie_table{
        padding-top: 5px;
        width: 1000px;
    }
    .movie_content{
        height: 80px;
        background-color: #DAEADA;
    }
    .movie_content td{
        padding-top: 10px;
        text-align: center;
    }
    .movie_pages{
        padding: 5px 0px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .movie_previous{
        float: left;
        cursor: pointer;
    }
    .movie_next{
        float: right;
        cursor: pointer;
    }

</style>

<script type="text/javascript">
    import Msg from './msg'
    export default {
        data(){
            return{
                year:['全部','2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011'],
                select:0,
                data:[],
                previous:'',
                next:''
            }
        },
        methods:{
            choiceYear:function (res){
                this.select=res
                if (this.year[this.select]=='全部'){
                    Msg.$emit('year','whole')  // 传递电影的年份
                }else {
                    Msg.$emit('year',this.year[this.select])  // 传递电影的年份
                }

            },
            previousPage:function (){
                Msg.$emit('page',this.previous)
                window.scrollTo(0,0)
            },
            nextPage:function (){
                Msg.$emit('page',this.next)
                window.scrollTo(0,0)
            }
        },
        mounted:function (){
            let _this=this
            Msg.$on('data',function (res){
                _this.data=res
            })
             Msg.$on('next',function (res){
                _this.next=res
            })
            Msg.$on('previous',function (res){
                _this.previous=res
            })
        }
    }
</script>