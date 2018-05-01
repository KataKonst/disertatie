<template>
<div>
  <b>Bayes</b>
  <p>value : {{sentiment}}</p>
</div>
</template>


<script>

  export default {
    props: ['sentiment'],
     computed: {
      sentiment: {
        get() {
         return this.props==1 ? "positive" : "negative"
        }
      }
    }
  }
  
</script>

<style scoped>
</style>
