import { useState } from 'react'
import './App.css'
import query_api from './components/api/query_api';
import prompt_api from './components/api/prompt_api';

function App() {
  const [ddl, setDdl] = useState(null);
  const [query, setQuery] = useState('');
  const [inputMethod, setInputMethod] = useState('readFromDb');
  const [response, setResponse] = useState('');

  const [prompt, setPrompt] = useState('');
  const generateQuery = async () => {
    const response = await prompt_api(ddl, prompt, query);
    setQuery(response.data.query);  // Assuming the response is structured as { data: 'your-query-string' }
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/sql') {
      const reader = new FileReader();
      reader.onload = (e) => setDdl(e.target.result);
      reader.readAsText(file);
    }
  };

  const executeQuery = async () => {
    const response = await query_api(query);
    setResponse(response.data);  // Assuming the response is structured as { data: 'your-query-result' }
  };

  return (
    <>
      <h1>TALK TO YOUR DATA</h1>
      <i></i>
      <div>
      <h2>1. Provide your data scheme</h2>
      <div>
        <label>
          <input
            type="radio"
            value="readFromDb"
            checked={inputMethod === 'readFromDb'}
            onChange={(e) => setInputMethod(e.target.value)}
          />
          Read from DB
        </label>
        <label>
          <input
            type="radio"
            value="provideAsText"
            checked={inputMethod === 'provideAsText'}
            onChange={(e) => setInputMethod(e.target.value)}
          />
          Provide as text
        </label>
        <label>
          <input
            type="radio"
            value="uploadSqlFile"
            checked={inputMethod === 'uploadSqlFile'}
            onChange={(e) => setInputMethod(e.target.value)}
          />
          Upload SQL File
        </label>
      </div>
      {inputMethod === 'provideAsText' && (
        <div>
          <textarea
          
            onChange={(e) => setDdl(e.target.value)}
            placeholder="Drop your DDL here or type it in"
            cols="30"
            rows="10"
          ></textarea>
        </div>
      )}
      {inputMethod === 'uploadSqlFile' && (
        <div>
          <input type="file" accept=".sql" onChange={handleFileUpload} />
        </div>
      )}
      <h2>2. Describe the data you need</h2>
      <textarea
        onChange={(e) => setPrompt(e.target.value)} 
        cols="30" 
        rows="10">
      </textarea>
      <button onClick={generateQuery}>Generate query</button>
    </div>
    <div>
        <h2>3. Execute query and get your data</h2>
      <div>
        <textarea 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          cols="30" 
          rows="10">
        </textarea>
        <button onClick={executeQuery}>Execute query</button>
      </div>
    </div>
    
    <div>
        <h2>4. View your results</h2>
      <table>
        <thead>
          {
            response && response.headers && (
              <tr>
                {response.headers.map((header) => (
                  <th key={header}>{header}</th>
                ))} 
              </tr>
            )
          }
        </thead>
        <tbody>
          {
            response && response.data && response.data.map((row) => (
              <tr key={row}>
                {row.map((cell) => (
                  <td key={cell}>{cell}</td>
                ))}
              </tr>
            ))
          }
        </tbody>
      </table>
    </div>
    </>
  )
}

export default App
