<template>
  <v-layout row>

    <v-flex>
      <v-card>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{preview}}</div>
            <span class="grey--text">{{twt.location}}</span>
            <p>{{twt.vader}}</p>
          </div>
        </v-card-title>
        <v-card-actions>
          <router-link :to="{ path: 'game' }">Reviews</router-link>
          <v-spacer></v-spacer>
          <v-btn icon @click.native="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
          </v-btn>
        </v-card-actions>
        <v-slide-y-transition>
          <v-card-text v-show="show">
            {{twt.text}}
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    props: ['tweet'],
    data: () => ({
      show: false
    }),
    computed: {
      twt: {
        get() {
          return this.$props.tweet[0] ? this.$props.tweet[0] : this.$props.tweet
        },
      },
        preview: {
          get() {
            return this.twt.text.substring(0, 30) + '...'
          }
        }
    }
  }
</script>

<style lang="scss">
  @import "../../../styleshets/main";
</style>
