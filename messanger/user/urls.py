from django.urls import path
from user.views import user

urlpatterns = [
    path('<int:user_id>', user, name="user"),
]

