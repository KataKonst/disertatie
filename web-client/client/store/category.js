import Vue from 'vue'
import Vuex from 'vuex'
import categoryAPI from '../api/categories'

Vue.use(Vuex)

const state = {
  categories:[],
  count: 0
}

const mutations = {
  SetCategories (state,categories) {
    state.categories = categories
  }
}

const actions = {
  getCategories({commit}) {
    categoryAPI.getCategories().then(result => {
      commit("SetCategories", result.data)
    })
  }
}

const getters = {
  categories: state => state.categories
}


export default {
  state,
  getters,
  actions,
  mutations
}
