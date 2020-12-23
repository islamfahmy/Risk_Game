import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import counterReducer from './Reducer/MapReducer'
import Websocket from 'react-websocket'

const store = createStore(counterReducer)
const socket = new WebSocket('ws://localhost:8080')
ReactDOM.render(
  
  <Provider store={store}>
    <App socket={socket}/>
  </Provider>,
   document.getElementById('root')
);

