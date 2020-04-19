<template>
  <div id="app">
    <p>App.vue</p>
    <!-- <VChart /> -->
    <!-- <BarChart /> -->
    <Map />
    <!-- <PieAndLineChart /> -->
    <!-- <LineChart /> -->
    <!-- <router-view/> -->
  </div>
</template>

<script>
import VChart from '@/components/V-Chart'
import LineChart from '@/components/LineChart'
import BarChart from '@/components/BarChart'
import PieAndLineChart from '@/components/PieAndLineChart'
import Map from '@/components/Map'
export default {
  name: 'App',
  components: {
    // VChart,
    // LineChart,
    // BarChart,
    // PieAndLineChart,
    Map
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
