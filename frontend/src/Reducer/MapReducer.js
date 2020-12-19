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
   		return state.map(m=>{
      	if(m.id===action.data.id) 
      		m.color=action.data.color;
      	 return m 
      })
   	}
  }
}
export default mapReducer;