import Vue from 'vue'
import Vuex from 'vuex'
import categoryStore from './category'
import sentimentStore from './sentiment'
import reviewStore from './review'
import yelpStore from './yelp'
import twitter from './twitter'
import imdbStore from './imdb'
import VueSocketio from 'vue-socket.io';
import socketio from 'socket.io-client'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    category:categoryStore,
    sentiment: sentimentStore,
    reviews: reviewStore,
    yelp: yelpStore,
    twitter: twitter,
    imdb : imdbStore
  }
})

Vue.use(VueSocketio, socketio('http://localhost:8080'), store);
export default store
