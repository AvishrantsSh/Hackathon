from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Hospital_Records, Age_Freq
import json

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        # try:
        #     if request.POST['h_name'] and request.POST['age'] and request.POST['action']:
        #         new_record = Hospital_Records.objects.get(name=request.POST['h_name'])
        #         new_record.address = request.POST['action']
        #         new_record.available -= 1
        #         new_record.save()

        #         # Age Stuff
        #         age = Age_Freq.objects.get(age=request.POST['age'])
        #         age.frequency += 1
        #         age.save()
        #         return HttpResponse("Nice Boi")
        # except:    
        #     return HttpResponse("I Ka Bhej Diye Ho")               
        # return HttpResponse(str(request.body)+" ye mila mujhe" + str(type(request.body)))
        return JsonResponse(json.loads(request.body))
    return HttpResponse("Lag Gaye")
# Create your views here.
