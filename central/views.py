from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['name']+"Yahi hai?")    
    
    return HttpResponse("Lag Gaye")
# Create your views here.
