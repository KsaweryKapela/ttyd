import React from 'react';
import ActionLabel from './ActionLabel';

function ExecuteQueryButton({ onClick, disabled, backendReady }) {
  return (
    <button
      className={`px-4 py-2 text-white font-bold rounded shadow ${disabled ? 'bg-gray-400' : 'bg-green-500 hover:bg-green-700'}`}
      onClick={onClick}
      disabled={disabled}
    >
      <ActionLabel label="Execute Query" backendReady={backendReady}/>
    </button>
  );
}

export default ExecuteQueryButton;
