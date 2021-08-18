<template>
  <div id="app">
    <div class="carrossel">
      <b-row align-h="center">
        <b-col xl="4">
          <p id="construcao_todos_texto">
            Dados de construções em Marabá-PA nos últimos 10 anos.
          </p>
        </b-col>
        <b-col xl="7">
          <img
            id="imagem_um"
            class="login-image"
            src="../assets/construcao_um.svg"
          />
        </b-col>
      </b-row>
    </div>
    <GraficoValorLiquido />
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

    <TabelaConstrucoesMaisRapidas />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({})
</script>

<style lang="scss">
#imagem_um {
  width: 30vw;
}
.carrossel {
  margin-top: 10vh;
  width: 70vw;
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
  font-size: 40px;
  color: rgb(0, 0, 0);
  font-weight: bold;
}
#container_dois_index_verde {
  margin-top: 10vh;
  margin-bottom: 40vh;
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
