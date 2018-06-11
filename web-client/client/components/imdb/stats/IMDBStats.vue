<template>
  <div>
      <v-flex xs3>
    <v-select class="ml-5" 
               v-on:change="onChange"
               v-model="selectedType" 
               v-bind:items="types" 
               label="Select" single-line
               bottom></v-select>
       </v-flex>
    <review-list :reviews="statsList.results" :page="page" :pagesize=5 v-if="statsList && statsList.length !== 0">
    </review-list>

    <div v-if="statsList && statsList.length !== 0" class="text-xs-center mb-5">
      <v-pagination total-visible=7 :length="statsLength" v-model="page"></v-pagination>
    </div>
  </div>

</template>

<script>
  import ReviewList from "../review/ReviewList";

 export default {
    components: {
      ReviewList,
    },
    data() {
      return {
        page: null,
        name: null,
        selectedType: {
            text: 'All',
            type: 'all',
            language: 'ro'
          },
         types: [
          {
           text: 'Test Ro',
           type: 'test',
           language: 'ro'
          },
          {
            text: 'Train Ro',
            type: 'train',
            language: 'ro'
          },
           {
            text: 'All Ro',
            algorithm: 'all',
            language: 'ro'
          },
           {
           text: 'Test En',
           type: 'test',
           language: 'en'
          },
          {
            text: 'Train en',
            type: 'train',
            language: 'en'
          },
           {
            text: 'All en',
            algorithm: 'all',
            language: 'en'
           }
        ],
      }
    },
      methods: {
      setPlace(place) {
        this.$router.push({ path: '/place/name/'+game })
      },
      onChange(item) {
           this.$store.dispatch('getIMDBReviews', {
           page: 1, size: 5, type: item.type, language:item.language
       })      
      }
    },
    beforeMount() {
      this.$data.page = 1
      this.$store.dispatch('getIMDBReviews', {
        page: 1, size: 5, type: this.$data.selectedType.type,
        language: this.$data.selectedType.language
      })
    },
    computed: {
      statsList: {
        get() {
          return this.$store.state.imdb.imdbReviews
        }
      },
      statsLength: {
        get() {
          return Math.ceil(this.$store.state.imdb.imdbReviews.length / 5)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('getIMDBReviews', {
          page: val, size: 5, type: this.$data.selectedType.type,
        language: this.$data.selectedType.language
        })
      }
    }
  }
</script>

<style scoped>

</style>
