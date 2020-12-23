import React from 'react'
import map from '../map'
const {cities} = map
const initState =cities
const  mapReducer=(state=[] , action) => 
{
  switch (action.type) {
   case "INIT":
   {
     return initState;
   }
   case "COLOR":
   	{ 
      var i ;
      for(i=0;i<state.length;i++)
        state[i].color=action.data[i];
   		return state.map(s=>s)
   	}
    case "COLOR_ONE" :
    { console.log(action.data)
      return state.map(s=>{
        if(s.id===action.data.id)
         s.color=action.data.color 
        return s })
      
    }
  }
}
export default mapReducer;