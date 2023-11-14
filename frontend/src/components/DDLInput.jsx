import React, { useState } from 'react';

function DDLInput({ value, onChange }) {
  const [fileContent, setFileContent] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const content = e.target.result;
        setFileContent(content);
        onChange(content);
      };
      reader.readAsText(file);
    }
  };

  const handleTextareaChange = (event) => {
    onChange(event.target.value);
  };

  return (
    <div className="flex flex-col gap-4">
      <textarea
        className="p-2 border border-gray-300 rounded"
        placeholder="Enter DDL schema here"
        value={value || fileContent}
        onChange={handleTextareaChange}
      />
      <input
        type="file"
        className="file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100"
        onChange={handleFileChange}
        accept=".sql"
      />
    </div>
  );
}

export default DDLInput;
