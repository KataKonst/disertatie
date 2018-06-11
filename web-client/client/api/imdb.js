import axios from 'axios'

export default {
  getIMDBReviews (type, language, page, size) {
    return axios.get("http://localhost:5000/imdb/type/"+type+"/language/"+language+"/page/"+page+"/size/"+size)
  },
}
