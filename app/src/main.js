import Vue from 'vue'
import VueRouter from 'vue-router'
import BootStrapVue from 'bootstrap-vue'
import App from './App.vue'
import SignUp from './pages/SignUp'
import Login from './pages/Login'
import Home from './pages/Home'
import * as VueGoogleMaps from 'vue2-google-maps'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus } from '@fortawesome/free-solid-svg-icons/faPlus'
import { faCalendar } from '@fortawesome/free-solid-svg-icons/faCalendar'
import { faAddressCard } from '@fortawesome/free-solid-svg-icons/faAddressCard'
import { faEdit } from '@fortawesome/free-solid-svg-icons/faEdit'
import { faMap } from '@fortawesome/free-solid-svg-icons/faMap'
import { faWindowClose } from '@fortawesome/free-solid-svg-icons/faWindowClose'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faPlus, faCalendar, faAddressCard, faEdit, faMap, faWindowClose);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(BootStrapVue);
Vue.use(VueRouter);
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBBGhoFwL83uHNQwFta5pAI2gz9EFIZRtY' //Lol please no steal
  }
});
Vue.filter('toFrCaDate', (date) =>{
  return new Intl.DateTimeFormat('fr-CA').format(date);
});

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
