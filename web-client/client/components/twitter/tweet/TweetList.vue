<template>
  <div class="text-xs-center mt-5">
    <div class="d-inline-block mr-3 mb-3" v-for="tw in tweets">
      <tweet :tweet="tw"></tweet>
    </div>
  </div>
</template>

<script>
  import Tweet from './Tweet'

  export default {
    props: ['tweets'],
    components: {
      Tweet,
    }
  }
</script>

<style scoped>
</style>
