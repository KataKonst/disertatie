<template>
  <div>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <h1>PlaceInput</h1>
        <div class="mb-3">
          <gmap-place-input label="Add a marker at this place" :select-first-on-enter="true"
                            @place_changed="updatePlace($event)"></gmap-place-input>
        </div>

        <gmap-map
          :center="center"
          :zoom="1"
          style="width: 500px; height: 300px"
        >
          <gmap-marker
            :position=markers[0].position
            :clickable="true"
            :draggable="true"
            @position_changed="updatePlaceM1($event)"
          ></gmap-marker>
          <gmap-marker
            :position=markers[1].position
            :clickable="true"
            :draggable="true"
            @position_changed="updatePlaceM2($event)"
          ></gmap-marker>
        </gmap-map>
      </v-flex>
    </v-layout>
    <v-btn @click="click()">Display</v-btn>

    <v-flex xs8 offset-xs2>
        <v-layout row wrap>
          <v-flex xs12>
            <v-text-field icon="search" v-model="searchQuery"
                          name="input-1" label="Search" v-on:keyup.enter="onSubmit" id="testing">
            </v-text-field>
          </v-flex>
        </v-layout>
    </v-flex>

    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <tweet-list :tweets="tweets"></tweet-list>
      </v-flex>
    </v-layout>

    <tweet-list v-if="foundTweets && foundTweets.length !== 0" :tweets="foundTweets.results">
    </tweet-list>
    <div v-if="foundTweets && foundTweets.length !== 0" class="text-xs-center">
      <v-pagination :length="fndTweetsLength" v-model="page"></v-pagination>
    </div>
  </div>
</template>


<script>

  import TweetList from "./tweet/TweetList";

  export default {
    components: {TweetList},
    data() {
      return {
        center: {lat: 14.124631433597454, lng: -164.375},
        markers: [{
          position: {lat: 14.12463143, lng: -164.375}
        }, {
          position: {lat: 59.63931534, lng: -19.53125}
        }],
        searchQuery: null,
        page: null
      }
    },
    computed: {
      tweets: {
        get() {
          return this.$store.state.twitter.tweets
        },
      },
      foundTweets: {
        get() {
          return this.$store.state.twitter.searchResult
         },
      },
      fndTweetsLength: {
        get() {
          return Math.ceil(this.$store.state.twitter.searchResult.length / 4)
        }
      }
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('searchByLocation', {
          query: this.$data.searchQuery,
          page: val, size: 4
        })
      }
    },
    methods: {
      click(center) {
        this.$store.dispatch('socket_myevent', {
          location: [this.markers[0].position,
            this.markers[1].position]
        })
      },
      updatePlace($event) {
        this.markers[0].position = {lat: $event.geometry.location.lat(), lng: $event.geometry.location.lng()}
        this.markers[1].position = {lat: $event.geometry.location.lat(), lng: $event.geometry.location.lng()}
        this.center = this.markers[0].position
      },
      updatePlaceM1($event) {
        this.markers[0].position = {lat: $event.lat(), lng: $event.lng()}
      },
      updatePlaceM2($event) {
        this.markers[1].position = {lat: $event.lat(), lng: $event.lng()}
      },
      onSubmit: function (event) {
        this.$data.page = 1
        console.log(this.$data.searchQuery)
        this.$store.dispatch('searchByLocation', {
          query: this.$data.searchQuery,
          page: 1, size: 6
        })
      }
    }
  }

</script>
