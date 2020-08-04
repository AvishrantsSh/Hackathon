from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        return HttpResponse(received_json_data+"Yahi hai?")    
    
    return HttpResponse("Lag Gaye")
# Create your views here.
