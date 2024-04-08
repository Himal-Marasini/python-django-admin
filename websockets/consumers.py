import json
import re
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer



def remove_word_and_special_characters(input_string):
    word_to_remove = "specific"
    # Define regex pattern to match the word and special characters
    pattern = re.compile(r'\b' + re.escape(word_to_remove) + r'\b|\W+')
    # Replace matched pattern with empty string
    result = pattern.sub('', input_string)
    return result


class WebSocketHandlers(AsyncWebsocketConsumer):
     async def websocket_connect(self, event):
        print("Websocket Connected...", event)
        print("Channel Name...", self.channel_name)
        
        group_name = remove_word_and_special_characters(self.channel_name)
        
        await self.channel_layer.group_add(group_name,self.channel_name)

        await self.accept()
        
     async def websocket_receive(self, event):
      print("text_data", event)
      
      text_data = event.get("text", "")
      text_data_json = json.loads(text_data)

      # Extract the event name and payload from the text data
      event_name = text_data_json.get("event_name", "")
      payload = text_data_json.get("payload", {})
      
      
      if event_name == "event1":
         print("Handling event1")
         
      elif event_name == "event2":
         print("Handling event2")
         
      else:
         print(f"Unknown event: {event_name}")
    

      await self.send(text_data=json.dumps({
         'data': text_data_json
      }))

     async def websocket_disconnect(self, close_code):
        print(f"Websocket Disconnected: {close_code}")
        raise StopConsumer()