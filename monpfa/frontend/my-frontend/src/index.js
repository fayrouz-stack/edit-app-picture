import React  from 'react';
import { createRoot } from 'react-dom/client'
import "./css/index.css"; 
import App from './app.js';
import { BrowserRouter,  Routes, Route } from 'react-router-dom';
import VerticalExample from './VerticalExample.js';
import app from './app'

{ 
     createRoot(document.getElementById('root')).render( <BrowserRouter>
     <Routes>
          <Route  exact path='/' element={<App />} />
          <Route  path='/verticalExample' element={<VerticalExample />} />
        </Routes>
        <App />
         </BrowserRouter>
, );
}