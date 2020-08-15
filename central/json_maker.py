from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from central.gcovid_ind import Covid_map
from .models import Records

def start():
    obj = Covid_map()
    scheduler = BackgroundScheduler()
    scheduler.add_job(obj.load_stats(), 'interval', hours=1)
    scheduler.start()

