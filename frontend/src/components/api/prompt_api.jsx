import default_axios from './default_axios';

async function prompt_api(ddl, prompt) {
  console.log(ddl)
  console.log(prompt)
    const response = await default_axios.post('/prompt', {
        ddl: ddl,
        prompt: prompt,
    })

  return response
}

export default prompt_api;
