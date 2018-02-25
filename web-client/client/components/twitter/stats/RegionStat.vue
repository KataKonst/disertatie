<template>
  <v-layout row>
    <v-flex>
      <v-card>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{ pageSize*(page-1) + index + 1 }}. {{ stat._id }}</div>
            <p class="grey--text">VADER score: {{stat.avg}}</p>
            <p class="grey--text">count {{stat.count}}</p>
                      </div>
        </v-card-title>
        <v-card-actions>
        <v-btn @click="regionClick(stat._id)">
            Display Tweets    
        </v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    props: ['stat', 'index','regionClick', 'page', 'pageSize'],
    data: () => ({
      show: false
    }),
    computed: {
      preview: {
        get() {
          return this.$props.game.description.substring(0, 30) + '...'
        }
      }
    }
  }
</script>

<style lang="scss">
</style>
