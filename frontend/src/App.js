import './App.css'; 
import React, { useState,useEffect } from 'react';
import Circle from './components/Circle'
import counterReducer from './Reducer/MapReducer'
import { createStore } from 'redux'
import { useSelector, useDispatch, } from 'react-redux'

let socket = null
const App=()=> {
    const[action,setAction]=useState("");
    const[attack,setAttack]=useState("");
    const[no,setNo]=useState("");
    if(!socket)
     socket= new WebSocket('ws://localhost:8080')
  // useEffect(() => {
  //  socket.emit('HELLO_THERE');
  const dispatch = useDispatch()
  socket.onmessage = function(event){
   console.log(event.data)
   if(JSON.parse(event.data).type=== "init")
    dispatch({type:'COLOR',data:JSON.parse(event.data).data})
   
   else if(JSON.parse(event.data).type==="color")
    dispatch({type:'COLOR_ONE',data:JSON.parse(event.data).data});
  
   else if(JSON.parse(event.data).type==="army")
    dispatch({type:'CHANGE_ARMY',data:JSON.parse(event.data).data});
   else if(JSON.parse(event.data).type==="string")
    setAction(JSON.parse(event.data).data) 
  }
  const Click=(x)=>
    {
      var temp ={
  attacker:attack,
attacked:x,
armies:no
      };
      socket.send(JSON.stringify(temp))
    }
    const handleSubmit = (evt) => {
      evt.preventDefault();
  }
   
    //})
  const cities = useSelector(state => state)
  const store = createStore(counterReducer);
 if(!cities)
    dispatch({ type: 'INIT' })
  
  return (
    <div>
      <label>
       atacker
        <input
          type="text"
          onChange={e => setAttack(e.target.value)}
        />
      </label>
        <label>
    no:    <input
          type="text"
          onChange={e => setNo(e.target.value)}
        />
      </label>
    
      <t1>
        {action}
      </t1>
    <div className="App" >

    {cities&&cities.map(m=><Circle key = {m.id} x={m.x} y= {m.y} color={m.color} Click={Click} r={m.r} id={m.id} count ={m.c} /> )}
    <div className="but"> 
    
    </div>
    </div>
     </div>
  )
}

export default App;
/*<button onClick={e => dispatch({ type: 'INIT' })}>
     Initialise
    </button>
    <button onClick={e => dispatch({ type: 'COLOR',data:{id:1,color:'blue'} })}>
     color
    </button>
    */