<template>
  <div>
    <review-list v-if="reviewList && reviewList.length !== 0" :reviews="reviewList.results">
    </review-list>
    <div v-if="reviewList && reviewList.length !== 0" class="text-xs-center mb-5">
      <v-pagination  total-visible=7 :length="reviewsLength" v-model="page"></v-pagination>
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
      }
    },
    beforeMount() {
      this.$data.page = 1
      this.$store.dispatch('searchYelpReviews', {
        query: this.$route.params.name,
        page: 1, size: 16
      })
    },
    computed: {
      reviewList: {
        get() {
          return this.$store.state.yelp.searchResult
        }
      },
      reviewsLength: {
        get() {
          return Math.ceil(this.$store.state.yelp.searchResult.length / 16)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('searchYelpReviews', {
          query: this.$route.params.name,
          page: val, size: 16
        })
      }
    }
  }
</script>

<style scoped>
</style>
