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
  async mounted() {},
})
</script>

<style lang="scss"></style>
