<template>
  <div class="text-xs-center mt-5">
    <div class="d-inline-block mr-3 mb-3" v-for="(place,index) in places">
      <place :place="place" :index="index" :page="page" :pagesize="pagesize"></place>
    </div>
  </div>
</template>

<script>
  import Place from './Place'

  export default {
    props: ['places','placeClick','page', 'pagesize'],
    components: {
      Place,
    }
  }
</script>

<style scoped>
</style>
