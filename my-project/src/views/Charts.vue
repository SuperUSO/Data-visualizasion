<template>
	<div>
		<h1>This is a test</h1>
		<div id="myChart" style="width: 600px;height: 400px;"></div>
	</div>
	
</template>

<script>
//import echarts from 'echarts'
import * as d3 from 'd3'
export default {
  name: 'echart',
  mounted(){
    this.SetEchart();
	this.GetDataD3();
  },
  data () {
    return {
      msg: 'Welcome'
    }
  },
  methods: {
	GetDataD3(){
		//var csvdata;
		d3.csv("up_data.csv",function(error, csvdata){
			if(error){
				console.log(error);
			}
			console.log(csvdata);
		})
		//var name,sex,age
		/*for(var i=0;i<csvdata.length;i++){
			var view = csvdata[i].view;
			var likes = csvdata[i].likes;
			var mid = csvdata[i].mid;
			var flowers = csvdata[i].flowers;
			console.log("view:"+view+"\n"+
						"likes:"+likes+"\n"+
						"mid:"+mid+"\n"+
						"flowers:"+flowers+"\n");
		}*/
	},
    SetEchart(){
        // 基于准备好的dom，初始化echarts实例
        let myChart = this.$echarts.init(document.getElementById('myChart'))
        // 绘制图表
		var option = {
			title: {
				text: '郑州月最低生活费组成（单位:元）',    
			},
			tooltip : {
				trigger: 'axis',
				axisPointer : {            // 坐标轴指示器，坐标轴触发有效
					type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
				},
			formatter: function (params) {
				var tar = params[1];
				return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value;
			}
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis: {
			type : 'category',
			splitLine: {show:false},
			data : ['总费用','房租','水电费','交通费','伙食费','日用品数']
		},
		yAxis: {
			type : 'value'
		},
		series: [
			{
				name: '辅助',
				type: 'bar',
				stack:  '总量',
				itemStyle: {
					normal: {
						barBorderColor: 'rgba(0,0,0,0)',
						color: 'rgba(0,0,0,0)'
					},
					emphasis: {
						barBorderColor: 'rgba(0,0,0,0)',
						color: 'rgba(0,0,0,0)'
					}
				},
				data: [0, 1700, 1400, 1200, 300, 0]
			},
			{
				name: '生活费',
				type: 'bar',
				stack: '总量',
				label: {
					normal: {
						show: true,
						position: 'inside'
					}
				},
				data:[3900, 2200, 300, 200, 900, 300]
			}
		]
	};
	myChart.setOption(option);
    }
  }
}

</script>

<style>
#myChart {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
}
</style>
