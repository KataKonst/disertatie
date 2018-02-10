import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  connect: false,
  tweets: []
}

const mutations = {
  SOCKET_CONNECT: (state,  status ) => {
    state.connect = true;
    console.log("ASdasd")
  },
  SOCKET_TWEET: (state,  message) => {
    state.tweets.push(message);
  }
}

const actions = {
  socket_myevent: (context, message) => {
    (new Vue()).$socket.emit('get_tweets', message);
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
