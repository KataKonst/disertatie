import axios from 'axios'

export default {
  calculateSentiment (language,alg,input) {
    return axios.post("http://localhost:5000/review/language/"+language+"/method/"+alg, {input})
  },
}
