<template>
<div>
  <b>SVM</b>
  <p>value : {{sentiment}}</p>
</div>
</template>

<script>

  export default {
    props: ['sentiment'],
     computed: {
      sentiment: {
        get() {
         return this.$props.sentiment==1 ? "positive" : "negative"
        }
      }
    }
  }
  
</script>

<style scoped>
</style>
