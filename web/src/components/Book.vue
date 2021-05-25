<template>
    <div>
        {{ sb }}
    </div>
</template>

<style type="text/css">

</style>

<script type="text/javascript">
    import Msg from './msg'
    export default {
        data(){
            return{
                sb:0
            }
        },
        mounted:function (){
            let _this=this
            Msg.$on('data',function (res){
                _this.sb=res
            })
        },
    }

</script>