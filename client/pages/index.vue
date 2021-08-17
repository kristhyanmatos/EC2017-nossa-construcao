<template>
  <div id="app">
    <div class="carrossel">
      <b-row>
        <b-col xl="9">
          <img class="login-image" src="../assets/construcao_um.svg" />
        </b-col>
        <b-col xl="3">
          <p id="construcao_todos_texto">A construção é de todos nós.</p>
        </b-col>
      </b-row>
    </div>

    <div id="container_dois_index_verde">
      <b-row>
        <b-col>
          <p id="construcao_futuro">
            Construindo o futuro e reformando o passado.
          </p>
        </b-col>
      </b-row>
      <img class="login-image" src="../assets/construcao_dois.svg" />
    </div>

    <GraficoValorLiquido />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({})
</script>

<style lang="scss">
.carrossel {
  margin-top: 10vh;
  width: 60vw;
}
#app {
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#cardIndex {
  align-self: center;
}
#construcao_todos_texto {
  font-size: 38px;
  color: rgb(0, 0, 0);
  font-weight: bold;
}
#container_dois_index_verde {
  margin-top: 10vh;
  height: 50vh;
  width: 97vw;
  background-color: rgb(0, 163, 168);
  display: flex;
  flex-direction: column;
  align-items: center;
}
#construcao_futuro {
  margin-top: 5vh;
  font-size: 38px;
  color: rgb(255, 255, 255);
  font-weight: bold;
}
</style>
