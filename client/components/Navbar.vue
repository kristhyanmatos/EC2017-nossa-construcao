<template>
  <div id="navbar">
    <b-avatar
      src="https://www.unifesspa.edu.br/images/manuais/Marca_UNIFESSPA/2019/Marca-Vertical-Smbolo-Tipografia-002.png"
      size="3rem"
      to="/"
    />
    <b-navbar-nav>
      <b-nav-item href="https://unifesspa.edu.br/" target="_blank">
        UNIFESSPA
      </b-nav-item>
    </b-navbar-nav>
    <b-navbar-nav>
      <b-nav-item href="https://faceel.unifesspa.edu.br/" target="_blank">
        FACEEL
      </b-nav-item>
    </b-navbar-nav>
    <b-navbar-nav>
      <b-nav-item href="https://www.instagram.com/_kristhyan/" target="_blank">
        KRISTHYAN
      </b-nav-item>
    </b-navbar-nav>
    <b-navbar-nav>
      <b-nav-item
        href="https://www.instagram.com/mikael_almondes/"
        target="_blank"
      >
        MIKAEL ALMONDES
      </b-nav-item>
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

  background: rgb(160, 70, 85);

  *:focus {
    outline: none !important;
  }
}
.navbar-nav .nav-link {
  font-weight: bold;
  color: white;
  margin-left: 20px;
}
</style>
