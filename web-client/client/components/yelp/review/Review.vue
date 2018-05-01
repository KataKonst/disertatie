<template>
  <v-layout row>
    <v-flex>
      <v-card>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{review.productName}}</div>
            <span class="grey--text">{{preview}}</span>
            <v-spacer></v-spacer>
            <span class="grey--text">{{review.sentiment}}</span>
          </div>
        </v-card-title>
           <vader :sentiment=review.vader> </vader>
           <svm :sentiment=review.svm></svm>
           <bayes :sentimen=review.bayes></bayes>
           <stars :stars=review.stars></stars>

          <v-spacer></v-spacer>
          <v-btn icon @click.native="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
          </v-btn>
        <v-slide-y-transition>
          <v-card-text v-show="show">
            {{review.text}}
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import StarRating from 'vue-star-rating'
import Svm from '../../sentiment/display/Svm'
import Stars from '../../sentiment/display/Stars'
import Bayes from '../../sentiment/display/Bayes'
import Vader from '../../sentiment/display/Vader'

 export default {
    props: ['review'],
    data: () => ({
      show: false
    }),
     components: {
      StarRating,
      Vader,
      Stars,
      Svm,
      Bayes
    },
    computed: {
      preview: {
        get() {
          return this.$props.review.text.substring(0, 30) + '...'
        }
      },
      sentiment: {
        get() {
          let review = this.$props.review;
          if (review.vader && review.vader.compound >= 0.5) {
            return "positive";
          } else if (review.vader.compound > -0.5 && review.vader.compound < 0.5) {
            return "neutral"
          } else {
            return "negative"
          }
        }
      }
    }
  }
  
</script>

<style lang="scss">
  @import "../../../styleshets/main";
</style>
