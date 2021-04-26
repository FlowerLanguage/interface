import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '../store'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VueParticles from 'vue-particles'  //粒子特性
import axios from 'axios'

Vue.use(VueParticles)
Vue.use(ElementUI);

Vue.config.productionTip = false
Vue.prototype.$http=axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
