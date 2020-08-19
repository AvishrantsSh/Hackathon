import calendar, os
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
from math import exp
import requests, json
from datetime import datetime, date
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py
import plotly.graph_objs as go

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
        self.today = date.today()
        if str(jobj["Date"]) != str(self.today):
            self.get_data(fobj)
            
        fobj.close()
        return jobj["Data"], jobj["TTotal"],jobj["TRecovered"],jobj["TDeceased"],jobj["DTotal"],jobj["DRecovered"],jobj["DDeceased"]

    def get_data(self):
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'temp.json')
        fobj = open(file_path, "r+")
        response = requests.get(url = self.link)
        # self.todos = response.text
        fobj.write(str(response.text))
        fobj.truncate()
        fobj.close()

    