import Vue from 'vue'
import VueRouter from 'vue-router'
import BootStrapVue from 'bootstrap-vue'
import App from './App.vue'
import SignUp from './pages/SignUp'
import Login from './pages/Login'
import Home from './pages/Home'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(BootStrapVue);
Vue.use(VueRouter);

importVueBootstrapComponents();

const routes = [
  {
    path: '/',
    name: '/',
    redirect: '/home',
    component: App
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
];

const router = new VueRouter({
  routes
});

const app = new Vue({
  el: '#app',
  router: router,
  render: h => h(App),
});

function importVueBootstrapComponents() {

}

