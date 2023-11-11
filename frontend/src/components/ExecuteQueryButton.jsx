import React from 'react';

function ExecuteQueryButton({ onClick, disabled }) {
  return (
    <button
      className={`my-4 px-4 py-2 text-white font-bold rounded shadow ${
        disabled ? 'bg-gray-400' : 'bg-green-500 hover:bg-green-700'
      }`}
      onClick={onClick}
      disabled={disabled}
    >
      Execute Query
    </button>
  );
}

export default ExecuteQueryButton;
