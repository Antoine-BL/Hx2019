import Vue from 'vue'
import BootStrapVue from 'bootstrap-vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootStrapVue);

new Vue({
  el: '#app',
  render: h => h(App)
});
