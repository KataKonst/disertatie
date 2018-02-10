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
        <v-card-actions>
          <v-btn flat>{{sentiment}}</v-btn>
          <a :href=reviewUrl>Review Link</a>
          <v-spacer></v-spacer>
          <v-btn icon @click.native="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
          </v-btn>
        </v-card-actions>
        <v-slide-y-transition>
          <v-card-text v-show="show">
            {{review.review}}
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    props: ['review'],
    data: () => ({
      show: false
    }),
    computed: {
      preview: {
        get() {
          return this.$props.review.review.substring(0, 30) + '...'
        }
      },
      reviewUrl : {
        get(){
          return this.$props.review.review_url;
        }
      },
      sentiment: {
        get() {
          let review = this.$props.review;
          console.log(review)
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
  @import "../../styleshets/main";
</style>
