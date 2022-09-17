import React  from 'react';
import ReactDOM from 'react-dom';
import "./css/index.css"; 
import App from './app.js';
import { BrowserRouter,  Routes, Route } from 'react-router-dom';
import render from 'react-dom'
import VerticalExample from './VerticalExample.js';
import TextLinkExample from '../src/components/header.js'

{ 

ReactDOM.render( <BrowserRouter>
     
     <Routes>
       
          <Route exact path='/ve' component={TextLinkExample} />
        
          <Route exact path='/' component={VerticalExample} />
        
       
        </Routes>
        <App />
        
      

         
         </BrowserRouter>
, document.getElementById('root'));


}