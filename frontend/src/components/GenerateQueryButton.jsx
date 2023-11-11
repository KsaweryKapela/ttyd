import React from 'react';
import ActionLabel from './ActionLabel';

function GenerateQueryButton({ onClick, disabled, backendReady }) {
  return (
    <button
      className={`px-4 py-2 text-white font-bold rounded shadow ${disabled ? 'bg-gray-400' : 'bg-blue-500 hover:bg-blue-700'}`}
      onClick={onClick}
      disabled={disabled}
    >
      <ActionLabel label="Generate SQL Query" backendReady={backendReady}/>
    </button>
  );
}

export default GenerateQueryButton;
