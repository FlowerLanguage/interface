<template>
    <div>
        <table class="foreign_table">
            <thead>
            <tr class="foreign_head">
                <th>日期</th>
                <th>收盘</th>
                <th>开盘</th>
                <th>高</th>
                <th>底</th>
                <th>涨跌幅</th>
                <th>类型</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in results" class="foreign_body">
                <td>{{ item.date }}</td>
                <td>{{ item.close }}</td>
                <td>{{ item.open }}</td>
                <td>{{ item.high }}</td>
                <td>{{ item.low }}</td>
                <td>{{ item.net_chg_pct }}</td>
                <td>{{ item.symbol }}</td>
            </tr>
            </tbody>
        </table>
        <div class="foreign_pages">
            <div class="foreign_previous" @click="previousPage">
                上一页
            </div>
            <div class="foreign_next" @click="nextPage">
                下一页
            </div>
        </div>
    </div>
</template>

<style type="text/css">
    .foreign_table {
        border: 1px solid #bababa;
        width: 1000px;
    }

    .foreign_head th {
        padding-right: 50px;
        font-size: 15px;
        font-weight: normal;
        border-bottom: 3px solid #bababa;
    }

    .foreign_body td {
        font-size: 15px;
        border-bottom: 1px solid #bababa;
        margin-right: 0px;
    }

    .foreign_pages {
        padding: 5px 0px;
        margin-bottom: 60px;
        font-weight: bold;
    }

    .foreign_previous {
        float: left;
        cursor: pointer;
    }

    .foreign_next {
        float: right;
        cursor: pointer;
    }
</style>

<script type="text/javascript">
    import Msg from './msg'

    export default {
        data() {
            return {
                results: [],
                previous:'',
                next:''
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('data', function (res) {
                _this.results = res
            })
            Msg.$on('next',function (res){
                _this.next=res
            })
            Msg.$on('previous',function (res){
                _this.previous=res
            })
        },
        methods: {
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