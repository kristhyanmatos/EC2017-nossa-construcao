<template>
  <div id="app">
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
        Analise comparativa entre os valores das licitações previstos e o valor
        liquidado ao final da obra, levando em consideração valores não
        previstos no projeto inicialmente
      </b-card-text>
    </b-card>
    <div class="row">
      <div class="col text-center">
        <h3>Gráfico Comparativo entre valores previstos e liquidados</h3>
      </div>
    </div>
    <GraficoValorLiquido />
    <Rodape />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({})
</script>

<style lang="scss">
#app {
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#cardIndex {
  width: 98vw;
  align-self: center;
}
</style>
