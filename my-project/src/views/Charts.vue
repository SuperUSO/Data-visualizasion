<template>
	<div>
		<el-row :gutter="10">
			<el-col :span="18">
				<el-row :gutter="10">
					<el-col :span="8"><div class="grid-content2 bg-purple"></div></el-col>
					<el-col :span="16"><div class="grid-content2 bg-purple"></div></el-col>
				</el-row>
			</el-col>
			<el-col :span="6">
				<el-col :span="24">
					<div class="grid-content4 bg-purple">
						<div id="cloudChart" style="width: 90%;height:290px;"></div>
					</div>
				</el-col>
				<!--el-col :span="24">
					<div class="grid-content5 bg-purple">
						<div id="myChart" style="width: 95%;height: 700px;"></div>
					</div>
				</el-col-->
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
		<!--div id="myChart" style="width: 80%;height: 600px;"></div>
		<div id="cloudChart" style="width: 80%;height: 600px;"></div-->
		<!--el-row: gutter="20">
			<el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
			<el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
			<el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
		</el-row-->
	</div>
	
</template>

<script>
import echarts from 'echarts'
import * as d3 from 'd3'
export default {
  name: 'echart',
  mounted(){
    this.SetCloud();
	this.DealData();
	this.$nextTick(() => {
		this.DealData();
	});
  },
  data () {
    return {
      msg: 'Welcome',
    }
  },
  methods: {
	DealData(){
		d3.dsv(",","temp_data_sorb.csv", function(data1){
			//console.log(data1);
			return {
				bvid: [""+data1.time.substring(0,10), ""+data1.bvid],
				title: [""+data1.time.substring(0,10), ""+data1.title],
				time: ""+data1.time,
				view: [""+data1.time.substring(0,10), +data1.view],
				favorite: [""+data1.time.substring(0,10), +data1.favorite],
				coin: [""+data1.time.substring(0,10), +data1.coin],
				share: [""+data1.time.substring(0,10), +data1.share],
				//cloudWord: [""+data1.title,""+data1.type]
			};
		}).then(function(data){
			require('echarts-wordcloud');
			//console.log(data);
			var viewData=[];
			var favoriteData=[];
			var coinData=[];
			var shareData=[];
			var bvidData=[];
			var titleData=[];
			//var cloudData=[];
			//var theData = [["2020-03-10", 8851508], ["2019-12-08", 6589367], ["2020-03-02", 802968]];
			for(var i=0;i<data.length;i++){
				viewData.push(data[i].view);
				favoriteData.push(data[i].favorite);
				coinData.push(data[i].coin);
				shareData.push(data[i].share);
				bvidData.push(data[i].bvid);
				titleData.push(data[i].title);
				//cloudData.push(data[i].cloudWord);
				//theData.time = data[i].time.substring(0, 9);
			}
			//console.log(cloudData)
			//console.log("view"+viewData);
			/*console.log("favorite"+favoriteData);
			console.log("coin"+coinData);
			console.log("share"+shareData);*/
			//var allData=[viewData,favoriteData,coinData,shareData];
			let myChart = echarts.init(document.getElementById('myChart'))
			var option2 = {
				legend: {
					data:['播放量', '点赞量', '投币量', '分享量'],
					selected:{'播放量':true,'点赞量':true,'投币量':true,'分享量':true}
				},
				tooltip: {
					show: true,
					trigger: 'axis',
					formatter(params){
						console.log(params);
						var result="";
						for(var i=4;i<params.length;i++){
							result+= params[i].seriesName+"： "+params[i].value[1]+'<br/>';
						}
						for(i=0;i<params.length-2;i++){
							result+= params[i].seriesName+"： "+params[i].value[1]+'<br/>';
						}

						return result;
					}
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
					splitNumber: 10,
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
					/*min: function(value){
						return value.min-30000;
					},*/
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
				},
				{
					name: '视频号',
					type: 'line',
					data: bvidData,
				},
				{
					name: '标题',
					type: 'line',
					data: titleData,
				}]
			};
			myChart.setOption(option2,true);
		});


	},
	SetCloud(){
		d3.dsv(",","word_data_new.csv",function(data){
			return {
				
				mid: ""+data.mid,
				words: ""+data.words,
			};
		}).then(function(data){
			//console.log(data[0].words);
			require('echarts-wordcloud');
			var str = data[0].words.split(",");
			//console.log(str);
			str[0] = str[0].substring(1,str[0].length)
			str[str.length-1] = str[str.length-1].substring(0, str[str.length-1]-1);
			var upWord=[]
			for(var i=0;i<str.length;i++){
				var array = str[i].replace("\"","");
				array = array.replace(':', ',');
				console.log(array.split(','));
				upWord.push(array.split(','));
			}
			console.log(upWord[0][0].replace("'","").replace("'",""),upWord[0][1]);

			var cloudData=[str.length-1];
			for(i=0;i<str.length-1;i++){
				var t={
					name: String,
					value: Number
				}
				t.name=upWord[i][0];
				t.name = t.name.replace("'","").replace("'","")
				t.value = Number(upWord[i][1])*100;
				console.log(t);
				cloudData.push(t);
			}
			console.log(cloudData);
			let wordCloud = echarts.init(document.getElementById('cloudChart'))
			
			var option = {
				series: [
					{
						type: "wordCloud",
						gridSize: 10,
						sizeRange: [14, 60],
						rotationRange: [0, 0],
						//maskImage: maskImage,
						textStyle: {
							normal: {
								color: function() {
									return (
										"rgb(" + Math.round(Math.random()*255) + ", " +
										Math.round(Math.random() * 255) + ", " + Math.round(Math.random() * 255) + ")"
									);
								}
							}
						},
						left: "center",
						width: "150%",
						height: "100%",
						data: cloudData
					}
				]
			}
			wordCloud.setOption(option);
		})
	}
    
  }
}

</script>

<style>
#myChart {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  text-align: center;
  left:10px;
}
#cloudChart{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  text-align: center;
  left:100px;	
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
