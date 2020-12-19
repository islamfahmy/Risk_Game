import asyncio
import websockets

const socket = new WebSocket('ws://localhost:8080')
socket.addEventListener('oper',function(event){
 socket.send('Hello server !')
})
socket.addEventListener('message',function(event){
	console.log("message ",event.data)
	})