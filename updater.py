from apscheduler.schedulers.blocking import BlockingScheduler
from central.stats import covid_stats
from django.core import serializers
import json
from os import path
from datetime import datetime
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    try:
        print('Running scheduled Job')
        obj = covid_stats()
        obj.get_data()
        print("Job Completed Successfully")

    except:
        print("Something went wrong")
sched.start()