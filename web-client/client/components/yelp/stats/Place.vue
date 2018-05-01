<template>
  <v-layout row>
    <v-flex>
      <v-card>
        <v-card-title primary-title>
          <div>
          <div class="headline">{{ pagesize*(page-1) + index + 1 }}. {{place._id}}</div>
          <p class="grey--text">Sentiment score: {{place.avg}}</p>
          <p class="grey--text">count {{place.count}}</p>
          </div>
        </v-card-title>
        <v-card-actions>
          <router-link :to="{ path: place._id }">Reviews</router-link>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    props: ['place','index','page', 'pagesize'],
    data: () => ({
      show: false
    }),
  }
</script>

<style lang="scss">
  @import "../../../styleshets/main";
</style>
