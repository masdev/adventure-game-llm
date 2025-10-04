import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
import StoryLoader from "./components/StoryLoader"
import StoryGenerator from "./components/StoryGenerator";

import './App.css'

function App() {

  return (
    <Router>
      <div className="app-conteiner">
        <header>
          <h1>Interactive Story Generator</h1>
        </header>
      </div>
      <main>
        <Routes>
          <Route path={"/story/:id"} element={<StoryLoader />} />
          <Route path={"/"} element={<StoryGenerator />} />
        </Routes>
      </main>
    </Router>
  )
}

export default App;
