import React from 'react';

function SQLQueryInput({ value, onChange }) {
  return (
    <div className="my-4">
      <label htmlFor="sqlQuery" className="block text-sm font-medium text-gray-700">
        SQL Query
      </label>
      <textarea
        id="sqlQuery"
        name="sqlQuery"
        className="mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        placeholder="Generated SQL query will appear here"
        value={value}
        onChange={e => onChange(e.target.value)}
        rows="4"
      />
    </div>
  );
}

export default SQLQueryInput;
