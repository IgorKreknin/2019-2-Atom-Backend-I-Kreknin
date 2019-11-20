from django.http import JsonResponse 
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from user.models import User

@csrf_exempt
def user(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
        	finded_user = find_user(pk)
        	if finded_user is not None:
        		return JsonResponse(finded_user[0].toJSONResponse())
        	return JsonResponse({'error': 'user not found'})
        return JsonResponse({'error': 'enter user name'})

    return HttpResponseNotAllowed(["GET"])

def find_user(username):
	return User.objects.all().filter(username = username) or None