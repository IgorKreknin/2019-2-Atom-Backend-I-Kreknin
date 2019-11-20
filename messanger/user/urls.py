from django.urls import path
from user.views import user

urlpatterns = [
    path('<str:pk>', user, name="user"),
]

