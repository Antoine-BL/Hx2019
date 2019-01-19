<template>
<b-navbar  toggleable toggle="md" type="dark" variant="dark">
  <b-navbar-brand to="/">{{brandMsg}}</b-navbar-brand>
  <b-collapse is-nav id="nav_collapse">
    <b-navbar-nav class="text-light">
    </b-navbar-nav>
  </b-collapse>
  <b-button to="/login" variant="success">Connexion</b-button>
  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
</b-navbar>
</template>

<script>
export default {
  name: 'app-header',
  data () {
    return {
      brandMsg: 'Allo-Vélo!'
    }
  },
}
</script>

<style scoped>

</style>
