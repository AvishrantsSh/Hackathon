from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Hospital_Records
import json

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        try:
            if request.POST['h_name'] and request.POST['age'] and request.POST['action']:
                new_record = Hospital_Records.objects.get(name=request.POST['h_name'])
                new_record.address = request.POST['action']
                new_record.available -= 1
                new_record.total += 1
                new_record.save()

                # Age Stuff
                return HttpResponse("Nice Boi")
        except:    
            return HttpResponse("I Ka Bhej Diye Ho")               
        return HttpResponse(str(request.body)+" ye mila mujhe" + str(type(request.body)))

    return HttpResponse("Lag Gaye")

def random_gen(request):
    if request.method == 'POST':
        return None

    return HttpResponse('home')
# Create your views here.
