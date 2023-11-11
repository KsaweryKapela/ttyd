import defaultAxios from './defaultAxios';

async function queryApi(query) {
  console.log(query)
    const response = await defaultAxios.post('/query', {
        query: query
    })
  return response
}

export default queryApi;
