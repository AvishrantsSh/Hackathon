from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Hospital_Records, Records
from django.views import generic
import json, random
# from central.gcovid_ind import Covid_map
from django.contrib.auth import get_user_model
User=get_user_model()

class GenStats_View(generic.TemplateView):
    model = Records
    template_name = 'stats.html'
    context_object_name = 'records'
    
    # def get_context_data(self, **kwargs):
    #     context = super(GenStats_View, self).get_context_data(**kwargs)
    #     obj = Covid_map()
    #     context['graph'], context['ttotal'], context['trecover'], context['tdeath'], context['dtotal'], context['drecover'], context['ddeath'] = obj.get_stats()
    #     return context       

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
    fields=['name', 'address','bed_capacity']
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
        if data['h_name'] and data['age'] and data['action'] and data['bed_type'] and data['vent']:
            record = Hospital_Records.objects.get(name=data['h_name'])
            if data['cp'] == 'Yes':
                record.ctotal += 1

            tmp = record.available[1:-1].split(',')
            tmp = list(map(int, tmp))
            if data['bed_type']=='General':
                tmp[0] -= 1
            
            elif data['bed_type']=='Emergency':
                tmp[1] -= 1

            elif data['bed_type']=='Isolation':
                tmp[2] -= 1
            record.available = tmp
            if data['vent'] == 'Yes':
                record.ventilator -= 1
            record.save()
            # Record Stuff
            sympt = data['symptoms'].split(' ')
            history = data['history'].split(' ')
            Records.objects.create(age = data['age'], b_group=data['b'], symptoms= sympt, medical_history=history)
            return HttpResponse("Data Received")

        elif data['h_name'] and data['ppe'] and data['blood']:
            record = Hospital_Records.objects.get(name=data['h_name'])
            record.ppe = int(data['ppe'])
            record.blood = list(map(int, data['blood'].split(' ')))
            record.save()

        # except:    
        #     return HttpResponse("I Ka Bhej Diye Ho "+ str(request.user))
    
    return HttpResponse("Lag Gaye")

def random_gen(request):
    if request.method == 'POST':
        for i in range (10):
            Hospital_Records.objects.create(name = chr(i+65), address=chr(i+97), bed_capacity=[random.randrange(50,200,10),random.randrange(50,200,10),random.randrange(50,200,10)])
            User.objects.create_user(
                                        username= chr(i+65),
                                        email= 'sample@email.co.uk',
                                        password="hocuspocus"
                                    ).save()
            
        # for i in range(1000):
        #     Records.objects.create(age=random.randrange(18,78), medical_history=",".join([random.choice(['0','1']) for k in range(7)]), status=random.choice(["Admitted","Released","Death"]))
        
        return HttpResponse('home')

    return HttpResponse('home')
# Create your views here.
