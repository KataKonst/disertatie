import axios from 'axios'

export default {
  searchByName (query, page, size) {
    return axios.get("http://localhost:5000/yelp/name/"+query+"/page/"+page+"/size/"+size)
  },
  getAllGames(page, size) {
    return axios.get("http://localhost:5000/game/all/")
  },
  getAverageSentYelp (page, size, alg) {
    return axios.get("http://localhost:5000/yelp/average/page/"+page+"/size/"+size+"/alg/"+alg)
  },
}
