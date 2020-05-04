<template>
  <div>
    <div id="mainChart" :style="{width: '450px', height: '420px'}"></div>
  </div>
</template>

<style>
#mainChart{
  padding-left: 30px;
  padding-top: 20px;
}
</style>

<script>
export default {
  name: "MainChart",
  props: ["rawDataProp"],
  data() {
    return {
      rawData: {},
      data: [],
      colors: [
        "#d87c7c",
        "#919e8b",
        "#d7ab82",
        "#6e7074",
        "#61a0a8",
        "#efa18d",
        "#787464",
        "#cc7e63",
        "#724e58",
        "#4b565b",
        "#9A2555"
      ],
      levels: ['1☆','2☆','3☆']
    };
  },
  mounted() {
    // this.draw();
    this.loadData()
      .then(this.processData)
      .then(this.draw);
  },
  watch: {
    // upId() {
    //   this.processData();
    //   this.draw();
    // }
  },
  methods: {
    loadData() {
      return this.$props.rawDataProp.then(d => {
        this.rawData = d;
      });
    },
    processData() {
      //   console.log(this.rawData);
      let groupByTypeObj = this.rawData.reduce((acc, item, idx) => {
        let result = acc[item.type] || {
          name: item.type.slice(0, item.type.length-1),
          children: [],
          itemStyle: {
            color: this.colors[idx]
          },
                
        };
        result.children.push({
          name: item.name,
          upId: item.mid,
          value: 1,
          emphasis: {
              itemStyle: {
                  color: 'red',
              },
          },
          count: item.work_sum
        });
        acc[item.type] = result;
        return acc;
      }, {});
      let groupByTypeArr = Object.keys(groupByTypeObj).map(
        x => groupByTypeObj[x]
      );
      let sortby = [5,0,4,10,9,2,3,8,1,7,6];
      let shuffled = groupByTypeArr
        .map((a,idx) => ({sort: sortby[idx], value: a}))
        .sort((a, b) => a.sort - b.sort)
        .map((a) => a.value)

      // console.log(shuffled);

      let groupByCntArr = [];

      for(let item of shuffled){
        let cntArr = item.children.map(x => parseInt(x.count));
        let curObj = {
          name: item.name,
          children: []
        }
        // if(cntArr.length < 3){
        //   curObj.children.push({
        //     name: this.levels[2],
        //     children: item.children
        //   });
        // }
        // else{
          curObj.children = [
            {
              name: this.levels[0],
              children: [],
            },
            {
              name: this.levels[1],
              children: [],
            },
            {
              name: this.levels[2],
              children: [],
            }
          ]
          let maxCnt = Math.max(...cntArr), minCnt = Math.min(...cntArr);
          let interval = (maxCnt - minCnt) / 3;
          let intervalArr = [minCnt+interval, maxCnt-interval];
          for(let x of item.children){
            let xCnt = x.count;
            if(xCnt<intervalArr[0]){
              curObj.children[0].children.push(x);
            }
            else if(xCnt<intervalArr[1]){
              curObj.children[1].children.push(x);
            }
            else{
              curObj.children[2].children.push(x);
            }
          }
        // }
        groupByCntArr.push(curObj);

      }
      // console.log(groupByCntArr)
      
      this.data = groupByCntArr;
    },
    draw() {
      //   var itemStyle = {
      //     star5: {
      //       color: colors[0]
      //     },
      //     star4: {
      //       color: colors[1]
      //     },
      //     star3: {
      //       color: colors[2]
      //     },
      //     star2: {
      //       color: colors[3]
      //     }
      //   };

      let data = this.data;
      console.log(data)

      for (var j = 0; j < data.length; ++j) {
        var level1 = data[j].children;
        for (var i = 0; i < level1.length; ++i) {
          var block = level1[i].children;
          var bookScore = [];
          var bookScoreId;
          //   for (var star = 0; star < block.length; ++star) {
          //     var style = (function(name) {
          //       switch (name) {
          //         case "5☆":
          //           bookScoreId = 0;
          //           return itemStyle.star5;
          //         case "4☆":
          //           bookScoreId = 1;
          //           return itemStyle.star4;
          //         case "3☆":
          //           bookScoreId = 2;
          //           return itemStyle.star3;
          //         case "2☆":
          //           bookScoreId = 3;
          //           return itemStyle.star2;
          //       }
          //     })(block[star].name);

          //     block[star].label = {
          //       color: style.color,
          //       downplay: {
          //         opacity: 0.5
          //       }
          //     };

          //     if (block[star].children) {
          //       style = {
          //         opacity: 1,
          //         color: style.color
          //       };
          //       block[star].children.forEach(function(book) {
          //         book.value = 1;
          //         book.itemStyle = style;

          //         book.label = {
          //           color: style.color
          //         };

          //         var value = 1;
          //         if (bookScoreId === 0 || bookScoreId === 3) {
          //           value = 5;
          //         }

          //         if (bookScore[bookScoreId]) {
          //           bookScore[bookScoreId].value += value;
          //         } else {
          //           bookScore[bookScoreId] = {
          //             color: colors[bookScoreId],
          //             value: value
          //           };
          //         }
          //       });
          //     }
          //   }

          // level1[i].itemStyle = {
          //   color: data[j].itemStyle.color
          // };
        }
      }

      let option = {
        color: this.colors,
        series: [
          {
            type: "sunburst",
            data: data,
            sort: function(a, b) {
              // return a.dataIndex - b.dataIndex;
              // if (a.depth === 1) {
              //   return b.getValue() - a.getValue();
              // } else {
              //   return a.dataIndex - b.dataIndex;
              // }
            },
            label: {
              rotate: "radial",
              color: "black"
            },
            itemStyle: {
              borderColor: "white",
              borderWidth: 1
            },
            levels: [
              {},
              {
                r0: 20,
                r: 130,
                label: {
                  rotate: 0
                }
              },
              //   {
              //     r0: 40,
              //     r: 105
              //   },
                {
                  r0: 115,
                  r: 140,
                  itemStyle: {
                    // shadowColor: colors[2],
                    color: "transparent"
                  },
                  label: {
                    rotate: "tangential",
                    fontSize: 10,
                    // color: colors[0]
                  }
                },
              {
                r0: 145,
                r: 155,
                itemStyle: {
                  // shadowBlur: 80,
                  shadowColor: this.colors[0]
                },
                label: {
                  position: "outside",
                  // textShadowBlur: 5,
                  textShadowColor: "#333",
                  fontSize:9
                },
                downplay: {
                  label: {
                    opacity: 0.5
                  }
                }
              }
            ]
          }
        ]
      };

      console.log("click---");
      let myChart = this.$echarts.init(document.getElementById("mainChart"));
      myChart.setOption(option);
        myChart.on("click", params => {
          // console.log(params);
          if(params.data.upId != undefined){
            this.$emit('selectUp', params.data.upId)
          }
        });
      console.log("end");
    }
  }
};
</script>