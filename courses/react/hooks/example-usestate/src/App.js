import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [variable, setVariable] = useState("Olá mundo");

  const [body, setBody] = useState({
    key: 1,
    value: "valor"
  })

  const handler = () => {
    setBody({...body, value: "outro"});
    console.log(body.value);
  }
  const [func, setFunc] = useState(handler);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Key: {body.key}</h1>
        <h1>Value: {body.value}</h1>
      </header>
    </div>
  );
}

export default App;
