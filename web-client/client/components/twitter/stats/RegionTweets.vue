<template>
  <div>
    <tweet-list v-if="locationFullResults && locationFullResults.length !== 0" :tweets="locationFullResults.results">
    </tweet-list>
    <div v-if="locationFullResults && locationFullResults.length !== 0" class="text-xs-center mb-5">
      <v-pagination  total-visible=7 :length="locationFullResultsLength" v-model="page"></v-pagination>
    </div>
  </div>
</template>

<script>
  import TweetList from "../tweet/TweetList";

  export default {
    components: {
      TweetList,
    },
    props: ['placeName'],
    name: "region-tweets",
    data() {
      return {
        page: null,
      }
    },
    beforeMount() {
      this.$data.page = 1
      this.$store.dispatch('getLocationFullNameTweets', {
        region: this.$props.placeName,
        page: 1, size: 16
      })
    },
    computed: {
      locationFullResults: {
        get() {
          return this.$store.state.twitter.locationFullResults
        }
      },
      locationFullResultsLength: {
        get() {
          return Math.ceil(this.$store.state.twitter.locationFullResults.length / 16)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('getLocationFullNameTweets', {
          region: this.$props.placeName,
          page: val, size: 16
        })
      },
     placeName: function (val) {
        this.$store.dispatch('getLocationFullNameTweets', {
          region: this.$props.placeName,
          page: 1, size: 16
        })
      }
    }
  }
</script>

<style scoped>

</style>
