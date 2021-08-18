<template>
  <div class="card_index">
    <p id="construcao_todos_texto">
      10 construções com maiores gastos líquidos.
    </p>
    <b-table striped hover :items="dados.slice(0, 10)" :fields="fields" />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'MaiorGasto',
  data() {
    return {
      fields: ['codigo', 'nome', 'inicio', 'fim', 'liquido'],
      dados: [],
    }
  },
  async mounted() {
    await this.buscaDadosApi()
    this.ordenaMaiorGasto()
  },
  methods: {
    async buscaDadosApi() {
      await this.$api
        .get('/nossas-construcoes')
        .then((response) => {
          this.dados = response.data
        })
        .catch((error) => console.log(error))
    },
    ordenaMaiorGasto() {
      this.dados.sort(function (a, b) {
        return (
          Number(b.liquido.replace('.', '').replace(',', '.')) -
          Number(a.liquido.replace('.', '').replace(',', '.'))
        )
      })
      this.dados.slice(0, 10).forEach((element) => {
        element.liquido = `R$ ${element.liquido}`
      })
    },
    formataDataNorteAmericana(data) {
      const dia = data.inicio.substring(2, 0)
      const mes = data.inicio.substring(5, 3)
      const ano = data.inicio.substring(10, 6)
      return ano + '-' + mes + '-' + dia
    },
    parseMillisecondsIntoReadableTime(milliseconds) {
      const hours = milliseconds / (1000 * 60 * 60)
      const absoluteHours = Math.floor(hours)
      const h = absoluteHours > 9 ? absoluteHours : '0' + absoluteHours

      const minutes = (hours - absoluteHours) * 60
      const absoluteMinutes = Math.floor(minutes)
      const m = absoluteMinutes > 9 ? absoluteMinutes : '0' + absoluteMinutes

      const seconds = (minutes - absoluteMinutes) * 60
      const absoluteSeconds = Math.floor(seconds)
      const s = absoluteSeconds > 9 ? absoluteSeconds : '0' + absoluteSeconds

      return h + 'h:' + m + 'm:' + s + 's'
    },
  },
})
</script>

<style lang="scss">
.card_index {
  margin-top: 150px;
  width: 78vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
