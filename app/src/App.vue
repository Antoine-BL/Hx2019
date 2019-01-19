<template>
  <div id="app">
    <app-header></app-header>
  </div>
</template>

<script>
import Header from './components/Header'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'app-header': Header,
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
