import pandas
import requests
import datetime

respuesta = requests.get('http://www.aire.cdmx.gob.mx/opendata/anuales_horarios/meteorolog%C3%ADa_2019.json')
data = respuesta.json()
temperaturas ={}

#Se extrae la información de temperaturas del JSON recorriendolo
for info in data['pollutionMeasurements']['date']:
    temperaturas[info] = data['pollutionMeasurements']['date'][info]['TMP']

#Se transpone el dataframe resultante
df = pandas.DataFrame(temperaturas)
temperaturasXhora = df.T

# Sólo escogí las estaciones meteorologicas en donde son zonas de ecobici
temperaturasXhora_seleccionados = temperaturasXhora[['BJU','MER','MGH']]
temperaturasXhora_seleccionados = temperaturasXhora_seleccionados.reset_index()
temperaturasXhora_seleccionados = temperaturasXhora_seleccionados.rename(columns={'index':'Fecha'})

# Separar la hora de la fecha
temperaturasXhora_seleccionados['Hora'] = temperaturasXhora_seleccionados['Fecha'].map(lambda x:x.split(' ')[1])
temperaturasXhora_seleccionados['Fecha'] = temperaturasXhora_seleccionados['Fecha'].map(lambda x: datetime.datetime.strptime(x.split(' ')[0],'%Y-%m-%d'))
temperaturasXhora_seleccionados['BJU'] = temperaturasXhora_seleccionados['BJU'].map(lambda x: None if x == '' else float(x))
temperaturasXhora_seleccionados['MGH'] = temperaturasXhora_seleccionados['MGH'].map(lambda x: None if x == '' else float(x))
temperaturasXhora_seleccionados['MER'] = temperaturasXhora_seleccionados['MER'].map(lambda x: None if x == '' else float(x))
#Se llenan los datos vacios con el promedio aproximado de las temperaturas de cada estación para no alterar demasiado los promedios por día
temperaturasXhora_seleccionados['BJU'] = temperaturasXhora_seleccionados['BJU'].fillna(18.82)
temperaturasXhora_seleccionados['MGH'] = temperaturasXhora_seleccionados['MGH'].fillna(18.93)
temperaturasXhora_seleccionados['MER'] = temperaturasXhora_seleccionados['MER'].fillna(18.94)
temperaturasXhora_seleccionados.to_csv('TemperaturasCDMX.csv',index='False')

#Se crea un dataframe vacío en el que se vaciaran los promedios diarios de temperatura por estación
dias_tabla = list(set(temperaturasXhora_seleccionados['Fecha']))
columnas_promedio = ['BJU','MGH','MER']

promedios_temperaturas = pandas.DataFrame(index = dias_tabla,columns=columnas_promedio)
promedios_temperaturas = promedios_temperaturas.fillna(0)

# Se calculan los promedios por día y se vacían en el dataframe creado anteriormente
for fecha in dias_tabla:
    temperaturasXdia = temperaturasXhora_seleccionados[temperaturasXhora_seleccionados['Fecha'] == fecha]
    promedios_temperaturas.loc[fecha,'BJU'] = temperaturasXdia['BJU'].mean()
    promedios_temperaturas.loc[fecha,'MER'] = temperaturasXdia['MER'].mean()
    promedios_temperaturas.loc[fecha,'MGH'] = temperaturasXdia['MGH'].mean()

#Se ordena el indice ya que antes era un Set
promedios_temperaturas.sort_index(inplace=True)
#En el siguiente documento se tienen los promedios diarios de temperatura
promedios_temperaturas.to_csv('PromediosDiarios2019.csv')


