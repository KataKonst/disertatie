<template>
  <div>
     <v-content>

      <v-flex xs8>
    <region-stat-list :page="page" :pageSize=5 v-if="statsList && statsList.length !== 0" :stats="statsList.results" :regionClick="setRegion">
    </region-stat-list>
    <div v-if="statsList && statsList.length !== 0" class="text-xs-center">
      <v-pagination :length="statsLength" v-model="page"></v-pagination>
    </div>
    </v-flex>
      <v-flex xs4>

    <div v-if="name">
      <region-tweets :placeName="name"></region-tweets>
    </div>
          </v-flex>
     </v-content>

  </div>

</template>

<script>
  import RegionStatList from "./RegionStatList";
  import RegionTweets from "./RegionTweets";

 export default {
    components: {
      RegionStatList,
      RegionTweets
    },
    data() {
      return {
        page: null,
        name: null
      }
    },
      methods: {
      setRegion(region) {
       this.$data.name = region
      }
      },
    beforeMount() {
      this.$data.page = 1
      this.$store.dispatch('getTwitterStats', {
        page: 1, size: 5
      })
    },
    computed: {
      statsList: {
        get() {
          return this.$store.state.twitter.statsList
        }
      },
      statsLength: {
        get() {
          return Math.ceil(this.$store.state.twitter.statsList.length / 5)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('getTwitterStats', {
          page: val, size: 5
        })
      }
    }
  }
</script>

<style scoped>

</style>
