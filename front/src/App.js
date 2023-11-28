import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Estadisticas from './components/Estadistica/Estadistica';
import Finanzas from './components/Finanza/Finanaza';

class App extends React.Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route path="/estadisticas" element={<Estadisticas />} />
          <Route path="/finanzas" element={<Finanzas />} />
          {/* Agrega más rutas según sea necesario */}
        </Routes>
      </Router>
    );
  }
}

export default App;