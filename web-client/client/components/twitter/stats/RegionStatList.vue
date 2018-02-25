<template>
  <div class="text-xs-center mt-5">
    <div class="d-inline-block mr-3 mb-3" v-for="(stat, index) in stats">
      <region-stat :stat="stat" :index="index" :page="page" :regionClick="regionClick" :pageSize="pageSize"></region-stat>
    </div>
  </div>
</template>

<script>
  import RegionStat from './RegionStat'

  export default {
    props: ['stats', 'regionClick', 'page', 'pageSize'],
    components: {
      RegionStat,
    }
  }
</script>

<style scoped>
</style>
