import React, { useState } from 'react';
import DDLInput from './components/DDLInput';
import NaturalQueryInput from './components/NaturalQueryInput';
import GenerateQueryButton from './components/GenerateQueryButton';
import SQLQueryInput from './components/SQLQueryInput';
import ExecuteQueryButton from './components/ExecuteQueryButton';
import QueryResultsDisplay from './components/QueryResultsDisplay';
import useBackendCheck from './components/hooks/useBackendCheck';
import promptApi from './components/api/promptApi';
import queryApi from './components/api/queryApi';

function App() {
  const backendReady = useBackendCheck();
  const [ddlSchema, setDdlSchema] = useState('');
  const [naturalQuery, setNaturalQuery] = useState('');
  const [sqlQuery, setSqlQuery] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [isQueryExecuting, setIsQueryExecuting] = useState(false);
  const [queryResults, setQueryResults] = useState({ headers: null, data: null });


  const handleGenerateQuery = async () => {
    setIsGenerating(true);
    const response = await promptApi(ddlSchema, naturalQuery);
    setSqlQuery(response.data.query);
    setIsGenerating(false);
  };

  const handleExecuteQuery = async () => {
    setIsQueryExecuting(true);
    const response = await queryApi(sqlQuery);
    setQueryResults({headers: response.data.headers, data: response.data.data});
    setIsQueryExecuting(false);
  };

  return (
    <div className="container mx-auto p-4">
      <DDLInput value={ddlSchema} onChange={setDdlSchema} />
      <NaturalQueryInput value={naturalQuery} onChange={setNaturalQuery} />
      <GenerateQueryButton onClick={handleGenerateQuery} disabled={!ddlSchema || !naturalQuery || isGenerating} backendReady={backendReady} />
      <SQLQueryInput value={sqlQuery} onChange={setSqlQuery} />
      <ExecuteQueryButton onClick={handleExecuteQuery} disabled={!sqlQuery || isQueryExecuting} backendReady={backendReady} />
      <QueryResultsDisplay headers={queryResults.headers} data={queryResults.data} />
    </div>
  );
}

export default App