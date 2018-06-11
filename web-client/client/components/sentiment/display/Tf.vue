<template>
<div>
  <b>LSTM Tensorflow</b>
  <p>positive: {{sentiment.positive}}</p>
  <p>negative: {{sentiment.negative}}</p>
</div>
</template>

<script>

  export default {
    props: ['sentiment'],
     computed: {
      sentiment: {
        get() {
         return this.$props.sentiment
        }
      }
    }
  }
  
</script>

<style scoped>
</style>
