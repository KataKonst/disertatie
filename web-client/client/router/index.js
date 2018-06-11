import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import SentInput from '../components/sentiment/Sentinput'
import PlaceDetail from '../components/yelp/stats/PlaceDetail'
import Twitter from '../components/twitter/Twitter'
import TwitterStats from '../components/twitter/stats/TwitterStats'
import YelpStats from '../components/yelp/stats/YelpStats'
import IMDBStats from '../components/imdb/stats/IMDBStats'
import RegionTweetsList from '../components/twitter/tweet/RegionTweetsList'
import HashtagStats from '../components/twitter/hashtags/HashtagStats'
import HashtagTweetsList from '../components/twitter/hashtags/HashtagTweetsList'


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
      path: '/twitter/region/:name',
      component: RegionTweetsList
    },
    {
      path: '/twitter/hashtag/:hashtag',
      component: HashtagTweetsList
    },
    {
      path: '/yelp/stats',
      component: YelpStats
    },
    {
      path: '/imdb/stats',
      component: IMDBStats
    },
    {
      path: '/sentiment',
      component: SentInput
    },
    { 
      path: '/yelp/:name', 
      component:PlaceDetail
    },
    { 
      path: '/hashtag', 
      component: HashtagStats
    }
  ]
})
