from django.urls import path
from .consumers import *


websocket_urlpatterns = [
    path('ws/app/', WebSocketHandlers.as_asgi())
]
