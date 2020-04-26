<template>
  <div>
    <div class="lineAndBarChart">
      <div id="lineAndBarChart" :style="{width: '1000px', height: '400px'}"></div>
    </div>
    <div class="pieChart">
      <div id="pieChart" :style="{width: '500px', height: '500px'}"></div>
    </div>
  </div>
</template>

<style>
</style>

<script>
import "echarts/lib/chart/line";
import "echarts/lib/chart/pie";

export default {
  name: "PopularityLineAndBarChart",
  data() {
    return {
      upid: "38351330",
      videos: [],
      popularityList: [], //line chart
      lengthSecondsList: [], //bar chart
      timeList: [], //xaxis
      types: [],
      typeAndValue: []
    };
  },
  mounted() {
    this.loadData()
      .then(this.processData)
      .then(this.draw);
  },
  methods: {
    loadData() {
      return this.$d3.csv("static/video_data.csv");
    },
    processData(data) {
      // console.log(data)
      data = data.filter(video => video.owner === this.upid);
      this.videos = data
        .map(video => {
          let lengthSecondsArr = video.length.split(":");
          let x60 = (lengthSecondsArr.length - 1) * 60;
          let lengthSeconds = 0;
          for (let time of lengthSecondsArr) {
            lengthSeconds += parseInt(time) * x60;
            x60 /= 60;
          }
          let popularity =
            parseInt(video.view) * 0.2 +
            parseInt(video.favorite) * 0.2 +
            parseInt(video.share) * 0.3 +
            parseInt(video.coin) * 0.3;

          return {
            bvid: video.bvid,
            // coin: parseInt(video.coin),
            // favorite: parseInt(video.favorite),
            // share: parseInt(video.share),
            // view: parseInt(video.view),
            popularity: popularity.toFixed(1),
            length: video.length,
            lengthSeconds: lengthSeconds,
            title: video.title,
            type_name: video.type_name,
            time: new Date(video.time),
            timeFormatted: video.time.split(" ")[0]
          };
        })
        .sort((a, b) => a.time - b.time);

      for (let video of this.videos) {
        this.popularityList.push(video.popularity);
        this.lengthSecondsList.push(video.lengthSeconds);
        this.timeList.push(video.timeFormatted);
      }

      let typeAndValueTemp = data.reduce((acc, cur) => {
        let current = acc[cur.type_name] || {
          type: cur.type_name,
          value: 0
        };
        current.value += 1;
        acc[cur.type_name] = current;
        return acc;
      }, {});
      console.log(typeAndValueTemp);
      this.typeAndValue = Object.keys(typeAndValueTemp).map(x => {
        this.types.push(x);
        return {
          name: x,
          value: typeAndValueTemp[x].value
        };
      });
      console.log(this.types)
      console.log(this.typeAndValue);

      return this.videos;
    },
    draw(data) {
      let popilarityMax = Math.max(...this.popularityList);
      let lengthMax = Math.max(...this.lengthSecondsList);
      let option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            crossStyle: {
              color: "#999"
            }
          }
        },
        legend: {
          data: ["视频时长", "视频受欢迎程度"]
        },
        xAxis: [
          {
            type: "category",
            data: this.timeList,
            axisPointer: {
              type: "shadow"
            }
          }
        ],
        yAxis: [
          {
            type: "value",
            name: "视频受欢迎程度",
            min: 0,
            max: popilarityMax,
            interval: popilarityMax / 5,
            axisLabel: {
              formatter: "{value}"
            }
          },
          {
            type: "value",
            name: "视频时长",
            min: 0,
            max: lengthMax,
            interval: lengthMax / 5,
            axisLabel: {
              formatter: "{value} s"
            }
          }
        ],
        dataZoom: {
          show: true,
          realtime: true,
          start: 0,
          end: 50
        },
        calculable: false,
        series: [
          {
            name: "视频受欢迎程度",
            type: "line",
            data: this.popularityList
          },
          {
            name: "视频时长",
            type: "bar",
            yAxisIndex: 1,
            data: this.lengthSecondsList
          }
        ]
      };
      let myChart = this.$echarts.init(
        document.getElementById("lineAndBarChart")
      );
      myChart.setOption(option);

      //---------------------------------

      let pieOption = {
        title: {
          text: "视频分区统计",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: this.types
        },
        series: [
          {
            name: "视频分区",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: this.typeAndValue,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      };
      let myPieChart = this.$echarts.init(
        document.getElementById("pieChart")
      );
      myPieChart.setOption(pieOption);
    }
  }
};
</script>