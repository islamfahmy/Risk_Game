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
   	{ console.log(action.data)
      for(var i=0;i<state.length;i++)
        {
          state[i].color=action.data.data[i];
        state[i].c=action.data.armies[i];
      }
   		return state.map(s=>s)
   	}
    case "COLOR_ONE" :
    { console.log(action.data)
      return state.map(s=>{
        if(s.id===action.data.id)
        { s.color=action.data.color 
                 s.c=action.data.armies
                }
                return s })
      
    }
    case "CHANGE_ARMY" :
    {
return state.map(s=>{
      if(s.id===action.data.id)
          s.c=action.data.armies
        return s ;
    })
  }
 }
}
export default mapReducer;