from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
import json
import os
path = os.path.abspath('.')


def home(request):
    return render(request, 'index.html')

def get_result():
    from traffic_app.main import detect_traffic_lights
    c = detect_traffic_lights()
    return c

@csrf_exempt
def get_the_report(request):
    dir = path+'/static/test_images/'
    for f in os.listdir(dir):
       os.remove(os.path.join(dir, f))

    file = request.FILES['file']
    fs = FileSystemStorage(location="./static/test_images/")
    filename = fs.save("img_1.jpg", file)
    result = get_result()
    return HttpResponse(result)
