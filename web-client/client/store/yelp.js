import Vue from 'vue'
import Vuex from 'vuex'
import yelpAPI from '../api/yelp'

Vue.use(Vuex)

const state = {
  searchResult: [],
  games: [],
  statsList: []
}

const mutations = {
  SetSearchedYelpReviews(state, result) {
    state.searchResult = result
  },
  SetYelpStats(state, result) {
    state.statsList = result
  },
}

const actions = {
  searchYelpReviews({commit}, data) {
    yelpAPI.searchByName(data.query, data.page, data.size).then(result => {
      commit("SetSearchedYelpReviews", result.data)
    })
  },
  getPlaceStats({commit},data) {
    yelpAPI.getAverageSentYelp(data.page, data.size, data.algorithm).then(result => {
      commit("SetYelpStats", result.data)
    }) 
   }
}

const getters = {
  searchResult: state => state.searchResult
}

export default {
  state,
  getters,
  actions,
  mutations
}
