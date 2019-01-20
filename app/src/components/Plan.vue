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
    <div v-if="showMap" class="row">
      <div class="col">
        <div class="row">
          <div class="col d-flex align-items-end justify-content-start">
            <b-button class="bg-light circle-btn rounded-circle text-dark">
              <font-awesome-icon v-on:click="addMarker" icon="plus"/>
            </b-button>
          </div>
          <div class="col d-flex align-items-end justify-content-end">
            <b-button class="bg-transparent border-0 p-0">
              <font-awesome-icon v-on:click="toggleMap" icon="window-close"/>
            </b-button>
          </div>
        </div>
        <div class="row py-0">
          <GmapMap
                   ref="mapRef"
                   :center="{lat:10, lng:10}"
                   :zoom="12"
                   :options="mapOptions"
                   map-type-id="terrain"
                   class="map">
          </GmapMap>
        </div>
      </div>
    </div>
    <div v-else class="row">
      <div class="col d-flex justify-content-center">
        <b-button class="circle-btn rounded-circle" v-on:click="toggleMap()" variant="light">
          <font-awesome-icon icon="map"/>
        </b-button>
      </div>
    </div>
    <div class="row">
      <div class="col d-flex justify-content-center">
        <b-button v-on:click="sauvegarderPlan" variant="success" class="circle-btn rounded-circle" v-on:click="toggleMap()" variant="light">
          Sauvegarder
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
  import {gmapApi} from 'vue2-google-maps'

  let bikeLayer;

  export default {
    name: "plan",
    props: ["plan"],
    data() {
      return {
        planData: this.plan,
        editingTitle: false,
        showMap: false,
        position: null,
        mapOptions: {
          mapTypeControl: false,
          zoomControl: false,
          fullscreenControl: false,
        },
        map: null,
        markers: [],
        directionsService: null,
        directionsDisplay: null,
        mapReady: false,
        polylines: null,
      }
    },
    mounted() {
      this.planData.dateCreation = new Date();
      this.planData.titre = 'Ceci est un titre';
      navigator.geolocation.getCurrentPosition((position) => {
        this.position = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    },
    computed: {
      google: gmapApi
    },
    methods: {
      confirmEdit(event) {
        event.preventDefault();
        this.toggleEdit();
      },
      toggleEdit() {
        this.editingTitle = !this.editingTitle;
      },
      toggleMap() {
        this.showMap = !this.showMap;

        if (!this.showMap) return;

        this.$forceUpdate();
        setTimeout(() => {
          if (this.showMap) {
            this.$refs.mapRef.$mapPromise.then((map) => {
              this.map = map;
              map.panTo(this.position);

              bikeLayer = new this.google.maps.BicyclingLayer();
              const bikeToggleDiv = document.createElement('div');
              new BikeOverlayControl(bikeToggleDiv, map);

              this.directionsService = new google.maps.DirectionsService;
              this.directionsDisplay = new google.maps.DirectionsRenderer({
                draggable: true,
                map: map,
                panel: document.getElementById('right-panel')
              });

              map.controls[this.google.maps.ControlPosition.TOP_CENTER].push(bikeToggleDiv);

              this.mapReady = true;
            });
          }
        }, 100);
      },
      addMarker() {
        const marker = {
          location: this.map.center,
        };

        this.directionsDisplay.addListener('directions_changed', () => {
          console.log('updating directions');
          this.storeWayPoints(this.directionsDisplay.getDirections());
        });

        this.markers.push(marker);
        this.displayRoute();
      },
      displayRoute () {
        if (this.markers.length < 2) return;

        const params = {
          origin: this.markers[0],
          destination: this.markers[this.markers.length - 1],
          travelMode: 'BICYCLING'
        };

        if (this.markers.length >= 3) {
          params.waypoints = this.markers
            .slice(1, this.markers.length - 2);
        }

        this.directionsService.route(params, (response, status) => {
          if (status === 'OK') {
            this.directionsDisplay.setDirections(response);
          } else {
            alert('Could not display directions due to: ' + status);
          }
        });
      },
      storeWayPoints(directions) {
        this.markers.length = 0;
        this.markers.push(directions.request.origin);

        if (directions.request.waypoints) {
          directions.request.waypoints.forEach(w => {
            this.markers.push(w);
          });
        }

        this.markers.push(directions.request.destination);

        this.polylines
      },
      sauvegarderPlan() {

      }
    }
  }

  function BikeOverlayControl(controlDiv, map, center) {
    var ctrl = this;

    ctrl.center_ = center;
    controlDiv.style.clear = 'both';

    var container = document.createElement('div');
    container.id = 'toggleBikeButton';
    container.title = 'Cliquer pour afficher ou cacher les pistes cyclables';
    container.style.backgroundColor = '#fff';
    container.style.border = '2px solid #fff';
    container.style.borderRadius = '3px';
    container.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
    container.style.cursor = 'pointer';
    container.style.marginBottom = '22px';
    container.style.textAlign = 'center';
    controlDiv.appendChild(container);

    var text = document.createElement('div');
    text.id = 'toggleBikeText';
    text.innerHTML  = 'Afficher pistes cyclables';
    container.appendChild(text);

    ctrl.showBikes = false;

    container.addEventListener('click', () => {
      ctrl.showBikes = !ctrl.showBikes;

      if (ctrl.showBikes) {
        bikeLayer.setMap(map);
      } else {
        bikeLayer.setMap(null);
      }
    });
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
