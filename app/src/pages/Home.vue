<template>
  <div class="container">
    <time-line>
    </time-line>
  </div>
</template>

<script>
  import TimeLine from '../components/TimeLine'

  export default {
    name: "home",
    components: {
      TimeLine,
      'time-line': TimeLine,
    }
  }
</script>

<style scoped>

</style>
