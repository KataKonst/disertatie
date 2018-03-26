 <template>
   <div>
      <region-tweets :placeName="$route.params.name"></region-tweets>
   </div>
</template>

<script>
  import RegionTweets from '../stats/RegionTweets'
  export default {
      components: {
      RegionTweets
    },
  }
</script>

<style scoped>
</style>