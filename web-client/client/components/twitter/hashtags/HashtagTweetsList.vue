 <template>
   <div>
      <hashtag-tweets :hashtag="$route.params.hashtag"></hashtag-tweets>
   </div>
</template>

<script>
  import HashtagTweets from './HashtagTweets'
  export default {
      components: {
      HashtagTweets
    },
  }
</script>

<style scoped>
</style>