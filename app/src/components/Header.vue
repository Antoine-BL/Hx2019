<template>
<b-navbar toggleable toggle="md" type="dark" variant="dark">
  <b-navbar-brand>{{brandMsg}}</b-navbar-brand>
  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
  <b-collapse is-nav id="nav_collapse">
    <b-navbar-nav class="text-light">
      <b-navbar-item href="#">Link</b-navbar-item>
    </b-navbar-nav>
  </b-collapse>
</b-navbar>
</template>

<script>
import bNavbar from 'bootstrap-vue/es/components/navbar/navbar';
import bNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand';
import bNavbarToggle from 'bootstrap-vue/es/components/navbar/navbar-toggle';

export default {
  data () {
    return {
      brandMsg: 'Allo-Vélo!'
    }
  },
  components: {
    'b-navbar': bNavbar,
    'b-navbar-brand': bNavbarBrand,
    'b-navbar-toggle': bNavbarToggle,
  }
}
</script>

<style lang="scss">

</style>
