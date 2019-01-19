import Vue from 'vue'
import VueRouter from 'vue-router'
import BootStrapVue from 'bootstrap-vue'
import App from './App.vue'
import SignUp from './pages/SignUp'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootStrapVue);
Vue.use(VueRouter);

const routes = [
  { path: '/test', component: {template: '<div>test</div>'}},
  { path: '/app', component: App},
  { path: '/signup', component: SignUp},
];

const router = new VueRouter({
  routes
});

const app = new Vue({
  el: '#app',
  router: router,
  render: h => h(App),
});

