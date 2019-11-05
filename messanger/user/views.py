from django.http import JsonResponse 
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user(request, user_id):
    if request.method == 'GET':
        return JsonResponse({"name": "user", "id": user_id, "photo": "img", "status": "online"})    
    return HttpResponseNotAllowed(["GET"])
