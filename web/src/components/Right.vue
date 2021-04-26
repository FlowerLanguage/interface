<template>
    <div class="right">
        <img ref="img" src="../../public/img/1.jpg" alt="春物">
        <div v-if="key=='hot_novel'">
            {{ key }}
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
<script type="text/javascript">
    import Msg from './msg.js'

    export default {
        data() {
            return {
                key: '',
            }
        },
        mounted: function () {
            let _this = this
            Msg.$on('type', function (res) {
                _this.key = res
                _this.$refs.img['src']=require('../../public/img/'+res+'.jpg')
            })
        },
        methods:{

        }

    }

</script>
<style>
    .right{
        position: relative;
    }
    .right img{
        width: 1000px;
        height: 300px;
    }
</style>