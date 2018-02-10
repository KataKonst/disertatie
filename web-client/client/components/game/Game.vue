<template>
  <v-layout row>
    <v-flex>
      <v-card>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{game.name}}</div>
            <span class="grey--text">{{preview}}</span>
          </div>
        </v-card-title>
        <v-card-actions>
          <router-link :to="{ path: 'game/'+game.colectionName }">Reviews</router-link>
          <v-spacer></v-spacer>
          <v-btn icon @click.native="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
          </v-btn>
        </v-card-actions>
        <v-slide-y-transition>
          <v-card-text v-show="show">
            {{game.description}}
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    props: ['game'],
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
  @import "../../styleshets/main";
</style>
