import Vue from 'vue'
import Vuex from 'vuex'
import categoryStore from './category'
import sentimentStore from './sentiment'
import reviewStore from './review'
import yelpStore from './yelp'
import twitter from './twitter'
import VueSocketio from 'vue-socket.io';
import socketio from 'socket.io-client'

Vue.use(Vuex)

const state = {
  count: 0
}

const mutations = {
  INCREMENT (state) {
    state.count++
  },
  DECREMENT (state) {
    state.count--
  }
}

const actions = {
  incrementAsync ({ commit }) {
    setTimeout(() => {
      commit('INCREMENT')
    }, 200)
  }
}

const store = new Vuex.Store({
  mutations,
  actions,
  modules: {
    category:categoryStore,
    sentiment: sentimentStore,
    reviews: reviewStore,
    yelp: yelpStore,
    twitter: twitter
  }
})

Vue.use(VueSocketio, socketio('http://localhost:8080'), store);
export default store
