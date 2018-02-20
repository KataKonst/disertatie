import Vue from 'vue'
import Vuex from 'vuex'
import twitterAPI from "../api/twitter";

Vue.use(Vuex)

const state = {
  connect: false,
  tweets: [],
  searchResult:[]
}

const mutations = {
  SOCKET_CONNECT: (state,  status ) => {
    state.connect = true;
  },
  SOCKET_TWEET: (state,  message) => {
    state.tweets.push(message);
  },
  SetFoundTweets(state, result) {
    state.searchResult = result
  }
}

const actions = {
  socket_myevent: (context, message) => {
    (new Vue()).$socket.emit('get_tweets', message);
  },
  searchByLocation({commit}, data) {
    twitterAPI .searchByLocation(data.query, data.page, data.size).then(result => {
      commit("SetFoundTweets", result.data)
    })
  },
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
