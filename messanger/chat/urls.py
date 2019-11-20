from django.urls import path
from chat.views import chat_list, create_chat

urlpatterns = [
    path('<str:pk>', chat_list, name="chat_list"),
    path('new/', create_chat, name="create_chat")
]

