import { useEffect, useState } from "react";
import Wordle from "./components/Wordle";
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Dashboard from "./components/Dashboard/Dashboard";
import Preferences from "./components/Preferences/Preferences";



function App() {
  const [solution, setSolution] = useState(null)

  useEffect(() => {
    fetch('http://localhost:3001/solutions')
    .then(res => res.json())
    .then(json => {
      // Generating a random integer between 0 & 14 to select a word
      const randomSolution = json[Math.floor(Math.random()*json.length)]
      setSolution(randomSolution.word)
    })
  }, [setSolution])


  /*const [token, setToken] = useState();
  if(!token) {
    return <Login setToken={setToken} />
  }*/

  return (
    <div className="wrapper">
      <div className="App">
        <h1>Wordle</h1>
        {solution && <Wordle solution={solution} />}
      </div>
      <BrowserRouter>
      <Routes>
        <Route exact path='/dashboard' element={< Dashboard />}></Route>
        <Route exact path='/preferences' element={< Preferences />}></Route>
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

//<div className="App">
//<h1>Wordle</h1>
//{solution && <Wordle solution={solution} />}
//</div>