<template>
	<div>
		<div id="myChart" style="width: 80%;height: 600px;"></div>
	</div>
	
</template>

<script>
import echarts from 'echarts'
import * as d3 from 'd3'
export default {
  name: 'VideoLineChart',
  props:['upId','rawDataProp'],
  mounted(){
	// this.DealData();
	// this.$nextTick(() => {
	// 	this.DealData();
    // });
    this.loadData().then(this.dealData)
    .then(this.draw)
  },
  data () {
    return {
      rawData: [],
      data: []
    }
  },
  watch:{
    'upId'(){
      this.dealData();
      this.draw()
    }
  },
  methods: {
      loadData(){
        return this.$props.rawDataProp.then(d => {
            console.log(d[0])
            this.rawData = d;
        });
      },
      dealData(){
          this.data = this.rawData
            .filter((d) => d.owner === this.$props.upId)
            .map((data1) => {
              return {
                time: ""+data1.time,
                // view: [""+data1.view],
				// favorite: [""+data1.favorite],
				// coin: [""+data1.coin],
                // share: [""+data1.share],
                datetime: new Date(data1.time),
				view: [""+data1.time.substring(0,10), +data1.view],
				favorite: [""+data1.time.substring(0,10), +data1.favorite],
				coin: [""+data1.time.substring(0,10), +data1.coin],
				share: [""+data1.time.substring(0,10), +data1.share],
                }            
            })
            .sort((a, b) => a.datetime - b.datetime);
      },
      draw(){
          let data=this.data
        //   console.log(data,"video")
          var viewData=[];
			var favoriteData=[];
			var coinData=[];
			var shareData=[];
			//var theData = [["2020-03-10", 8851508], ["2019-12-08", 6589367], ["2020-03-02", 802968]];
			for(var i=0;i<data.length;i++){
				viewData.push(data[i].view);
				favoriteData.push(data[i].favorite);
				coinData.push(data[i].coin);
				shareData.push(data[i].share);
				//theData.time = data[i].time.substring(0, 9);
			}
			// console.log("view"+viewData);
			// console.log("favorite"+favoriteData);
			// console.log("coin"+coinData);
			// console.log("share"+shareData);
			//var allData=[viewData,favoriteData,coinData,shareData];
			let myChart = echarts.init(document.getElementById('myChart'))
			var option2 = {
				legend: {
					data:['播放量', '点赞量', '投币量', '分享量'],
				},
				tooltip: {
					show: true,
					trigger: 'axis',
				},
				title: {
					//left: 'center',
					text: '4.1.4',
				},
				toolbox: {
					feature: {
						dataZoom: {
							yAxisIndex: 'none'
						},
						restore: {},
						saveAsImage: {}
					}
				},
				xAxis: {
					type: 'time',
					splitNumber: 13,
					/*axisLable: {
						formatter: function(value){
							return new Date(value).toLocaleTimeString();
						}
					},*/
					
				},
				yAxis: { 
					type: 'value',
					//interval: 100000,
					boundaryGap: ["0", "100%"],
					min: function(value){
						return value.min-30000;
					},
					max: function(value){
						return value.max+30000;
					},
					},
				dataZoom: [{
					type: 'slider',
					show: true,
					yAxisIndex: [0],
					start: 0,
					end: 70
				}, {
					type: 'inside',
					yAxisIndex: [0],
					start: 1
				},{
					type: 'slider',
					show: true,
					xAxisIndex: [0],
					start: 1, 
					end: 30
				},{
					type: 'inside',
					xAxisIndex: [0],
					start: 1,
					end: 10
				}],
				series:[{
					name: '播放量',
					type: 'line',
					//smooth: true,
					//stack: '总量',
					data: viewData,
				},
				{
					name: '点赞量',
					type: 'line',
					//smooth: true,
					//stack: '总量',
					data: favoriteData,					
				},
				{
					name: '投币量',
					type: 'line',
					//stack: '总量',
					data: coinData,
				},
				{
					name: '分享量',
					type: 'line',
					//stack: '总量',
					data: shareData,
				}]
			};
			myChart.setOption(option2,true);
      },
	DealData(){
		d3.dsv(",","static/temp_data_sorb.csv", function(data1){
			//console.log(data1);
			return {
				time: ""+data1.time,
				view: [""+data1.time.substring(0,10), +data1.view],
				favorite: [""+data1.time.substring(0,10), +data1.favorite],
				coin: [""+data1.time.substring(0,10), +data1.coin],
				share: [""+data1.time.substring(0,10), +data1.share],
			};
		}).then(function(data){
			
			//console.log(data);
			var viewData=[];
			var favoriteData=[];
			var coinData=[];
			var shareData=[];
			//var theData = [["2020-03-10", 8851508], ["2019-12-08", 6589367], ["2020-03-02", 802968]];
			for(var i=0;i<data.length;i++){
				viewData.push(data[i].view);
				favoriteData.push(data[i].favorite);
				coinData.push(data[i].coin);
				shareData.push(data[i].share);
				//theData.time = data[i].time.substring(0, 9);
			}
			console.log("view"+viewData);
			console.log("favorite"+favoriteData);
			console.log("coin"+coinData);
			console.log("share"+shareData);
			//var allData=[viewData,favoriteData,coinData,shareData];
			let myChart = echarts.init(document.getElementById('myChart'))
			var option2 = {
				legend: {
					data:['播放量', '点赞量', '投币量', '分享量'],
				},
				tooltip: {
					show: true,
					trigger: 'axis',
				},
				title: {
					//left: 'center',
					text: '4.1.4',
				},
				toolbox: {
					feature: {
						dataZoom: {
							yAxisIndex: 'none'
						},
						restore: {},
						saveAsImage: {}
					}
				},
				xAxis: {
					type: 'time',
					splitNumber: 13,
					/*axisLable: {
						formatter: function(value){
							return new Date(value).toLocaleTimeString();
						}
					},*/
					
				},
				yAxis: { 
					type: 'value',
					//interval: 100000,
					boundaryGap: ["0", "100%"],
					min: function(value){
						return value.min-30000;
					},
					max: function(value){
						return value.max+30000;
					},
					},
				dataZoom: [{
					type: 'slider',
					show: true,
					yAxisIndex: [0],
					start: 0,
					end: 100
				}, {
					type: 'inside',
					yAxisIndex: [0],
					start: 1
				},{
					type: 'slider',
					show: true,
					xAxisIndex: [0],
					start: 1, 
					end: 100
				},{
					type: 'inside',
					xAxisIndex: [0],
					start: 1,
					end: 10
				}],
				series:[{
					name: '播放量',
					type: 'line',
					//smooth: true,
					//stack: '总量',
					data: viewData,
				},
				{
					name: '点赞量',
					type: 'line',
					//smooth: true,
					//stack: '总量',
					data: favoriteData,					
				},
				{
					name: '投币量',
					type: 'line',
					//stack: '总量',
					data: coinData,
				},
				{
					name: '分享量',
					type: 'line',
					//stack: '总量',
					data: shareData,
				}]
			};
			myChart.setOption(option2,true);
		});


	},
  }
}

</script>

<style scoped>
#myChart {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  text-align: center;
  left:100px;
}
</style>
