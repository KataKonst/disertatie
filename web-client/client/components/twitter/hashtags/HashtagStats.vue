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
    <hashtag-list :page="page" :pageSize=5 v-if="statsList && statsList.length !== 0" :stats="statsList.results" :hashtagClick="setHashtag">
    </hashtag-list>
    <div v-if="statsList && statsList.length !== 0" class="text-xs-center">
      <v-pagination :length="statsLength" v-model="page"></v-pagination>
    </div>
    </v-flex>
      <v-flex>
   </v-flex>
  </div>

</template>

<script>
  import HashtagList from "./HashtagList";

 export default {
    components: {
      HashtagList,
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
        ],
      }
    },
      methods: {
      setHashtag(hashtag) {
        this.$router.push({ path: '/twitter/hashtag/'+hashtag })
      },
      onChange(item) {
           this.$store.dispatch('getTwitterHashtagStats', {
        page: 1, size: 5, algorithm: item.algorithm
      })      }
      },
    beforeMount() {
      this.$data.page = 1
      this.$store.dispatch('getTwitterHashtagStats', {
        page: 1, size: 5, algorithm: this.$data.selectedAlgorithm.algorithm
      })
    },
    computed: {
      statsList: {
        get() {
          return this.$store.state.twitter.statsHashtagList
        }
      },
      statsLength: {
        get() {
          return Math.ceil(this.$store.state.twitter.statsHashtagList.length / 5)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('getTwitterHashtagStats', {
          page: val, size: 5, algorithm: this.$data.selectedAlgorithm.algorithm
        })
      }
    }
  }
</script>

<style scoped>

</style>
