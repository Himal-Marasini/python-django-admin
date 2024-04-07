import json
from channels.generic.websocket import AsyncWebSocketConsumer

class WebSocketConsumer(AsyncWebSocketConsumer):

    async def connect(self):
        print("Websocket Connected...")
        await self.accept()
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(f"Message Received: {text_data_json}")
        await self.send(text_data=json.dumps({
            'data': text_data_json
        }))

    async def disconnect(self, close_code):
        print(f"Websocket Disconnected: {close_code}")
        pass