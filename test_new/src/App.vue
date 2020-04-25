<template>
  <div id="app">
    <!--img alt="Vue logo" src="./assets/logo.png"-->
	<!--el-header>
		<TheTitle msg="B站百大UP主可视化分析"/>
	</el-header-->
	<!--el-header style="font-size: larger;">B站百大UP主可视化分析</el-header-->
	<!--div class="Title">B站百大UP主可视化分析</div-->
	<!--table><tr>
	<td><img  src="./assets/花花与三猫_终.png"/></td>
	<td><img  src="./assets/咬人猫_终.png"/></td>
	<td><img  src="./assets/花花与三猫_终.png"/></td>
	<td><img  src="./assets/花花与三猫_终.png"/></td>
	<td><img  src="./assets/花花与三猫_终.png"/></td>
	</tr></table-->
	<!--div class="img">
		<img  src="./assets/花花与三猫_终.png" height="100%"/>
	</div>
	<div class="img">
		<img  src="./assets/花花与三猫_终.png" height="100%"/>
	</div>
	<div class ="img" background="./assets/花花与三猫_终.png" style=" background-repeat:no-repeat ;
			background-size:100% 100%;background-attachment: fixed;"></div-->
   
	<!--el-container>
		<el-aside>
			<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
		</el-aside>
		<el-aside>
			<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
		</el-aside>
		<el-aside>
			<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
		</el-aside>
		<el-aside>
			<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
		</el-aside>
		<el-aside>
			<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
		</el-aside>
	</el-container-->
	<!--div class="block">
		<span class="demonstration">默认Hover指示器触发</span>
		<el-carousel height="500px">
			<el-carousel-item v-for="item in 4" :key="item">
				<h3 class="small">{{item}}</h3>
			</el-carousel-item>
		</el-carousel>
	</div-->
	<!--div class="block">
		<span class="demonstration">默认Hover指示器触发</span>
		<el-carousel height="500px">
			<el-carousel-item v-for="imgSrc in imgSrc()" :key="imgSrc">
				<h3 class="small">{{imgSrc}}</h3>
			</el-carousel-item>
		</el-carousel>
	</div-->
	<div class="block">
		<span class="demonstration">默认Hover指示器触发</span>
		<el-carousel height="600px">
			<el-carousel-item>
				<el-container>
					<el-aside>
						<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
					</el-aside>
					<el-aside>
						<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/咬人猫_终.png')"></el-image>
					</el-aside>
					<el-aside>
						<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
					</el-aside>
					<el-aside>
						<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
					</el-aside>
					<el-aside>
						<el-image style="width: 18.75rem; height: 98%" :src="require('@/assets/花花与三猫_终.png')"></el-image>
					</el-aside>
				</el-container>
			</el-carousel-item>
			<el-carousel-item>
				<el-container>
					<el-image style="width: 100% height:80%;" :fit="fit" :src="require('@/assets/index.png')"></el-image>
				</el-container>
			</el-carousel-item>
			<el-carousel-item>
				<h3 class="small">3</h3>
			</el-carousel-item>
		</el-carousel>
	</div>
	<!--div class="demo-image">
		<div class="block" v-for="fit in fits" :key="fit">
			<span class="demonstration">{{fit}}</span>
			<el-image style="width: 100px;height: 100px;" :src="url" :fit="fit"></el-image>
		</div>
	</div-->
	<el-footer>
		<el-link href="./charts.vue" target="_blank">next</el-link>
	</el-footer>
	
	
  </div>
</template>

<script>
//import TheTitle from './components/HelloWorld.vue'

export default {
	data() {
      return {
        fits: ['fill', 'contain', 'cover', 'none', 'scale-down'],
        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
		//imgSrcs:require('@/assets/花花与三猫_终.png'),
      }
    },
  name: 'App',
  components: {
  //  TheTitle
  },
  /*data(){
	  return{
		  imgSrc:["require('@/assets/花花与三猫_终.png')","require('@/assets/花花与三猫_终.png')"]
	  }
  }*/
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  margin-top: 10px;
  
}
.img{
	height:100%;
	width:17%;
}
.Title{
	width: 100%;
	font-size: 3em;
}
</style>
