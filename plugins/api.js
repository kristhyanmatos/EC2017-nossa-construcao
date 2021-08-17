export default function ({ $axios }, inject) {
  // Create a custom axios instance
  const api = $axios.create({
    headers: {
      common: {
        Accept: 'text/plain, */*',
      },
    },
  })

  // Set baseURL to something different
  api.setBaseURL('http://127.0.0.1:80/')

  // Inject to context as $api
  inject('api', api)
}
