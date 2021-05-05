<template>
    <div>
        <select name="" id="" @change="getSelectValue($event)">
            <option v-for="item in date" :value="item.value" >{{ item.text }}</option>
        </select>
        <table class="house_table">
            <thead>
                <tr class="house_head">
                    <th>序号</th>
                    <th>城市名称</th>
                    <th>平均单价(元/㎡)</th>
                    <th>环比</th>
                    <th>同比</th>
                </tr>
            </thead>
            <tbody>
                <tr class="house_body" v-for="item in data">
                    <td>{{ item.id }}</td>
                    <td>{{ item.city }}</td>
                    <td>{{ item.avg_unit_price }}</td>
                    <td>{{ item.chain_comparison }}</td>
                    <td>{{ item.year_on_year }}</td>
                </tr>
            </tbody>
        </table>
        <div class="house_pages">
            <div class="house_previous" @click="previousPage">
                上一页
            </div>
            <div class="house_next" @click="nextPage">
                下一页
            </div>
        </div>
    </div>
</template>

<style>
    .house_table{
        width: 1000px;
        text-align: center;
        border: 2px solid #e6e7eb;
    }
    .house_head th{
        font-weight: normal;
        font-size: 15px;
    }
    .house_pages {
        padding: 5px 0px;
        margin-bottom: 60px;
        font-weight: bold;
    }
    .house_body td{
        border-bottom: 2px solid #e6e7eb;
        padding-top: 10px;
    }
    .house_previous {
        float: left;
        cursor: pointer;
    }

    .house_next {
        float: right;
        cursor: pointer;
    }
</style>

<script>
    import Msg from './msg'
    export default {
        data(){
            return{
                data:[],
                previous:'',
                next:'',
                date:[
                    {
                        'value':'202102',
                        'text':'2021年2月份'
                    },
                    {
                        'value':'202104',
                        'text':'2021年4月份'
                    },
                ]
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
        },
        methods:{
            getSelectValue:function (res){
                Msg.$emit('year',res.target.value)
            },
            previousPage: function () {
                Msg.$emit('page', this.previous)
                window.scrollTo(0, 0)
            },
            nextPage: function () {
                Msg.$emit('page', this.next)
                window.scrollTo(0, 0)
            }
        }
    }
</script>