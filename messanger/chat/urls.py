from django.urls import path
from chat.views import chat

urlpatterns = [
    path('<int:chat_id>', chat, name="chat"),
]

