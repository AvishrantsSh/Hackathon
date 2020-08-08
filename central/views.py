from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Hospital_Records, Records
import json, random

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data['h_name'] and data['age'] and data['action']:
                new_record = Hospital_Records.objects.get(name=data['h_name'])
                new_record.available -= 1
                new_record.total += 1
                new_record.save()

                # Record Stuff
                Records.objects.create(age = data['age'], status= data['action'])

                return HttpResponse("Nice Boi")
        
        except:    
            return HttpResponse("I Ka Bhej Diye Ho "+ str(request.user))
    
    return HttpResponse("Lag Gaye")

def random_gen(request):
    if request.method == 'POST':
        for i in range (10):
            Hospital_Records.objects.create(name = chr(i+65), address=chr(i+97), bed_capacity=random.randrange(50,200,10))
            
        for i in range(1000):
            Records.objects.create(age=random.randrange(18,78), medical_history=",".join([random.choice(['0','1']) for k in range(7)]), status=random.choice(["Admitted","Released","Death"]))
        
        return HttpResponseRedirect('')

    return HttpResponse('home')
# Create your views here.
