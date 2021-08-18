<template>
  <div class="card_index">
    <p id="construcao_todos_texto">
      10 construções com maiores tempos de duração.
    </p>
    <b-table striped hover :items="dados.slice(0, 10)" :fields="fields" />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'MaisDemorada',
  data() {
    return {
      fields: ['codigo', 'nome', 'inicio', 'fim', 'duracao'],
      dados: [],
    }
  },
  async mounted() {
    await this.buscaDadosApi()
    this.ordenaMaiorMenorTempoConstrucao()
    this.adicionaTempoDuracao()
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
    ordenaMaiorMenorTempoConstrucao() {
      this.dados.sort(function (a, b) {
        let dia = a.inicio.substring(2, 0)
        let mes = a.inicio.substring(5, 3)
        let ano = a.inicio.substring(10, 6)
        let data = ano + '-' + mes + '-' + dia
        const inicioA = new Date(data)

        dia = a.fim.substring(2, 0)
        mes = a.fim.substring(5, 3)
        ano = a.fim.substring(10, 6)
        data = ano + '-' + mes + '-' + dia
        const fimA = new Date(data)
        const duracaoA = fimA.getTime() - inicioA.getTime()

        dia = b.inicio.substring(2, 0)
        mes = b.inicio.substring(5, 3)
        ano = b.inicio.substring(10, 6)
        data = ano + '-' + mes + '-' + dia
        const inicioB = new Date(data)

        dia = b.fim.substring(2, 0)
        mes = b.fim.substring(5, 3)
        ano = b.fim.substring(10, 6)
        data = ano + '-' + mes + '-' + dia
        const fimB = new Date(data)
        const duracaoB = fimB.getTime() - inicioB.getTime()

        return duracaoB - duracaoA
      })
    },
    adicionaTempoDuracao() {
      this.dados.forEach((element) => {
        let dia = element.inicio.substring(2, 0)
        let mes = element.inicio.substring(5, 3)
        let ano = element.inicio.substring(10, 6)
        let data = ano + '-' + mes + '-' + dia
        const inicio = new Date(data)

        dia = element.fim.substring(2, 0)
        mes = element.fim.substring(5, 3)
        ano = element.fim.substring(10, 6)
        data = ano + '-' + mes + '-' + dia
        const fim = new Date(data)
        const diferenca = fim.getTime() - inicio.getTime()

        const duracao = this.parseMillisecondsIntoReadableTime(diferenca)
        element.duracao = duracao
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
  width: 70vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
