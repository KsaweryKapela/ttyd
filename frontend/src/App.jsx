import React, { useState } from 'react';
import DDLInput from './components/DDLInput';
import NaturalQueryInput from './components/NaturalQueryInput';
import GenerateQueryButton from './components/GenerateQueryButton';
import SQLQueryInput from './components/SQLQueryInput';
import ExecuteQueryButton from './components/ExecuteQueryButton';
import QueryResultsDisplay from './components/QueryResultsDisplay';
import prompt_api from './components/api/prompt_api';
import query_api from './components/api/query_api';

function App() {
  const [ddlSchema, setDdlSchema] = useState('');
  const [naturalQuery, setNaturalQuery] = useState('');
  const [sqlQuery, setSqlQuery] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [isQueryExecuting, setIsQueryExecuting] = useState(false);
  const [queryResults, setQueryResults] = useState({ headers: null, data: null });


  const handleGenerateQuery = async () => {
    setIsGenerating(true);
    const response = await prompt_api(ddlSchema, naturalQuery);
    setSqlQuery(response.data.query);
    setIsGenerating(false);
  };

  const handleExecuteQuery = async () => {
    setIsQueryExecuting(true);
    const response = await query_api(sqlQuery);
    setQueryResults({headers: response.data.headers, data: response.data.data});
    setIsQueryExecuting(false);
  };

  return (
    <div className="container mx-auto p-4">
      <DDLInput value={ddlSchema} onChange={setDdlSchema} />
      <NaturalQueryInput value={naturalQuery} onChange={setNaturalQuery} />
      <GenerateQueryButton onClick={handleGenerateQuery} disabled={!ddlSchema || !naturalQuery || isGenerating} />
      <SQLQueryInput value={sqlQuery} onChange={setSqlQuery} />
      <ExecuteQueryButton onClick={handleExecuteQuery} disabled={!sqlQuery || isQueryExecuting} />
      <QueryResultsDisplay headers={queryResults.headers} data={queryResults.data} />
    </div>
  );
}

export default App