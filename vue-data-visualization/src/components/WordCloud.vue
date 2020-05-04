<template>
  <div>
    <div id="wordCloud" :style="{width: '400px', height: '600px'}"></div>
  </div>
</template>

<style>
</style>

<script>
import "echarts-wordcloud";
export default {
  name: "WordCloud",
  props:[],
  data() {
    return {
      upId: [],
      follows: [],
      likes: [],
      view: []
    };
  },
  mounted() {
    this.setCloud();
  },
  methods: {
    setCloud(){
        // let loadDsv = this.$d3.dsv(",","iso-8859-1")
		this.$d3.dsv(",","static/word_data_new.csv",function(data){
			return {
				
				mid: ""+data.mid,
				words: ""+data.words,
			};
		}).then((data) => {
			console.log(data[0].words);
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
			let wordCloud = this.$echarts.init(document.getElementById('wordCloud'))
			
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
};
</script>