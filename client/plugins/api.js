export default function ({ $axios }, inject) {
  const api = $axios.create({
    headers: {
      common: {
        Accept: 'text/plain, */*',
      },
    },
  })

  api.setBaseURL('http://127.0.0.1:80/')

  inject('api', api)
}
