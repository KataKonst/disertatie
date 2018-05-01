<template>
<div>
  <b>Vader</b>
    <v-btn icon @click.native="show = !show">
        <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
    </v-btn>
    <v-slide-y-transition>
        <v-card-text v-show="show">
           <p>negative: {{sentiment.neg}}</p>
           <p>neutral: {{sentiment.neu}}</p>
           <p>positive: {{sentiment.pos}}</p>
           <p>compound: {{sentiment.compound}}</p>
        </v-card-text>
    </v-slide-y-transition>
  <p>value : {{value}}</p>
</div>
</template>

<script>

  export default {
    props: ['sentiment'],
        data: () => ({
      show: false
    }),
     computed: {
      value: {
        get() {
          let review = this.$props.review;
          if ( this.$props.sentiment && this.$props.sentiment.compound >= 0.5) {
            return "positive";
          } else if (this.$props.sentiment.compound > -0.5 && this.$props.sentiment.compound < 0.5) {
            return "neutral"
          } else {
            return "negative"
          }
        }
      }
    }
  }
  
</script>

<style scoped>
</style>
