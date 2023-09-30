import './App.css'

function App() {
  return (
    <>
      <h1>TALK TO YOUR DATA</h1>
      <i></i>
      <h2>1. Provide your data scheme</h2>
      <div>
        <p>Drop your DDL here</p>
      </div>
      <h2>2. Describe the data you need</h2>
      <div>
        <textarea name="" id="" cols="30" rows="10"></textarea>
        <button>Generate query</button>
      </div>
      <h2>3. Execute query and get your data</h2>
      <div>
        <textarea name="" id="" cols="30" rows="10"></textarea>
        <button>Execute query</button>
      </div>
      <h2>4. View your results</h2>
      <table></table>
    </>
  )
}

export default App
