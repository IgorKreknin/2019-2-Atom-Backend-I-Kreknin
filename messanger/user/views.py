from django.http import JsonResponse 

def user(request):
    if request.method == 'GET':
        id = request.GET.get('id') 
    else:
        raise
    return JsonResponse({"name": "user", "id": id, "photo": "img", "status": "online"})
