<template>
<div>
    <div class="container">
        <div id="map" :style="{width: '700px', height: '700px'}"></div>
    </div>
</div>
</template>

<style>
/**
 * The default size is 600px×400px, for responsive charts
 * you may need to set percentage values as follows (also
 * don't forget to provide a size for the container).
 */
.echarts {
  width: 600px;
  height: 400px;
}
</style>

<script>
// import geojsonRaw from '../assets/province_geo.json'

export default {
    name: "Map",
    components: {
        
    },
    data () {
        return{
            // geojsonRaw: geojsonRaw,
            geojson: [],
            provTotal: []
        }
    },
    mounted(){
        // this.loadData()
        this.loadData().then(this.drawMap);
    },
    methods:{
        loadData(){
            // this.$papa.parse('../assets/province_confirmed_total.csv',{
            //     complete: function(results){
            //         this.provTotal = results;
            //         console.log(results)
            //     }
            // })
            // this.provTotal = this.$d3.csv('../assets/province_confirmed_total.csv');
            // console.log(this.provTotal)
            // console.log(this.geojsonRaw.features[0])

            // this.geojson = this.geojsonRaw.features.map(x => {
            //     return {
            //         name: x.properties.name,
            //         coords: x.properties.cp
            // }})
            // console.log(this.geojson)
            // this.$d3.json('../assets/province_geo.json').then(data => {
            //     console.log(data)
            // })
            // this.$d3.csv('../assets/province_confirmed_total.csv').then(data => {
            //     console.log(data)
            // })

            // return Promise.all([
            //     this.$d3.csv('../assets/province_confirmed_total.csv'),
            //     // this.$d3.json('../assets/province_geo.json'),
            // ]).then(datasets => {
            //     this.provTotal = datasets[0];
            //     // this.geojson = datasets[1];
            // })

            // this.$axios.get('../../static/province_confirmed_total.csv')
            //     .then((res)=>{
            //         console.log(res)
            //     })

            return this.$axios.all([
                this.$axios.get('../../static/province_confirmed_total.csv'),
                this.$axios.get('../../static/province_geo.json')
            ]).then(this.$axios.spread((...responses)=>{
                // console.log(responses[0])
                // console.log(responses[1])
                let temp = responses[0].data.split('\n')
                this.provTotal = temp.slice(1).map((item) => {
                    let x = item.split(',');
                    return {
                        name: x[0],
                        confirmedCount: x[1]
                    }
                })
                console.log(this.provTotal)
                
                this.geojson = responses[1].data.features.map(x => {
                    return {
                        name: x.properties.name,
                        coords: x.properties.cp
                }})
                console.log(this.geojson)
                return [this.provTotal, this.geojson]
            }))
        },
        drawMap(){
            console.log(this.provTotal);
            console.log(this.geojson);
            
        }
    }
}
</script>