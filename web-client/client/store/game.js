import Vue from 'vue'
import Vuex from 'vuex'
import gameAPI from '../api/game'

Vue.use(Vuex)

const state = {
  searchResult: []
}

const mutations = {
  SetSearchedGames(state, result) {
    state.searchResult = result
  }
}

const actions = {
  searchGame({commit}, data) {
    gameAPI.searchByName(data.query, data.page, data.size).then(result => {
      commit("SetSearchedGames", result.data)
    })
  },
  allGames({commit}, data) {
    gameAPI.all(data.page, data.size).then(result => {
      commit("SetSearchedGames", result.data)
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
