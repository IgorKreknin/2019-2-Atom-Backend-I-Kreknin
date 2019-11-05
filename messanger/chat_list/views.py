from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse({"chat_list": [{"name": "chat1", "lastMsg": "msg"}, {"name": "chat2", "lastMsg": "msg"}, {"name": "chat1", "lastMsg": "msg"}]})

@csrf_exempt
def showHtml(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(["GET"])
    return render(request, "chat_list.html")


