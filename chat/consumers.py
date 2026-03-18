import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # --- MAKE SURE THIS IS INDENTED EXACTLY LIKE THIS ---
    @database_sync_to_async
    def save_message(self, username, room, content, image):
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.first() 
        return Message.objects.create(user=user, room_name=room, content=content, image_url=image)

    @database_sync_to_async
    def delete_message_from_db(self, message_id, username):
        try:
            msg = Message.objects.get(id=message_id, user__username=username)
            msg.delete()
            return True
        except Message.DoesNotExist:
            return False

    async def receive(self, text_data):
        data = json.loads(text_data)
        username = self.scope['user'].username if self.scope['user'].is_authenticated else 'Anonymous'
        
        if 'typing' in data:
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'typing_indicator',
                'username': username,
                'typing': data['typing']
            })
        elif 'action' in data and data['action'] == 'delete':
            success = await self.delete_message_from_db(data['message_id'], username)
            if success:
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'delete_message',
                    'message_id': data['message_id']
                })
        else:
            # Now the class will find this attribute!
            msg_obj = await self.save_message(username, self.room_name, data.get('message', ''), data.get('image', None))
            
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'chat_message',
                'message': msg_obj.content,
                'image_url': msg_obj.image_url,
                'username': username,
                'message_id': msg_obj.id
            })

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def typing_indicator(self, event):
        await self.send(text_data=json.dumps(event))
        
    async def delete_message(self, event):
        await self.send(text_data=json.dumps({
            'action': 'delete',
            'message_id': event['message_id']
        }))