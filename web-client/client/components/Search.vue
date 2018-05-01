<template>
  <div class="search-wrapper">
    <v-content>
      <v-flex xs12>
        <v-form v-model="valid" ref="form">
          <v-layout row wrap>
            <v-flex xs10>
              <v-text-field icon="search" v-model="searchQuery" name="input-1" label="Search" v-on:keyup.enter="onSubmit" id="testing">
              </v-text-field>
            </v-flex>
          </v-layout>
        </v-form>
      </v-flex>
    </v-content>

    <review-list v-if="reviewList &&  reviewList.length !== 0" :reviews=" reviewList.results">
    </review-list>
    <div v-if=" reviewList &&  reviewList.length !== 0" class="text-xs-center mb-5">
      <v-pagination total-visible=7  :length="reviewsLength" v-model="page"></v-pagination>
    </div>
  </div>
</template>

<script>
  import ReviewList from "./yelp/review/ReviewList";

  export default {
    components: {
      ReviewList,
    },
    data() {
      return {
        page: null,
        name: null,
        searchQuery: null,
      }
    },
    beforeMount() {
      this.$store.dispatch("getGames")
      this.$store.commit('SOCKET_CONNECT', "Adad")
    },
    computed: {
      games: {
        get() {
          return this.$store.state.games.games
        },
        set(value) {
          this.$store.commit('updateMessage', value)
        }
      },
      gameReviewList: {
        get() {
          return this.$store.state.yelp.searchResult
        },
        set(value) {}
      },
      reviewList: {
        get() {
          return this.$store.state.yelp.searchResult
        },
        set(value) {
        }
      },
      reviewsLength: {
        get() {
          return Math.ceil(this.$store.state.yelp.searchResult.length / 4)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('searchYelpReviews', {
          query: this.$data.searchQuery,
          page:  val, size: 4
        })
      }
    },
    methods: {
      onSubmit: function (event) {
        this.$data.page = 1
        this.$store.dispatch('searchYelpReviews', {
          query: this.$data.searchQuery,
          page:  1, size: 4
        })
      },
    }
  }

</script>

<style>

</style>
