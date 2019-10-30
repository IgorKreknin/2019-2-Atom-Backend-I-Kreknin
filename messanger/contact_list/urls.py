from django.urls import path
from contact_list.views import contact_list

urlpatterns = [
    path('', contact_list, name="contact_list"),
]

