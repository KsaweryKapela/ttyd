import defaultAxios from './defaultAxios';

async function promptApi(ddl, prompt) {
  console.log(ddl)
  console.log(prompt)
    const response = await defaultAxios.post('/prompt', {
        ddl: ddl,
        prompt: prompt,
    })

  return response
}

export default promptApi;
