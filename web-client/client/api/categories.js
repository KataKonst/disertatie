import axios from 'axios'

export default {
  getCategories () {
    return axios.get("http://localhost:5000/categories")
  },
}
