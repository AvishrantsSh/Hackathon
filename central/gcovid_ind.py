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

class Covid_map(object):
    def __init__(self):
        self.link = "https://api.covid19india.org/data.json"
        
    def get_stats(self):
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'temp.txt')
        fobj = open(file_path, "r+")
        flist = fobj.read().split('$')
        if str(flist[0])[5:] == str(date.today()):
            fobj.close()
            return str(flist[1])[5:], str(flist[2])[7:],str(flist[3])[11:],str(flist[4])[10:],str(flist[5])[7:],str(flist[6])[11:],str(flist[7])[10:], 
        
        self.get_data()
        self.normalise()
        data = self.plot_graph()
        fobj.write("Date:"+str(date.today())+
                    "$Data:"+str(data)+
                    "$TTotal:"+str(self.total)+
                    "$TRecovered:"+str(self.recovered)+
                    "$TDeceased:"+str(self.deceased)+
                    "$DTotal:"+str(self.tchange)+
                    "$DRecovered:"+str(self.rchange)+
                    "$DDeceased:"+str(self.dchange)
                    )

        fobj.truncate()
        fobj.close()
        return data, self.total, self.recovered, self.deceased, self.tchange, self.rchange, self.dchange

    def func_logistic(self, t, a, b, c):
        return c / (1 + a * np.exp(-b*t))

    def get_data(self):
        response = requests.get(url = self.link)
        self.todos = json.loads(response.text)

    def normalise(self):
        x = len(self.todos['cases_time_series'])
        tmp = self.todos['cases_time_series'][x-1]
        self.total, self.recovered, self.deceased = tmp['totalconfirmed'], tmp['totaldeceased'], tmp['totalrecovered']
        self.tchange, self.rchange, self.dchange = tmp['dailyconfirmed'], tmp['dailydeceased'], tmp['dailyrecovered']
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
        tmp = np.array(df['new_cases'])
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
        ##Method-1
        # fig = plot_plotly(m, forecast)  # This returns a plotly Figure
        # return py.plot(fig, output_type='div', include_plotlyjs=False,show_link=False, link_text="")

        ##Method-2
        yhat = go.Scatter(
                        x = forecast['ds'],
                        y = forecast['yhat'],
                        mode = 'lines',
                        marker = {
                            'color': '#3bbed7'
                        },
                        line = {
                            'width': 3
                        },
                        name = 'Forecast',
                        )

        yhat_upper = go.Scatter(
                                x = forecast['ds'],
                                y = tmp,
                                marker=dict(color="crimson", size=5),
                                mode="markers",
                                name = 'Actual',

                                )



        layout = go.Layout(
                        yaxis = {'title': {'text': 'y'}, 'automargin':True},
                        hovermode = 'x',
                        xaxis = {'rangeselector': {'buttons': [{'count': 7, 'label': '1w', 'step': 'day', 'stepmode': 'backward'},
                                                                            {'count': 1,
                                                                                'label': '1m',
                                                                                'step': 'month',
                                                                                'stepmode': 'backward'},
                                                                            {'count': 6,
                                                                                'label': '6m',
                                                                                'step': 'month',
                                                                                'stepmode': 'backward'},
                                                                            {'count': 1, 'label': '1y', 'step': 'year', 'stepmode': 'backward'},
                                                                            {'step': 'all'}]},
                                                'rangeslider': {'visible': True},
                                                'title': {'text': 'ds'},
                                                'automargin': True,
                                                'type': 'date'},
                        
                        legend = {
                            'yanchor':"top",
                            'y':0.99,
                            'xanchor':"left",
                            'x':0.01
                      },
                      autosize = True,
                      margin= {
                          'l': 10, 
                          'r': 0, 
                          't':75, 
                          'b': 10, 
                          'pad':0,},
                        )

        data = [yhat_upper, yhat]
        fig = dict(data = data, layout = layout)
        return py.plot(fig, output_type='div', include_plotlyjs=False, show_link=False, link_text="", image_width='100px', image_height='100px', config={'responsive':True})
