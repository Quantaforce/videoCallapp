# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = "chat_%s" % self.room_name

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat_message", "message": message}
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name='Test-Room'
        print("working")

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name

        )
        print("disconnected")
    
    async def receive(self,text_data):
        receive_dict=json.loads(text_data)
        message=receive_dict['message']
        action = receive_dict['action']
        if (action == 'new-offer') or (action == 'new-answer'):
            print(receive_dict)
            receiver_channel_name=receive_dict['message']['receiver_channel_name']

            receive_dict['message']['receiver_channel_name']=self.channel_name

            await self.channel_layer.send(
                receiver_channel_name,
                {
                    'type':'send.sdp',
                    'receive_dict':receive_dict
                })
            return

        receive_dict['message']['receiver_channel_name']=self.channel_name
        
        async def send_message(self,event):
            message=event['message']
            await self.send(text_data=json.dumps({
                'message':message
            }))

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'send.sdp',
                'receive_dict':receive_dict
            }

        )
    async def send_sdp(self,event):
        receive_dict=event['receive_dict']

        await self.send(text_data=json.dumps(receive_dict))
        
