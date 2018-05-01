<template>
<div>
  <b>Stars</b>
  <star-rating class="ml-5" star-size=20 read-only=true show-rating=false v-model="stars"></star-rating>
</div>
</template>

<script>
import StarRating from 'vue-star-rating'

  export default {
    props: ['stars'],
        data: () => ({
      show: false
    }),
    components: {
      StarRating,
    },
  }
  
</script>

<style scoped>
</style>
