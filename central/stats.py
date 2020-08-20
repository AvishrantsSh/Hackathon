import os
from math import exp
import requests, json
from datetime import datetime, date

class covid_stats(object):
    def __init__(self):
        pass

    def get_stats(self):
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'temp.json')
        update = Updater(file_path)
        fobj = open(file_path, "r+")
        if not fobj.read(1):
            fobj.close()
            update.get_data()

        fobj = open(file_path, "r+")
        jobj = dict(json.loads(fobj.read()))
        fobj.close()
        return jobj["Time"], jobj["Data"], jobj["TTotal"],jobj["TRecovered"],jobj["TDeceased"],jobj["DTotal"],jobj["DRecovered"],jobj["DDeceased"]

class Updater(object):
    def __init__(self, path):
        self.link = "https://testplotly.herokuapp.com/getstats/general/covid/plotly/data.json"
        self.path = path
        # self.link='http://192.168.43.15:8000/getstats/general/covid/plotly/data.json'

    def get_data(self):
        fobj = open(self.path, "r+")
        response = requests.get(url = self.link)
        fobj.write(str(response.text))
        fobj.truncate()
        fobj.close()

    