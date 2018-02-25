import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import SentInput from '../components/sentiment/Sentinput'
import GameDetail from '../components/game/GameDetail'
import Twitter from '../components/twitter/Twitter'
import TwitterStats from '../components/twitter/stats/TwitterStats'



Vue.use(Router)

export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/twitter',
      component: Twitter
    },
    {
      path: '/twitter/stats',
      component: TwitterStats
    },
    {
      path: '/sentiment',
      component: SentInput
    },
    { path: '/game/:name', component:GameDetail  }

  ]
})
