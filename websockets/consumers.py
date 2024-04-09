import json
import re
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer
from .socketEvents import SocketOnEvent


def remove_word_and_special_characters(input_string):
    word_to_remove = "specific"
    # Define regex pattern to match the word and special characters
    pattern = re.compile(r'\b' + re.escape(word_to_remove) + r'\b|\W+')
    # Replace matched pattern with empty string
    result = pattern.sub('', input_string)
    return result


# In the websockets, we just define the on event listener and there is no concept of on and emit like socket.io since
# it just send the raw data and accourding to the if condition we check the event_type and call the approprate functions
# and after processing the request we send back the response in same ws request.

# question arises, How then server send the request to the client socket.io part?

# research: https://chat.openai.com/share/4eb85ccc-d417-4561-ae32-5eb6b9815f91
# https://chat.openai.com/share/2fb30263-eb59-4b7a-a643-0fbbe83e8f64

class WebSocketHandlers(AsyncWebsocketConsumer):
     async def websocket_connect(self, event):
        print("Websocket Connected...", event)
        print("Channel Name...", self.channel_name)
        
        resCount = 1
        await self.email_from_sessionUser(resCount)
        await self.accept()
        
     async def websocket_receive(self, event):
      print("text_data", event)
      
#         {
#     "event_name": "loginStatus",
#     "payload": {
#         "test":"test"
#     }
# }
        
      
      text_data = event.get("text", "")
      text_data_json = json.loads(text_data)

      # Extract the event name and payload from the text data
      event_name = text_data_json.get("event_name", "")
      payload = text_data_json.get("payload", {})
      
      
      if event_name == SocketOnEvent.LOGIN_STATUS.value:
         print("Handling event", event_name)
         await self.process_login_status(payload)
      elif event_name == "event2":
         print("Handling event2")
      else:
         print(f"Unknown event: {event_name}")
    

      # await self.send(text_data=json.dumps({
      #    'data': text_data_json
      # }))

     async def websocket_disconnect(self, close_code):
        print(f"Websocket Disconnected: {close_code}")
        raise StopConsumer()
     
     async def process_login_status(self, data):
        print("process_login_status", data)

        response_data = {
            'username': "username",
            'user_count': "user_count"
        }
        
      # emiting method 
      # await self.emit_from_client("HELLO DATA")

        await self.send(text_data=json.dumps(response_data))
        
     async def response_user_count(self, data): 
        print("Response user data...", data)
        
     async def delete_user_data(self, data): 
        print("Delete user data...", data)

     async def emit_from_client(self, data): 
        print("Emit from client...", data)
         
     async def join(self, data): 
        print("join...", data)
        
     async def force_stop_upgrade_process(self, data): 
        print("ForceStopUpgradeProcess...", data)
        
     async def force_stop_config_process(self, data): 
        print("ForceStopUpgradeProcess...", data)
   
     async def email_from_sessionUser(self, data): 
        print("EMAIL FROM SESSION USER")
   