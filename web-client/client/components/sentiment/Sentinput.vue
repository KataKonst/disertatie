<template>
    <v-card color="grey lighten-4" flat>
      <v-card-text>
        <v-subheader>Analyze text</v-subheader>
        <v-container fluid>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                name="sentiment"
                v-model="sentimentInput"
                label="Sentiment text"
                textarea
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-flex xs4>
        <v-select class="ml-5" v-bind:items="algoritms" v-model="algoritm" label="Select" single-line
                  bottom></v-select>
     
      <v-card v-if="sentimentResult" class="ml-5 mb-3">
        <v-card-text v-if="sentimentResult.method == 'vader'">
                <vader :sentiment=sentimentResult.results> </vader>
        </v-card-text>

          
         <v-card-text v-if="sentimentResult.method == 'stanford'">
          result: {{sentimentResult.results}}
        </v-card-text>
         <v-card-text v-if="sentimentResult.method == 'bayes'">
          result: {{sentimentResult.results}}
        </v-card-text>
        <v-card-text v-if="sentimentResult.method == 'svm'">
          result: {{sentimentResult.results}}
        </v-card-text>
         <v-card-text v-if="sentimentResult.method == 'me'">
          result: {{sentimentResult.results}}
        </v-card-text>
          <v-card-text v-if="sentimentResult.method == 'tf'">
           <tf :sentiment=sentimentResult.results></tf>
        </v-card-text>
      </v-card>
      <v-btn @click="calculate" class="ml-5">Calculate</v-btn>
      </v-flex>
      </v-card>
</template>


<script>
import StarRating from 'vue-star-rating'
import Vader from './display/Vader'
import Tf from './display/Tf'
import Me from './display/Me'

  export default {
        components: {
            Vader,
            Tf
         },
    data() {
      return {
        algoritm: null,
        sentimentInput: null,
        algoritms: [
          {
            text: 'Vader RO',
            language: "ro",
            algorithm: "vader"
          },
          {
            text: 'Vader EN',
            language: "en",
            algorithm: "vader"
          },
          {
            text: 'Stanford EN',
            language: "en",
            algorithm: "stanford"
          },
           {
            text: 'Naive Bayes EN',
            language: "en",
            algorithm: "bayes"
          },
          {
            text: 'Naive Bayes RO',
            language: "ro",
            algorithm: "bayes"
          },
          {
            text: 'SVM EN',
            language: "en",
            algorithm: "svm"
          },
          {
            text: 'SVM RO',
            language: "ro",
            algorithm: "svm"
          },
          {
            text: 'Max Ent',
            language: "en",
            algorithm: "me"
          },
           {
            text: 'Max Ent RO',
            language: "ro",
            algorithm: "me"
          },
           {
            text: 'Tensorflow',
            language: "en",
            algorithm: "tf"
          },
           {
            text: 'Tensorflow RO',
            language: "ro",
            algorithm: "tf"
          }
        ],
      }
    },
    methods: {
      calculate: function (event) {
        this.$store.dispatch("calculateSentiment",
          {input: this.$data.sentimentInput, alg: this.$data.algoritm})
      }
    },
    computed: {
      sentimentResult: {
        get() {
          return this.$store.state.sentiment.sentimentResult
        }
      }
    }
  }

</script>

<style scoped>

</style>
