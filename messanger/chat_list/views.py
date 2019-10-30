from django.http import JsonResponse
from django.shortcuts import render

def chat_list(request):
    return JsonResponse({"chat_list": [{"name": "chat1", "lastMsg": "msg"}, {"name": "chat2", "lastMsg": "msg"}, {"name": "chat1", "lastMsg": "msg"}]})

def showHtml(request):
    return render(request, "chat_list.html")


