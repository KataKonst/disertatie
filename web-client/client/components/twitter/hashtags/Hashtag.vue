<template>
  <v-layout row>
    <v-flex>
      <v-card>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{ pageSize*(page-1) + index + 1 }}. {{ hashtag._id }}</div>
            <p class="grey--text">Sentiment score: {{hashtag.avg}}</p>
            <p class="grey--text">count {{hashtag.count}}</p>
                      </div>
        </v-card-title>
        <v-card-actions>
        <v-btn @click="hashtagClick(hashtag._id)">
            Display Tweets    
        </v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    props: ['hashtag', 'index','hashtagClick', 'page', 'pageSize'],
    data: () => ({
      show: false
    }),
    computed: {    }
  }
</script>

<style lang="scss">
</style>
