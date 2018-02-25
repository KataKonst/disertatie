import Vue from 'vue'
import Vuex from 'vuex'
import twitterAPI from "../api/twitter";

Vue.use(Vuex)

const state = {
  connect: false,
  tweets: [],
  searchResult:[],
  statsList:[],
  locationFullResults:[],
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
  },
  SetStatsTweets(state, result) {
    state.statsList = result
  },
  SetLocationFullNameTweets(state, result) {
    console.log(result)
    state.locationFullResults =  result
  }
}

const actions = {
  socket_myevent: (context, message) => {
    (new Vue()).$socket.emit('get_tweets', message);
  },
  searchByLocation({commit}, data) {
    twitterAPI.searchByLocation(data.query, data.page, data.size).then(result => {
      commit("SetFoundTweets", result.data)
    })
  },
  getTwitterStats({commit},data) {
    twitterAPI.getStats(data.page, data.size).then(result => {
      commit("SetStatsTweets", result.data)
    }) 
   },
   getLocationFullNameTweets({commit}, data){
    twitterAPI.searchByLocationFullName(data.region ,data.page, data.size).then(result => {
      commit("SetLocationFullNameTweets", result.data)
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
