import os
from math import exp
import requests, json
from datetime import datetime, date

class covid_stats(object):
    def __init__(self):
        self.link = "https://testplotly.herokuapp.com/getstats/general/covid/plotly/data.json"
        # self.link='http://192.168.43.15:8000/getstats/general/covid/plotly/data.json'
    
    def get_stats(self):
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'temp.json')
        fobj = open(file_path, "r+")
        if not fobj.read(1):
            fobj.close()
            self.get_data()

        fobj = open(file_path, "r+")
        jobj = dict(json.loads(fobj.read()))
        fobj.close()
        return jobj["Time"], jobj["Data"], jobj["TTotal"],jobj["TRecovered"],jobj["TDeceased"],jobj["DTotal"],jobj["DRecovered"],jobj["DDeceased"]

    def get_data(self):
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'temp.json')
        response = requests.get(url = self.link)
        fobj = open(file_path, "w")
        fobj.write(str(response.text))
        fobj.truncate()
        fobj.close()

    