from django.urls import path
from .views import chat_bot_view, index

urlpatterns = [
    path('chat/', chat_bot_view, name='chat-bot'),
    path('', index, name='index'),
]