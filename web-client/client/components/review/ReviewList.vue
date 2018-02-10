<template>
  <div class="text-xs-center mt-5">
    <div class="d-inline-block mr-3 mb-3" v-for="rev in reviews">
        <review :review="rev"></review>
    </div>
  </div>
</template>


<script>
  import Review from './Review'

  export default {
    props: ['reviews'],
    components: {
      Review,
    },
  }
</script>

<style scoped>
</style>
