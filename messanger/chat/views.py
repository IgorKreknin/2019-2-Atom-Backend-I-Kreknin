from django.http import JsonResponse

def chat(request):
    if request.method == 'GET':
        id = request.GET.get('id') 
    else:
        raise 
    return JsonResponse({"id": id, "messages": [{"name": "user1", "msg": "blablabla"}, {"name": "user2", "msg": "qweqwe"}, {"name": "user1", "msg": "blablabla"}]})
