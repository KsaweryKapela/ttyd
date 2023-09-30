import default_axios from './default_axios';

async function prompt_api(ddl, prompt, query) {
  console.log(ddl)
  console.log(prompt)
  console.log(query)
    const response = await default_axios.post('/mock_prompt', {
        ddl: ddl,
        prompt: prompt,
        query: query
    })

  return response
}

export default prompt_api;
