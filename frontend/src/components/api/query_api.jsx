import default_axios from './default_axios';

async function query_api(query) {
  console.log(query)
    const response = await default_axios.post('/query', {
        query: query
    })
  return response
}

export default query_api;
