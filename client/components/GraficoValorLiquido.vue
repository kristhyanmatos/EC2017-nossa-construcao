<template>
  <div id="grafico_valor_liquido">
    <b-row>
      <b-col align-self="center">
        <Apexchart
          :series="series"
          type="line"
          :options="chartOptions"
          width="90%"
          height="750"
        />
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Vue from 'vue'

import VueApexCharts from 'vue-apexcharts'

Vue.use(VueApexCharts)
Vue.component('Apexchart', VueApexCharts)
export default Vue.extend({
  name: 'GraficoValorLiquido',
  data() {
    return {
      series: [
        {
          name: 'Valor Real',
          data: [],
        },
        { name: 'Valor Líquidado', data: [] },
      ],
      chartOptions: {
        dataLabels: {
          enabled: false,
        },
        colors: ['#FF1654', '#247BA0'],
        stroke: {
          width: [4, 4],
        },
        plotOptions: {
          bar: {
            columnWidth: '20%',
          },
        },
        xaxis: {
          categories: [],
        },
        yaxis: {
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          labels: {
            show: true,
            type: 'number',
            formatter(val) {
              return val !== undefined ? val.toFixed(3) : val
            },
          },
        },
        legend: {
          horizontalAlign: 'left',
          offsetX: 40,
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
        .then((response) => {
          const valores = response.data.map((construcao) => construcao.valor)
          const liquidados = response.data.map(
            (construcao) => construcao.liquido
          )
          const anos = response.data.map((construcao) => construcao.fim)
          this.series = [
            { name: 'Valor Real', data: valores },
            { name: 'Valor Liquidado', data: liquidados },
          ]
          this.chartOptions = this.setChartOptions(anos)
          console.log(anos)
        })
        .catch((error) => console.log(error))
    },
    setChartOptions(datas) {
      return {
        dataLabels: {
          enabled: false,
        },
        colors: ['#FF1654', '#247BA0'],
        stroke: {
          width: [4, 4],
        },
        plotOptions: {
          bar: {
            columnWidth: '20%',
          },
        },
        xaxis: {
          categories: datas,
        },
        yaxis: {
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          labels: {
            show: true,
            type: 'number',
            formatter(val) {
              return val !== undefined ? val.toFixed(3) : val
            },
          },
        },
        legend: {
          horizontalAlign: 'left',
          offsetX: 40,
        },
      }
    },
  },
})
</script>

<style lang="scss"></style>
