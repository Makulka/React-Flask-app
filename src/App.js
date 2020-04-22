import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentNostro, setCurrentNostro] = useState(0);

  useEffect(() => {
    fetch('/nostro').then(res => res.json()).then(data => {
      console.log(data)
      setCurrentNostro(data.nostro_name);
    });
  }, []);
  
  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current nostro is {currentNostro}.</p>
      </header>
    </div>
  );
}

export default App;

//https://jaredpalmer.com/formik/docs/tutorial