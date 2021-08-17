<template>
  <div id="sobrenos">
    <p class="text-top"><strong> OBJETIVO DA APLICAÇÃO</strong></p>
    <div class="text-top">
      O objetivo desta aplicação é fazer a análise de dados de projetos de
      construção civil da cidade de Marabá-PA. O processo de licitação de um
      projeto na cidade é documentado e expresso no site do município, presente
      em
      <a href="https://maraba.pa.gov.br/" target="_blank"
        >https://maraba.pa.gov.br/</a
      >
      , todo projeto detêm alguns parametros como o código, data de início e fim
      do projeto, o valor previsto de gastos iniciais e o valor liquidado, valor
      esse representando o total de gastos que o projeto deteve, desse modo é o
      valor final pago pela prefeitura. Nessa perspectiva existe um problema,
      pois grande parte das vezes os projetos detêm um valor liquidado final com
      até 600% do valor inicial de acréscimo, desse modo demonstra-se um
      superfaturamento exacerbado nos projetos, que pode ser por diversos
      fatores, entretanto para uma boa gestão é necessário mapear essa
      problemática e com esse intuito nossa aplicação resume em um gráfico essa
      análise de discrepância entre os valores previstos e o real valor gasto
      pela prefeitura desde 2019 à 2022(valores pagos até o momento). Projeto
      publicado no repositório
      <a
        href="https://github.com/kristhyanmatos/EC2017-nossa-construcao"
        target="_blank"
        >GitHub</a
      >.
    </div>
    <b-card-group deck>
      <b-card
        title="Mikael Almondes da Silva"
        :img-src="url_mikael"
        img-alt="Image"
        img-top
      >
        <b-card-text>
          Curso: Engenharia da Computação Turma: 2017 Disciplina: Banco de Dados
          e Desenvolvimento WEB
        </b-card-text>
      </b-card>

      <b-card
        title="Kristhyan de Matos Maia"
        :img-src="url_kristhyan"
        img-alt="Image"
        img-top
      >
        <b-card-text>
          Curso: Engenharia da Computação Turma: 2017 Disciplina: Banco de Dados
          e Desenvolvimento WEB
        </b-card-text>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'SobreNos',
  data() {
    return {
      url_mikael:
        'https://scontent.fmab1-1.fna.fbcdn.net/v/t1.6435-9/77082677_2633306276785876_3182608046652129280_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeF7_w22uG7RR62jr9j7gao23JMyO_fhAlHckzI79-ECUSYsgc5G4YrV2FINL39SF08LW4KUPcZvDUn2urS3Rewx&_nc_ohc=b5R78B8FLdgAX8SNimh&tn=TezutjTH_Xr4VaPO&_nc_ht=scontent.fmab1-1.fna&oh=abc72b3fb9febcde76476be42a12d58a&oe=6140C8DA',
      url_kristhyan:
        'https://pbs.twimg.com/profile_images/1346143037223809034/rEon3b_k.jpg',
    }
  },
})
</script>

<style scoped>
#sobrenos {
  margin-top: 15vh;
}
.text-top {
  color: var(--color-text-light);
  font-size: 22px;
  margin-bottom: 20px;
  text-align: justify;
}
</style>
