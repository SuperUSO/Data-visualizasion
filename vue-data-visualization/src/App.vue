<template>
  <div id="app">
    <p>App.vue</p>
    <!-- <VChart /> -->
    <!-- <BarChart /> -->
    <!-- <Map /> -->
    <PopularityLineAndBarChart />
    <!-- <LineChart /> -->
    <!-- <router-view/> -->
  </div>
</template>

<script>
import VChart from '@/components/V-Chart'
import LineChart from '@/components/LineChart'
import BarChart from '@/components/BarChart'
import PieAndLineChart from '@/components/PieAndLineChart'
import PopularityLineAndBarChart from '@/components/PopularityLineAndBarChart'
export default {
  name: 'App',
  components: {
    // VChart,
    LineChart,
    // BarChart,
    // PieAndLineChart,
    PopularityLineAndBarChart
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
