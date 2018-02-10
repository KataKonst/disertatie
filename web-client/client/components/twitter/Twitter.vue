<template>
  <div>
    <h1>PlaceInput</h1>
    <gmap-place-input label="Add a marker at this place" :select-first-on-enter="true" @place_changed="updatePlace($event)"></gmap-place-input>
    <br>

  <gmap-map
    :center="center"
    :zoom="7"
    style="width: 500px; height: 300px"
  >
    <gmap-marker
      :position=center
      :clickable="true"
      :draggable="true"
      @position_changed="updatePlaceM1($event)"
    ></gmap-marker>
    <gmap-marker
      :position=center
      :clickable="true"
      :draggable="true"
      @position_changed="updatePlaceM2($event)"
    ></gmap-marker>
  </gmap-map>
    <input type="number" v-model="center.lat" number>


    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-list three-line>
            <template v-for="tweet in tweets">
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-sub-title v-html="tweet"></v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>
            </template>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
    <v-btn @click="click()">sadas</v-btn>


  </div>
</template>

<script>

  export default {
    data () {
      return {
        center: {lat: 10.0, lng: 10.0},
        markers: [{
          position: {lat: 10.0, lng: 10.0}
        }, {
          position: {lat: 11.0, lng: 11.0}
        }]
      }
    },
    computed: {
      tweets: {
        get() {
          return this.$store.state.twitter.tweets
        }
      }
    },
    beforeMount() {
    },
    methods :{
      click(center){
        this.$store.dispatch('socket_myevent', {location:[this.markers[0].position,
            this.markers[1].position]})
      },
      updatePlaceM1($event){
        console.log("pos1")
        this.markers[0].position={lat:$event.lat(), lng: $event.lng()}
      },
      updatePlaceM2($event){
        this.markers[1].position={lat:$event.lat(), lng: $event.lng()}
      }
    }
  }

</script>
