<template>
  <div id="app">
    <app-header/>
    <router-view/>
  </div>
</template>

<script>

import AppHeader from "./components/AppHeader";

export default {
  name: 'app',
  data () {
    return {
      user: null,
      groups: null,
    }
  },
  components: {
    'app-header': AppHeader
  },
}
</script>

<style lang="scss">
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
