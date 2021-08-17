<template>
  <div id="navbar">
    <b-avatar src="../assets/kmlogo.svg" size="3rem" to="/" />
    <b-navbar-nav>
      <b-nav-item to="/"> NOSSA CONSTRUÇÃO </b-nav-item>
    </b-navbar-nav>

    <b-navbar-nav id="item_nav_sobe_nos">
      <b-nav-item to="/sobre"> SOBRE NÓS </b-nav-item>
    </b-navbar-nav>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  methods: {},
})
</script>

<style lang="scss">
#navbar {
  position: fixed;
  z-index: 99;
  top: 0;
  left: 0;
  height: 60px;
  width: 100%;
  padding-left: 60px;

  display: flex;
  align-items: center;

  background: rgb(1, 131, 136);

  *:focus {
    outline: none !important;
  }
}
.navbar-nav .nav-link {
  font-weight: bold;
  color: white;
  margin-left: 20px;
}
#item_nav_sobe_nos {
  justify-self: flex-end !important;
}
</style>
