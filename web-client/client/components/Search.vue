<template>
  <div class="search-wrapper">
    <v-content>
      <v-flex xs8 offset-xs2>
        <v-form v-model="valid" ref="form">
          <v-layout row wrap>
            <v-flex xs10>
              <v-text-field icon="search" v-model="searchQuery"
                            name="input-1" label="Search" v-on:keyup.enter="onSubmit" id="testing">
              </v-text-field>
            </v-flex>
            <v-flex xs2>
              <v-select class="ml-5" v-bind:items="categories" v-model="category" label="Select" single-line
                        bottom>
              </v-select>
            </v-flex>
          </v-layout>
        </v-form>
      </v-flex>
    </v-content>

    <review-list v-if="reviewList && reviewList.length !== 0" :reviews="reviewList.results">
    </review-list>
    <game-list v-if="gamesList && gamesList.length !== 0" :games="gamesList.results">
    </game-list>
    <div v-if="reviewList && reviewList.length !== 0" class="text-xs-center">
      <v-pagination :length="reviewsLength" v-model="page"></v-pagination>
    </div>
    <div v-if="gamesList && gamesList.length !== 0" class="text-xs-center">
      <v-pagination :length="gamesLength" v-model="page"></v-pagination>
    </div>
  </div>
</template>

<script>
  import ReviewList from "./review/ReviewList";
  import GameList from "./game/GameList";

  export default {
    components: {
      ReviewList,
      GameList
    },
    data() {
      return {
        page: null,
        category: null,
        searchQuery: null,
      }
    },
    beforeMount() {
      this.$store.dispatch("getCategories")
      this.$store.commit('SOCKET_CONNECT', "Adad")
    },
    computed: {
      categories: {
        get() {
          return this.$store.state.category.categories
        },
        set(value) {
          this.$store.commit('updateMessage', value)
        }
      },
      reviewList: {
        get() {
          return this.$store.state.reviews.searchResult
        },
        set(value) {
        }
      },
      gamesList: {
        get() {
          return this.$store.state.games.searchResult
        },
        set(value) {
        }
      },
      reviewsLength: {
        get() {
          return Math.ceil(this.$store.state.reviews.searchResult.length / 4)
        }
      },
      gamesLength: {
        get() {
          return Math.ceil(this.$store.state.games.searchResult.length / 4)
        }
      },
    },
    watch: {
      page: function (val) {
        this.$store.dispatch('allGames', {
          query: this.$data.searchQuery,
          page: val, size: 4
        })
      }
    },
    methods: {
      onSubmit: function (event) {
        this.$data.page = 1
        this.$store.dispatch('allGames', {
          query: this.$data.searchQuery,
          page: 1, size: 4
        })
      },
    }
  }

</script>

<style>

</style>
