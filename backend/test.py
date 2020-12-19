import asyncio
import websockets
import json


async def server(websocket,path) :
  await websocket.send(json.dumps({
        'type':"init",
        'content':[{"id":"1","color":"1"}]
        })) 
start_server = websockets.serve(server,"localhost",8080)

asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever()