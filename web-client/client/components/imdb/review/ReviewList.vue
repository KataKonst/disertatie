<template>
    <v-layout row>

    <flex  v-for="rev in reviews" class="mr-5">
        <review :review="rev"></review>
    </flex >
</v-layout>
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
