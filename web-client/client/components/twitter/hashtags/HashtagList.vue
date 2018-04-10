<template>
  <div class="text-xs-center mt-5">
    <div class="d-inline-block mr-3 mb-3" v-for="(stat, index) in stats">
      <hashtag :hashtag="stat" :index="index" :page="page" :hashtagClick="hashtagClick" :pageSize="pageSize">
     </hashtag>
    </div>
  </div>
</template>

<script>
  import Hashtag from './Hashtag'

  export default {
    props: ['stats', 'hashtagClick', 'page', 'pageSize'],
    components: {
      Hashtag,
    }
  }
</script>

<style scoped>
</style>
