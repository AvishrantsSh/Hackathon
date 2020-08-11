from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Hospital_Records, Records
from django.views import generic
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
        context['graph'] = obj.get_stats()
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
            User.objects.create_user(
                                        username= chr(i+65),
                                        email= 'sample@email.co.uk',
                                        password="hocuspocus"
                                    ).save()
            
        for i in range(1000):
            Records.objects.create(age=random.randrange(18,78), medical_history=",".join([random.choice(['0','1']) for k in range(7)]), status=random.choice(["Admitted","Released","Death"]))
        
        return HttpResponseRedirect('')

    return HttpResponse('home')
# Create your views here.
