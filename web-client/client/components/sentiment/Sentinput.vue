<template>
  <v-content>
    <v-card color="grey lighten-4" flat>
      <v-card-text>
        <v-subheader>Light Theme</v-subheader>
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
      <v-flex xs2>
        <v-select class="ml-5" v-bind:items="algoritms" v-model="algoritm" label="Select" single-line
                  bottom></v-select>
      </v-flex>
      <v-card v-if="sentimentResult">
        <v-card-text>
          neu: {{sentimentResult.neu}}
          neg: {{sentimentResult.neg}}
          pos: {{sentimentResult.pos}}
          compound: {{sentimentResult.compound}}
        </v-card-text>
      </v-card>
      <v-btn @click="calculate">Calculate</v-btn>

    </v-card>
  </v-content>

</template>

<script>
  export default {
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
        ],
      }
    },
    methods: {
      calculate: function (event) {
        console.log(this.$store.state)
        this.$store.dispatch("calculateSentiment",
          {input: this.$data.sentimentInput, alg: this.$data.algoritm})
      }
    },
    computed: {
      sentimentResult: {
        get() {
          return this.$store.state.sentiment.sentimentResult
        },
        set(value) {
        }
      }
    }
  }

</script>

<style scoped>

</style>
