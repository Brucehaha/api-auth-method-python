from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from authAPI.decorators import auth_api
# Create your views here.
import hashlib




@csrf_exempt
@auth_api
def asset(request):
    if request.method == "POST":
        tm_key = request.META['HTTP_AUTH_KEY']
        import json
        host_info = json.loads(str(request.body, encoding='utf-8'))
        print(host_info)
    return HttpResponse('....')

