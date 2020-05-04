<template>
  <div id="app">
    <!-- <div>
      <el-row :gutter="10">
        <el-col :span="13">
          <el-row :gutter="10">
            <el-col :span="9"><div class="grid-content2 bg-purple">
              <BarStackChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/>
            </div></el-col>
            <el-col :span="11"><div class="grid-content2 bg-purple">
              <MainChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/>
            </div></el-col>
          </el-row>
        </el-col>
        <el-col :span="6">
          <el-col :span="24">
            <PopularityLineAndBarChart :upId="upId" :rawDataProp="getVideoData"/>
          </el-col>
        </el-col>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <div class="grid-content3 bg-purple">
            <div id="myChart" style="width: 95%;height: 400px;"></div>
          </div>
        </el-col>
        <el-col :span="12"><div class="grid-content3 bg-purple"></div></el-col>
      </el-row>
    </div> -->
    <div class="container">
      <div class="col1">
        <BarStackChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/>
      </div>
      <div class="col2">
        <MainChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/>
        <VideoLineChart :upId="upId" :rawDataProp="getVideoData"/>
      </div>
      <div class="col3">
        <WordCloud :upId="upId" />
        <PopularityLineAndBarChart :upId="upId" :rawDataProp="getVideoData"/>
      </div>
    </div>
    <!-- <PopularityLineAndBarChart :upId="upId" :rawDataProp="getVideoData"/> -->
    <!-- <MainChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/> -->
    <!-- <VideoLineChart :upId="upId" :rawDataProp="getVideoData"/> -->
    <!-- <BarStackChart @selectUp="selectUp($event)" :rawDataProp="getUpData"/> -->
    <!-- <WordCloud :upId="upId" /> -->
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

<style scoped>
.container{
  display: flex;
}
.col1{
  width: 380px;
}
.col2{
  width: 575px;
}
.col3{
  border-left: 1px solid black;
  width: 700px;
}
.grid-content{
	border-radius: 4px;
	min-height: 1000px;
}
.grid-content2{
	border-radius: 4px;
	min-height: 700px;
	margin-bottom: 10px;
}
.grid-content3{
	border-radius: 4px;
	min-height: 400px;
}
.grid-content4{
	border-radius: 4px;
	min-height: 290px;
	margin-bottom: 10px;
}
.grid-content5{
	border-radius: 4px;
	min-height: 700px;
}
.bg-purple{
	background: rgba(170, 170, 255, 0.9);
	
}
</style>
