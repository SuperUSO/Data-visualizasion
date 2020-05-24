<template>
  <div id="app">
    <!--div id="nav"-->
      <!--router-link to="/">Index</router-link> |
      <router-link to="/chartx">About</router-link--> 
    <!--/div-->
    <router-view/>	

	<!--el-breadcrumb separator-class="el-icon-arrow-right">
		<el-breadcrumb-item : to="{path: '/'}">首页</el-breadcrumb-item>
		<el-breadcrumb-item >活动管理</el-breadcrumb-item>
	</el-breadcrumb-->
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.el-scrollbar_wrap{
	overflow-x: hidden;
}
</style>
