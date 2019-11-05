#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import re
from bs4 import BeautifulSoup



def datos_banxico():
    
    def api(url):
        response = requests.get(url)
        results = response.json()
        results=pd.io.json.json_normalize(results)
        return results
        
        
    url='https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/2019-10-01/2019-11-01?token=452d8bd2f431ce514eb9189c21b7764105fb48064a48701a80c89b06f48a9629'
    results=api(url)
    url2='https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43774/datos/2019-10-01/2019-11-01?token=452d8bd2f431ce514eb9189c21b7764105fb48064a48701a80c89b06f48a9629'
    results_ob=api(url2)

    
    lista1=[]
    lista2=[]
    
    for item in results['bmx.series'][0]:
        lista2.append(item['datos'])

    lista2=lista2[0]

    lista1=[]

    for item in results_ob['bmx.series'][0]:
        lista1.append(item['datos'])

    lista1=lista1[0]
    

    fechas_tc=[]
    tc=[]
    tasao=[]
    fechas_tc=[d['fecha'] for d in lista2]
    tc=[d['dato'] for d in lista2]

    data_banxico=pd.DataFrame(fechas_tc,columns=['fechas'])
    data_banxico['Tipo_Cambio']=tc
    
    tasao=[d['dato'] for d in lista1]
    data_banxico['Tasa_inversion_diaria']=tasao
    
    data_banxico['fechas'] = pd.to_datetime(data_banxico['fechas'])
    data_banxico['Max']=""
    maxi=data_banxico['Tipo_Cambio'].max()
    data_banxico['Max'][0]=maxi
    maxi=data_banxico['Tipo_Cambio'].max()
  
    index_label = data_banxico[data_banxico['Tipo_Cambio']==maxi].index.tolist() 
    index_label=int(index_label[0])
    data_banxico['fecha_max']=""
    fecha_max=data_banxico['fechas'][index_label]
    data_banxico['fecha_max'][0]=fecha_max
    
    data_banxico['Min']=""
    mini=data_banxico['Tipo_Cambio'].min()
    data_banxico['Min'][0]=mini
 
    
    index_label = data_banxico[data_banxico['Tipo_Cambio']==mini].index.tolist() 
    index_label=int(index_label[0])
    data_banxico['fecha_min']=""
    fecha_min=data_banxico['fechas'][index_label]
    data_banxico['fecha_min'][0]=fecha_min


    data_banxico.to_csv('Banxico.csv',index=False)

    return data_banxico

def websca(): 
    news=[]
    fechas=[]
    for i in range(1,20):
        url=f'https://www.reuters.com/news/archive/mexico-news?view=page&page={i}&pageSize=10'
        html = requests.get(url).content
        soup = BeautifulSoup(html, "lxml")
        names=soup.find_all('h3',{'class':'story-title'})
        times=soup.find_all('span',{'class':'timestamp'})
        names = list([name.text.strip().split("\n") for name in names])
        news.append(names[0:-3])
        times = list([time.text.strip().split("\n") for time in times])
        fechas.append(times)

    
    
    fechas=fechas[0]+fechas[1]+fechas[2]+fechas[3]+fechas[4]+fechas[5]+fechas[6]+fechas[7]+fechas[8]+fechas[9]+fechas[10]+fechas[11]
    news=news[0]+news[1]+news[2]+news[3]+news[4]+news[5]+news[6]+news[7]+news[8]+news[9]+news[10]+news[11]
    data=pd.DataFrame(fechas)
    data['news']=news
    data[0] = pd.to_datetime(data[0])
    data.to_csv('News_reuters.csv', index=False)
    return data




datos_banxico()
websca()

