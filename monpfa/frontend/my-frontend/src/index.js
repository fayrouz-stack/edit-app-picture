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
          <Route  path='/app' element={app} />
          <Route  path='/VerticalExample' element={VerticalExample} />
        </Routes>
        <App />
         </BrowserRouter>
, );
}