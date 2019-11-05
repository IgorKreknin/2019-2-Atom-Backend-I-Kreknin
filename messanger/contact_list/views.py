from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse({"contact_list": [{"name": "name1", "img": "img1"}, {"name": "name2", "img": "img2"}, {"name": "name3", "img": "img3"}]})


