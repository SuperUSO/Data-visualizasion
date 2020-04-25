<template>
  <div id="app">
    <!--img alt="Vue logo" src="./assets/logo.png"-->
	<!--el-header>
		<TheTitle msg="B站百大UP主可视化分析"/>
	</el-header-->
	<!--el-header style="font-size: larger;">B站百大UP主可视化分析</el-header-->
	<div class="Title">B站百大UP主可视化分析</div>
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
	<div class="block">
		<span class="demonstration">默认Hover指示器触发</span>
		<el-carousel height="600px">
			<el-carousel-item>
				<el-container>
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
				</el-container>
			</el-carousel-item>
			<el-carousel-item>
				<h3 class="small">2</h3>
			</el-carousel-item>
			<el-carousel-item>
				<h3 class="small">3</h3>
			</el-carousel-item>
			<el-carousel-item>
				<h3 class="small">4</h3>
			</el-carousel-item>
		</el-carousel>
	</div>
	<el-footer>
		next
	</el-footer>
	
	
  </div>
</template>

<script>
//import TheTitle from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
  //  TheTitle
  }
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
