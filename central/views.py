from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Hospital_Records, Records
from django.views import generic
from django.core import serializers

import json, random
from central.gcovid_ind import Covid_map
from django.contrib.auth import get_user_model
User=get_user_model()

class GenStats_View(generic.TemplateView):
    model = Records
    template_name = 'stats.html'
    context_object_name = 'records'
    
    def get_context_data(self, **kwargs):
        context = super(GenStats_View, self).get_context_data(**kwargs)
        obj = Covid_map()
        context['graph'], context['ttotal'], context['trecover'], context['tdeath'], context['dtotal'], context['drecover'], context['ddeath'] = obj.get()
        return context       

class H_Details(generic.DetailView):
    model=Hospital_Records
    template_name='h_details.html'
    def get_object(self):
        user = self.request.user
        if str(user)!= "AnonymousUser":
            try:
                return Hospital_Records.objects.get(name=user.username)
            except:
                return None
        else:
            return None

class Details_change(generic.UpdateView):
    model=Hospital_Records
    template_name='h_details_change.html'
    fields=['name','address','bed_capacity','ventilator','ppe']
    def get_object(self):
        user = self.request.user
        if str(user)!= "AnonymousUser":
            try:
                return Hospital_Records.objects.get(name=user.username)
            except:
                return None
        else:
            return None

class AllRecords(generic.ListView):
    model = Hospital_Records
    template_name = 'all_records.html'
    context_object_name = 'object'

@csrf_exempt
def newdt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if data['h_name'] and data['age'] and data['action'] and data['bed_type'] and data['vent']:
                record = Hospital_Records.objects.get(name=data['h_name'])
                if data['cp'] == 'Yes':
                    record.ctotal += 1

                tmp = record.available.split(',')
                tmp = list(map(int, tmp))
                if data['bed_type']=='General':
                    tmp[0] -= 1
                
                elif data['bed_type']=='Emergency':
                    tmp[1] -= 1

                elif data['bed_type']=='Isolation':
                    tmp[2] -= 1
                record.available = ','.join(tmp)
                if data['vent'] == 'Yes':
                    record.ventilator -= 1
                record.save()
                # Record Stuff
                sympt = data['symptoms'].split(' ')
                sympt = ','.join(sympt)
                history = data['history'].split(' ')
                sympt = ','.join(history)
                Records.objects.create(age = data['age'], b_group=data['b'], symptoms= sympt, medical_history=history)
                return HttpResponse("Data Received")
        except:
            try: 
                if data['h_name'] and data['ppe'] and data['blood']:
                    record = Hospital_Records.objects.get(name=data['h_name'])
                    record.ppe = int(data['ppe'])
                    record.blood = list(map(int, ','.join(data['blood'].split(' '))))
                    record.save()
                    return HttpResponse("Data Received")

            except:    
                return HttpResponse("Application Error")
    
        return HttpResponse("Invalid Format")

def random_gen(request):
    if request.method == 'POST':
        for i in range (10):
            Hospital_Records.objects.create(name = chr(i+65), address=chr(i+97), bed_capacity=[random.randrange(50,200,10),random.randrange(50,200,10),random.randrange(50,200,10)], blood=[50,100,23,56,213,67,36,67])
            User.objects.create_user(
                                        username= chr(i+65),
                                        email= 'sample@email.co.uk',
                                        password="hocuspocus"
                                    ).save()
            
        for i in range(100):
            Records.objects.create(age=random.randrange(18,78), b_group="B+", symptoms="Bahut,dard,hai", medical_history="Bahut,dard,thi")
        
        return HttpResponseRedirect(reverse('home'))

    return HttpResponseRedirect(reverse('home'))

def Fetchdata(request):
    records_all = Records.objects.all()
    record_list = serializers.serialize('json', records_all, fields=('age','b_group','symptoms','medical_history'))
    data = json.loads(record_list)
    tmp=[]
    for d in data:
        del d['pk']
        del d['model']
        tmp.append(d['fields'])
    
    tmp = ','.join(str(t) for t in tmp)
    cleaned_response = {'Data':tmp}
    json_file=json.dumps(cleaned_response)
    return HttpResponse(json_file, content_type="application/json")

# Create your views here.
