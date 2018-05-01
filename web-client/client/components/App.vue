<template>
    <v-app>
      <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons' rel="stylesheet">
      <link href="https://unpkg.com/vuetify@1.0.10/dist/vuetify.min.css" rel="stylesheet">
        <v-navigation-drawer  :clipped="clipped" v-model="drawer" app enable-resize-watcher>
            <v-list>
                <v-list-tile>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            <span>Menu</span>
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-divider></v-divider>
                <template v-for="(item) in items">
                    <v-list-tile :href="item.href" :to="{path: item.href}">
                        <v-list-tile-action>
                            <v-icon light v-html="item.icon"></v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title v-html="item.title"></v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar class="indigo" :clipped-left="clipped" dark app>
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title>Sentiment analysis</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click.native.stop="openGithub()">
                <v-icon>home</v-icon>
            </v-btn>
        </v-toolbar>
        <v-content>
            <v-fade-transition mode="out-in">
                    <v-flex xs12>
                <router-view></router-view>
                    </v-flex>
            </v-fade-transition>
        </v-content>
        <v-footer class="indigo pa-3" dark app>
        </v-footer>
    </v-app>
</template>
<script>
 export default {
    data() {
      return {
        drawer: true,
              clipped: false,
        items: [{
          href: '/',
          router: true,
          title: 'Home',
          icon: 'home',
        }, {
          href: '/twitter',
          router: true,
          title: 'Twitter',
          icon: 'extension',
        }, {
          href: '/twitter/stats',
          router: true,
          title: 'Twitter stats',
          icon: 'domain',
        },
        {
          href: '/sentiment',
          router: true,
          title: 'Analyze Sentiment',
          icon: 'domain',
        },
         {
          href: '/hashtag',
          router: true,
          title: 'Hashtag',
          icon: 'domain',
        },
        {
          href: '/yelp/stats',
          router: true,
          title: 'Yelp',
          icon: 'domain',
        }],
      };
    },
    methods: {
      openGithub() {
        window.open('https://github.com/katakonst/sent-proj');
      },
    },
  }
</script>



<style lang="scss">
  @import "../styleshets/main";
 .intro {
  display: flex;
  justify-content: center;
  margin: 4rem 0;
}

a {
  color: inherit;
}

.text-center {
  text-align: center;
}
</style>

