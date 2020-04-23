<template>
  <div id="app">
    <!--img alt="Vue logo" src="./assets/logo.png"-->
	<el-header>
		<TheTitle msg="B站百大UP主可视化分析"/>
	</el-header>
   
	<el-container>
		<el-aside>
			<el-image style="width: 18.75rem; height: 33.125;rem" :src="require('@/assets/花花与三猫_终.png')"></el-image>
		</el-aside>
		<el-aside>
			<el-image class="img" :src="require('@/assets/cJun.jpg')"></el-image>
		</el-aside>
		<el-aside>
			<el-image class="img" :src="require('@/assets/cJun.jpg')"></el-image>
		</el-aside>
		<el-aside>
			<el-image class="img" :src="require('@/assets/cJun.jpg')"></el-image>
		</el-aside>
		<el-aside>
			<el-image class="img" :src="require('@/assets/cJun.jpg')"></el-image>
		</el-aside>
	</el-container>
	<el-footer>
		next
	</el-footer>
	
	
  </div>
</template>

<script>
import TheTitle from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    TheTitle
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
  margin-top: 60px;
  
}
.img{
	height:33.125rem;
	width:18.75rem;
}
</style>
