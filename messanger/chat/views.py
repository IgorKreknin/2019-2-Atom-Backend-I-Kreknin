from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat(request, chat_id):
    if request.method == 'GET':
        return JsonResponse({"id": chat_id, "messages": [{"name": "user1", "msg": "blablabla"}, {"name": "user2", "msg": "qweqwe"}, {"name": "user1", "msg": "blablabla"}]})
    return HttpResponseNotAllowed(["GET", "POST", "SET"])
