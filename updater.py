from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import serializers
import json, requests
from os import path
from datetime import datetime
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=20)
def timed_job():
    # try:
    print('Running scheduled Job')
    module_dir = path.dirname(__file__)  
    file_path = path.join(module_dir, 'central/temp.json')
    fobj = open(file_path, "w")
    response = requests.get(url = 'https://testplotly.herokuapp.com/getstats/general/covid/plotly/data.json')
    # self.todos = response.text
    fobj.write(str(response.text))
    fobj.truncate()
    fobj.close()
    print("Job Completed Successfully")

    # except:
    #     print("Something went wrong")
sched.start()