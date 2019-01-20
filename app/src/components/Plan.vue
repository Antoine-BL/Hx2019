<template>
  <div class="col bg-info plan">
    <div class="row">
      <div class="col-6">
        <b-form @submit="confirmEdit" inline>
          <b-input-group>
            <b-form-input :disabled="!editingTitle" type="text" v-model="planData.titre"/>
            <b-button v-on:click="toggleEdit" variant="light">
              <font-awesome-icon icon="edit"/>
            </b-button>
          </b-input-group>
        </b-form>
      </div>
      <div class="col-6 ml-auto d-flex justify-content-end align-items-center">
        <div class="mr-2">
          {{planData.dateCreation | toFrCaDate}}
        </div>
        <b-button class="circle-btn  rounded-circle" variant="light">
          <font-awesome-icon icon="calendar"/>
        </b-button>
      </div>
    </div>
    <div class="row bg-info">
      <div class="col-8" v-if="plan.people && plan.people.length !== 0">
        <person v-for="person in plan.people"
                v-bind:data="person"
                v-bind:key="person.id">
        </person>
      </div>
      <div class="col-8" v-else>
        Personne ne fait partie de ce plan
      </div>
      <div class="col-4 d-flex justify-content-end">
        <b-button class="circle-btn rounded-circle" variant="light">
          <font-awesome-icon icon="address-card"/>
        </b-button>
      </div>
    </div>
    <div class="row">
      <GmapMap ref="mapRef"
        :center="{lat:10, lng:10}"
        :zoom="7"
        map-type-id="terrain"
        class="map">
      </GmapMap>
    </div>
  </div>
</template>

<script>
  export default {
    name: "plan",
    props: ["plan"],
    data() {
      return {
        planData: this.plan,
        editingTitle: false,
      }
    },
    mounted() {
      this.planData.dateCreation = new Date();
      this.planData.titre = 'Ceci est un titre';

      this.$refs.mapRef.$mapPromise.then((map) => {
        map.panTo({lat: 1.38, lng: 103.80})
      })
    },
    methods: {
      confirmEdit(event) {
        event.preventDefault();
        this.toggleEdit();
      },
      toggleEdit() {
        this.editingTitle = !this.editingTitle;
        if (this.editingTitle) {
          this.plan.titre = '';
        }
      }
    }
  }
</script>

<style scoped>
  .plan .row {
    padding: 0.5rem 0;
    display: flex;
    align-items: center;
  }

  .circle-btn {
    width: 45px;
    height: 45px;
  }

  .map {
    margin: 0 1%;
    width: 100%;
    height: 50vh;
  }
</style>
