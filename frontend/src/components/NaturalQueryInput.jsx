import React from 'react';

function NaturalQueryInput({ value, onChange }) {
  return (
    <div className="my-4">
      <label htmlFor="naturalQuery" className="block text-sm font-medium text-gray-700">
        Describe the data you need
      </label>
      <input
        type="text"
        id="naturalQuery"
        name="naturalQuery"
        className="mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        placeholder="Enter your natural language query"
        value={value}
        onChange={e => onChange(e.target.value)}
      />
    </div>
  );
}

export default NaturalQueryInput;
