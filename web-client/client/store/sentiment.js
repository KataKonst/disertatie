import Vue from 'vue'
import Vuex from 'vuex'
import sentimentAPI from '../api/sentiment'

Vue.use(Vuex)

const state = {
  sentimentResult:null
}

const mutations = {
  SetSentimentResult (state,result) {
    state.sentimentResult = result
  }
}

const actions = {
  calculateSentiment({commit},data) {
    console.log(data)
    sentimentAPI.calculateSentiment(data.alg.language,data.alg.algorithm,data.input).
    then(result => {
      commit("SetSentimentResult", result.data)
    })
  }
}

const getters = {
  sentiment: state => state.sentimentResult
}

export default {
  state,
  getters,
  actions,
  mutations
}
