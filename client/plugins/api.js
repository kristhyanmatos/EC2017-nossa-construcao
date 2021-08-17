export default function ({ $axios }, inject) {
  const api = $axios.create({
    headers: {
      common: {
        Accept: 'text/plain, */*',
      },
    },
  })

  api.setBaseURL('https://nossa-construcao.herokuapp.com/')

  inject('api', api)
}
