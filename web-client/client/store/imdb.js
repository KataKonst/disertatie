import Vue from 'vue'
import Vuex from 'vuex'
import imdbAPI from '../api/imdb'

Vue.use(Vuex)

const state = {
  imdbReviews: []
}

const mutations = {
  SetIMDBReviews(state, result) {
    state.imdbReviews = result
  },
 }

const actions = {
  getIMDBReviews({commit}, data) {
    imdbAPI.getIMDBReviews(data.type, data.language, data.page, data.size).then(result => {
      commit("SetIMDBReviews", result.data)
    })
  },
}

const getters = {
  imdbReviews: state => state.imdbReviews
}

export default {
  state,
  getters,
  actions,
  mutations
}
