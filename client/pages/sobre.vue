<template>
  <div>
    <p class="text-top">OBJETIVO DA APLICAÇÃO</p>
    <div class="text-top">
      O objetivo desta aplicação é fazer a analise de dados de projetos de contrução civil
      da cidade de Marabá-PA. O processo de licitação de um projeto na cidade é documentado e expresso 
      no site do municipio, presente em https://maraba.pa.gov.br/ , todo projeto detêm alguns parametros
      como o código, data de inicio e fim do projeto, o valor previsto de gastos iniciais e o valor liquidado,
      valor esse representando o total de gastos que o projeto deteve, desse modo é o valor final pago pela 
      prefeitura.
      Nessa perspectiva existe um problema, pois grande parte das vezes os projetos detêm um valor liquidado final com até
      600% do valor inicial de acrescimo, desse modo demonstra-se um superfaturamento exarcebado nos projetos,
      que pode ser por diversos fatores, entretanto para uma boa gestão é necessário mapear essa problemática e 
      com esse intuito nossa aplicação resume em um gráfico essa analise de discrepância entre os valores previstos
      e o real valor gasto pela prefeitura desde 2019 a a 2022(valores pagos até o momento).  
     
    </div>
   <b-card-group deck>
    <b-card title="Title" img-src="https://instagram.fmab1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/82878889_555066915090242_7732950829602177024_n.jpg?_nc_ht=instagram.fmab1-1.fna.fbcdn.net&_nc_ohc=HUaDtMTxfvwAX-LJUqL&edm=AP_V10EBAAAA&ccb=7-4&oh=7b9336861fe7f94dc0d9cd056ad589d7&oe=61237B97&_nc_sid=4f375e" img-alt="Image" img-top>
      <b-card-text>
        Desenvolvedor: Mikael Almondes da Silva
        Curso: Engenharia da Computação
        Turma: 2017
        Disciplina: Banco de Dados e Desenvolvimento WEB
      </b-card-text>
    </b-card>

    <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
      <b-card-text>
        Desenvolvedor: Kristhyan de Matos Maia
        Curso: Engenharia da Computação
        Turma: 2017
        Disciplina: Banco de Dados e Desenvolvimento WEB
      </b-card-text>
    </b-card>
 
  </div>
</template>

<script>
  
    export default{
        name: 'SobreNos'
      
    }
    
</script>

<style scoped>

    .text-top{
        color: var(--color-text-light);
        font-size: 22px;
        margin-bottom: 20px;
    }
</style>