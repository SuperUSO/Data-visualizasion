<template>
  <div class="barStackChart">
    <div id="barStackChart" :style="{width: '380px', height: '710px'}"></div>
  </div>
</template>

<style>
</style>

<script>
export default {
  name: "BarStackChart",
  props:['rawDataProp'],
  data() {
    return {
      upId: [],
      follows: [],
      likes: [],
      view: [],
      name: [],
      rawData: [],
      map: new Map()
    };
  },
  mounted() {
    this.loadData()
      .then(this.processData)
      .then(this.draw);
  },
  methods: {
    loadData() {
      return this.$props.rawDataProp.then(d => {
        this.rawData = d;
      });
    },
    processData() {
      let data = this.rawData
      // console.log(data);
      let idx = 0;
      for (let item of data) {
        this.upId.push(item.mid);
        this.follows.push(item.follower);
        this.view.push(item.view);
        this.likes.push(item.likes);
        this.name.push(item.name);
        this.map.set(item.name, item.mid)
      }
    },
    draw() {
      let option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        legend: {
          data: ["关注人数", "点赞"]
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true
        },
        xAxis: {
          type: "value"
        },
        yAxis: {
          type: "category",
          data: this.name
        },
        dataZoom: [{
          yAxisIndex: [0],
          show: true,
          realtime: true,
          start: 100,
          end: 60
        },
        {
					type: 'slider',
					show: true,
					xAxisIndex: [0],
					start: 0, 
					end: 70
				}],
        series: [
          {
            name: "关注人数",
            type: "bar",
            stack: "总量",
            label: {
              show: false,
              position: "insideRight"
            },
            data: this.follows
          },
        //   {
        //     name: "观看数",
        //     type: "bar",
        //     stack: "总量",
        //     label: {
        //       show: true,
        //       position: "insideRight"
        //     },
        //     data: this.view
        //   },
          {
            name: "点赞",
            type: "bar",
            stack: "总量",
            label: {
              show: false,
              position: "insideRight"
            },
            data: this.likes
          },
        ]
      };
        let myChart = this.$echarts.init(document.getElementById('barStackChart'))
        myChart.setOption(option)
        
        myChart.on('click', params => {
        console.log(this.map)  
            this.$emit('selectUp', this.map.get(params.name))
            console.log(this.map.get(params.name))
        })
    }
  }
};
</script>