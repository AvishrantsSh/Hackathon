from apscheduler.schedulers.blocking import BlockingScheduler
from central.models import Records
from django.core import serializers
import json
from os import path
from datetime import datetime
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=6)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('interval', minutes=1)
def scheduled_job():
    print('Starting daily scheduled job')
    module_dir = path.dirname(__file__)  
    file_path = path.join(module_dir, 'templates/data.json')
    fobj = open(file_path, "w")
    
    records_all = Records.objects.all()
    record_list = serializers.serialize('json', records_all, fields=('age','b_group','symptoms','medical_history'))
    data = json.loads(record_list)
    tmp=[]
    for d in data:
        del d['pk']
        del d['model']
        tmp.append(d['fields'])
    
    tmp = ','.join(str(t) for t in tmp)
    cleaned_response = {'Updated':str(datetime.now()), 'Data':tmp}
    json_file = json.dumps(cleaned_response, indent=4, sort_keys=True)
    fobj.write(json_file)
    fobj.close()

sched.start()