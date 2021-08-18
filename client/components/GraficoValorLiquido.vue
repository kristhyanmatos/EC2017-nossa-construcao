<template>
  <div id="componente_grafico_valor_liquido">
    <div class="row">
      <div class="col text-center">
        <h1>
          <strong>Comparativo entre Valores Previstos e Liquidados</strong>
        </h1>
        <p>
          Analise comparativa entre os valores das licitações previstos e o
          valor liquidado ao final da obra, levando em consideração valores não
          previstos no projeto inicialmente
        </p>
      </div>
    </div>
    <Apexchart
      id="grafico_valor_liquido"
      :series="series"
      type="line"
      :options="chartOptions"
      height="700"
    />
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
          width: 'straight',
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
            formatter(val) {
              return val + '%'
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
            formatter(val) {
              return val !== undefined
                ? 'R$ ' +
                    val.toString().toLocaleString('pt-br', {
                      style: 'currency',
                      currency: 'BRL',
                    })
                : val
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

<style lang="scss">
#componente_grafico_valor_liquido {
  margin-top: 20vh;
  width: 97vw;
}
#grafico_valor_liquido {
  width: 96vw;
}
</style>
