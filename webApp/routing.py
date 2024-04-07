from django.urls import path
from .websockets import WebSocketConsumer


websocket_urlpatterns = [
    path('ws/app/', WebSocketConsumer.as_asgi())
]
