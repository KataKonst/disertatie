import axios from 'axios'

export default {
  searchGameRevByCol (col, page, size) {
    return axios.get("http://localhost:5000/game/name/"+col+"/page/"+page+"/size/"+size)
  },
}
