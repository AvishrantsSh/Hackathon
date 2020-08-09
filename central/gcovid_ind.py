import calendar
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
from math import exp
import requests, json
from datetime import datetime
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py

class Covid_map(object):
    def __init__(self):
        self.link = "https://api.covid19india.org/data.json"
        self.get_data()
        self.normalise()

    def func_logistic(self, t, a, b, c):
        return c / (1 + a * np.exp(-b*t))

    def get_data(self):
        response = requests.get(url = self.link)
        self.todos = json.loads(response.text)

    def normalise(self):
        x = len(self.todos['cases_time_series'])
        for i in range(x):
            cdate = self.todos['cases_time_series'][i]['date'].split()
            cdate[1] = str(list(calendar.month_name).index(cdate[1]))
            cdate.append("2020")
            cdate.reverse()
            self.todos['cases_time_series'][i]['date']=datetime.strptime("-".join(cdate) ,'%Y-%m-%d')

    def plot_graph(self):
        df = pd.DataFrame(self.todos['cases_time_series'])
        df = df[:][['dailyconfirmed', 'date']]
        df = df.rename(columns = {'dailyconfirmed': 'new_cases', 'dailydeceased':'fatalities'})
        df['new_cases'] = df['new_cases'].astype(int)
        df['date'] = pd.to_datetime(df.date)
        df = df.reset_index(drop=False)
        df['cap']=100000
        df.columns = ['index', 'y', 'ds','cap']

        m = Prophet(growth="logistic")
        m.fit(df)
        future = m.make_future_dataframe(periods=20)
        future['cap'] = df['cap'].iloc[0]

        forecast = m.predict(future)
        forecast['trend'] = forecast['trend'].apply(np.ceil)
        forecast['trend'] = forecast['trend'].astype(int)
        
        fig = plot_plotly(m, forecast)  # This returns a plotly Figure
        return py.plot(fig, output_type='div', include_plotlyjs=False,show_link=False, link_text="")
