import axios from 'axios'

export default {
  searchByLocation (location, page, size) {
    return axios.get("http://localhost:5000/twitter/location/"+location+"/page/"+page+"/size/"+size)
  },
  searchByLocationFullName (location, page, size) {
    return axios.get("http://localhost:5000/twitter/location-full/"+location+"/page/"+page+"/size/"+size)
  },
  getStats (page, size) {
    return axios.get("http://localhost:5000/twitter/average/page/"+page+"/size/"+size)
  }
}
