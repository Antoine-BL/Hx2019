<template>

  <div class="col">
    <div v-for="plan in plans" class="row">
      <plan class="col" v-bind:plan="plan"></plan>
    </div>
    <b-form inline class="row mt-5 justify-content-center">
      <b-button id="addBtn"
                class="add-button bg-light text-muted rounded-circle"
                variant="success"
                @click="addPlan()">
        <font-awesome-icon icon="plus"/>
      </b-button>
    </b-form>
  </div>
</template>

<script>
  import Plan from './Plan'

  export default {
    name: "time-line",
    data() {
      return {
        plans: [{}],
      }
    },
    methods: {
      addPlan() {
        this.compteur++;
        this.plans.push({});
      },
    },
    components: {
      'plan': Plan
    }
  }
</script>

<style scoped>
.add-button{
  border: 1px dotted gray;
}
.add-bar {
  position: absolute;
  transform: translateY(50%);
  height: 95%;
}
</style>
