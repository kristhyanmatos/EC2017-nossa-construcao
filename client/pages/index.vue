<template>
  <div id="app">
    <Navbar />
    <b-row>
      <b-col align-self="center" xl="11">
        <b-card
          id="cardIndex"
          overlay
          img-src="https://picsum.photos/900/250/?image=3"
          img-alt="Card Image"
          text-variant="white"
          title="Transparência de valores"
          sub-title="Construção civil"
        >
          <b-card-text>
            Analise comparativa entre os valores das licitações previstos e o
            valor liquidado ao final da obra, levando em consideração valores
            não previstos no projeto inicialmente
          </b-card-text>
        </b-card>
      </b-col>
    </b-row>
    <div class="row">
      <div class="col text-center">
        <h1>Gráfico Comparativo entre valores previstos e liquidados</h1>
      </div>
    </div>
    <GraficoValorLiquido />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({})
</script>

<style lang="scss">
#app {
  justify-content: center;
}
#cardIndex {
  margin-top: 70px;
  width: 99%;
  align-self: center;
}
</style>
