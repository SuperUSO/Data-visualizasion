<template>
  <div id="app">
    <!-- <PopularityLineAndBarChart :upId="upId" :rawDataProp="getVideoData"/> -->
    <MainChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/>
    <!-- <VideoLineChart :upId="upId" :rawDataProp="getVideoData"/> -->
    <!-- <BarStackChart @selectUp="selectUp($event)" :rawDataProp="getVideoData"/> -->
    <WordCloud />
  </div>
</template>

<script>
import MainChart from '@/components/MainChart'
import VideoLineChart from '@/components/VideoLineChart'
import BarStackChart from '@/components/BarStack'
import PieAndLineChart from '@/components/PieAndLineChart'
import PopularityLineAndBarChart from '@/components/PopularityLineAndBarChart'
import WordCloud from '@/components/WordCloud'
export default {
  name: 'App',
  components: {
    MainChart,
    BarStackChart,
    VideoLineChart,
    PopularityLineAndBarChart,
    WordCloud
  },
  data(){
    return {
      upId: "38351330",
      upData: [],
      videoData: [],
    }
  },
  computed:{
    getUpData(){
      return this.$d3.csv('static/up_data.csv').then((d) => {
        this.upData = d;
        return d;
      })
    },
    getVideoData(){
      return this.$d3.csv('static/video_data.csv').then((d) => {
        this.videoData = d;
        return d;
      })
    }
  },
  methods:{
    selectUp(upId){
      this.upId = upId;
    }
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
