from django.http import JsonResponse

def contact_list(request):
    return JsonResponse({"contact_list": [{"name": "name1", "img": "img1"}, {"name": "name2", "img": "img2"}, {"name": "name3", "img": "img3"}]})


