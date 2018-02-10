import Vue from 'vue'
import Vuex from 'vuex'
import reviewsAPI from '../api/review'

Vue.use(Vuex)

const state = {
  searchResult:[]
}

const mutations = {
  SetSearchedReviews(state,result) {
    state.searchResult = result
    console.log(state)
  }
}

const actions = {
  searchGameReviews({commit},data) {
    reviewsAPI.searchGameRevByCol(data.query, data.page, data.size).then(result => {
      commit("SetSearchedReviews", result.data)
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
