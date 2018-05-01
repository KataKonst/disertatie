<template>
  <div>
    <tweet-list v-if="hashtagTweetsResults &&hashtagTweetsResults.length !== 0" :tweets="hashtagTweetsResults.results">
    </tweet-list>
    <div v-if="hashtagTweetsResults &&hashtagTweetsResults.length !== 0" class="text-xs-center mb-5">
      <v-pagination  total-visible=7 :length="hashtagTweetsResultsLength" v-model="page"></v-pagination>
    </div>
  </div>
</template>

<script>
  import TweetList from "../tweet/TweetList";

  export default {
    components: {
      TweetList,
    },
    props: ['hashtag'],
    name: "hashtag-tweets",
    data() {
      return {
        page: null,
      }
    },
    beforeMount() {      this.$data.page = 1
      this.$store.dispatch('getHashtagTweets', {
        hashtag: this.$props.hashtag,
        page: 1, size: 16
      })
    },
    computed: {
      hashtagTweetsResults: {
        get() {
          return this.$store.state.twitter.hashtagTweetsResult
        }
      },
      hashtagTweetsResultsLength: {
        get() {
          return Math.ceil(this.$store.state.twitter.hashtagTweetsResult.length / 16)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('getHashtagTweets', {
          hashtag: this.$props.hashtag,
          page: val, size: 16
        })
      },
     placeName: function (val) {
        this.$store.dispatch('getHashtagTweets', {
          hashtag: this.$props.hashtag,
          page: 1, size: 16
        })
      }
    }
  }
</script>

<style scoped>

</style>
