import './App.css'; 
import React, { useState } from 'react';
import Circle from './components/Circle'
import map from './map'
import counterReducer from './Reducer/MapReducer'
import { createStore } from 'redux'
import { useSelector, useDispatch } from 'react-redux'
var coords = [];
  
const App=()=> {
   
  const dispatch = useDispatch()
  const cities = useSelector(state => state)
  const store = createStore(counterReducer);
 if(!cities)
    dispatch({ type: 'INIT' })
  return (
    <div className="App" >
    {cities&&cities.map(m=><Circle key = {m.id} x={m.x} y= {m.y} color={m.color} r={m.r} count ={m.id} /> )}
    <div className="but"> 
    
    </div>
    </div>
  );
}

export default App;
/*<button onClick={e => dispatch({ type: 'INIT' })}>
     Initialise
    </button>
    <button onClick={e => dispatch({ type: 'COLOR',data:{id:1,color:'blue'} })}>
     color
    </button>
    */