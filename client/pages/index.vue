<template>
  <div id="app">
    <div class="row">
      <div class="col text-center">
        <h1>Olá Haroldo</h1>
      </div>
    </div>
    <Apexchart :series="series" type="line" :options="chartOptions" />
  </div>
</template>

<script>
import Vue from 'vue'

import VueApexCharts from 'vue-apexcharts'

Vue.use(VueApexCharts)
Vue.component('Apexchart', VueApexCharts)
export default Vue.extend({
  name: 'App',
  components: {},
  data() {
    return {
      series: [
        {
          name: 'Valor',
          data: [],
        },
      ],
      chartOptions: {
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: 'straight',
        },
        title: {
          text: 'Nossas Construções',
          align: 'left',
        },
      },
    }
  },
  async mounted() {
    await this.buscaDadosApi()
  },
  methods: {
    async buscaDadosApi() {
      await this.$api
        .get('/nossas-construcoes')
        .then(
          (response) =>
            (this.series[0].data = response.data.map(
              (construcao) => construcao.valor
            ))
        )
        .catch((error) => console.log(error))
    },
  },
})
</script>

<style lang="scss"></style>
