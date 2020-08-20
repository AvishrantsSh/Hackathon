from apscheduler.schedulers.blocking import BlockingScheduler
from central.stats import Updater
from django.core import serializers
import json
from os import path
from datetime import datetime
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=20)
def timed_job():
    # try:
    print('Running scheduled Job')
    module_dir = path.dirname(__file__)  
    file_path = path.join(module_dir, 'central/temp.json')
    obj = Updater(file_path)
    obj.get_data()
    print("Job Completed Successfully")

    # except:
    #     print("Something went wrong")
sched.start()