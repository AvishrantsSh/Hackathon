from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Hospital_Records
import json

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        # try:
        data = json.loads(request.body)
        if data['h_name'] and data['age'] and data['action']:
            new_record = Hospital_Records.objects.get(name=data['h_name'])
            new_record.address = data['action']
            new_record.available -= 1
            new_record.total += 1
            new_record.save()
        return HttpResponse("Nice Boi")

        # except:    
        #     return HttpResponse("I Ka Bhej Diye Ho")               
        
    return HttpResponse("Lag Gaye")

def random_gen(request):
    if request.method == 'POST':
        return None

    return HttpResponse('home')
# Create your views here.
