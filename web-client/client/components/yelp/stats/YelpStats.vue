<template>
  <div>
      <v-flex xs3>
    <v-select class="ml-5" 
               v-on:change="onChange"
               v-model="selectedAlgorithm" 
               v-bind:items="algoritms" 
               label="Select" single-line
               bottom></v-select>
       </v-flex>

      <v-flex xs12>
    <place-list :page="page" :pagesize=5 v-if="statsList && statsList.length !== 0" :places="statsList.results">
    </place-list>
    <div v-if="statsList && statsList.length !== 0" class="text-xs-center mb-5">
      <v-pagination total-visible=7 :length="statsLength" v-model="page"></v-pagination>
    </div>
    </v-flex>
      <v-flex>
   </v-flex>
  </div>

</template>

<script>
  import PlaceList from "./PlaceList";

 export default {
    components: {
      PlaceList,
    },
    data() {
      return {
        page: null,
        name: null,
        selectedAlgorithm: {
            text: 'Vader EN',
            language: "en",
            algorithm: "vader"
          },
         algoritms: [
          {
            text: 'Vader EN',
            language: "en",
            algorithm: "vader"
          },
          {
            text: 'Stanford EN',
            language: "en",
            algorithm: "stanford"
          },
           {
            text: 'SVM en',
            language: "en",
            algorithm: "svm"
           },
           {
            text: 'Bayes en',
            language: "en",
            algorithm: "bayes"
          },
        ],
      }
    },
      methods: {
      setPlace(place) {
        this.$router.push({ path: '/place/name/'+game })
      },
      onChange(item) {
           this.$store.dispatch('getPlaceStats', {
           page: 1, size: 5, algorithm: item.algorithm
       })      
      }
    },
    beforeMount() {
      this.$data.page = 1
      this.$store.dispatch('getPlaceStats', {
        page: 1, size: 5, algorithm: this.$data.selectedAlgorithm.algorithm
      })
    },
    computed: {
      statsList: {
        get() {
          return this.$store.state.yelp.statsList
        }
      },
      statsLength: {
        get() {
          return Math.ceil(this.$store.state.yelp.statsList.length / 5)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('getPlaceStats', {
          page: val, size: 5, algorithm: this.$data.selectedAlgorithm.algorithm
        })
      }
    }
  }
</script>

<style scoped>

</style>
