import React from 'react';

function GenerateQueryButton({ onClick, disabled }) {
  return (
    <button
      className={`px-4 py-2 text-white font-bold rounded shadow ${
        disabled ? 'bg-gray-400' : 'bg-blue-500 hover:bg-blue-700'
      }`}
      onClick={onClick}
      disabled={disabled}
    >
      Generate SQL Query
    </button>
  );
}

export default GenerateQueryButton;
