<template>
  <div class="text-xs-center mt-5">
    <div class="d-inline-block mr-3 mb-3" v-for="gm in games">
      <game :game="gm"></game>
    </div>
  </div>
</template>

<script>
  import Game from './Game'

  export default {
    props: ['games'],
    components: {
      Game,
    }
  }
</script>

<style scoped>
</style>
