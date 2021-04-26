<template>
    <div class="home">
        <div class="left">
            <Left></Left>
        </div>
        <div class="right">
            <Right></Right>
        </div>
    </div>
</template>

<script type="text/javascript">
    // @ is an alias to /src
    import Left from '../components/Left.vue'
    import Right from '../components/Right.vue'

    export default {
        data(){
            return{
            }
        },
        methods:{

        },
        components: {
            Left,
            Right
        }
    }
</script>

<style>
    *{
        padding: 0;
        margin: 0;
    }
    .home{
        width: 1200px;
        margin: 20px auto;
    }
    .left{
        width: 80px;
        margin-right: 10px;
        float: left;
    }
    .right{
        width: 1000px;
        margin-left: 10px;
        float: left;
    }

</style>
