# chat/routing.py
from dotenv import load_dotenv
from dotenv import load_dotenv
from dotenv import load_dotenv
from django.urls import re_path

from . import consumers

# websocket_urlpatterns = [
#     re_path(r"ws/video/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
# ]
websocket_urlpatterns = [
   re_path(r"", consumers.ChatConsumer.as_asgi()),
]
