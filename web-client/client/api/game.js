import axios from 'axios'

export default {
  searchByName (name, page, size) {
    return axios.get("http://localhost:5000/game/name/"+name+"/page/"+page+"/size/"+size)
  },
  all(page, size) {
    return axios.get("http://localhost:5000/game/all/page/"+page+"/size/"+size)
  }
}
