import pandas
import datetime

viajes ={}
#No conseguí el API con ecobici, pero existe la posibilidad de descargar archivos con los datos básicos de viajes realizados
#Se crea un diccionario con un dataframe de viajes realizados.

for month in range(1,10):
    url = '.\\Ecobici\\2019-0%s.csv'%(month)
    viajes[month] = pandas.read_csv(url)

def cantidadViajesDiarios (viajes_mensual):
    dias = set(viajes_mensual['Fecha_Retiro'])
    columnas = ['Numero_Viajes']
    viajes = pandas.DataFrame(index=dias, columns=columnas)
    viajes = viajes.fillna(0)

    for fecha in dias:
        viajes.loc[fecha]['Numero_Viajes'] = fecha
        viajes.loc[fecha]['Numero_Viajes'] = len(viajes_mensual[viajes_mensual['Fecha_Retiro']== fecha])

    return viajes

#Se cuentan los viajes diarios realizados
Cantidad_Viajes_Diarios = {}
for month in range(1,10):
    df = cantidadViajesDiarios(viajes.get(month))
    df.reset_index(inplace=True)
    df.sort_values('index',inplace=True)
    Cantidad_Viajes_Diarios[month] = df

#Esta informacion se une en un solo DataFrame
ConteoViajes = Cantidad_Viajes_Diarios[1]
for month in range(2,10):
    ConteoViajes  = ConteoViajes.append(Cantidad_Viajes_Diarios[month])

ConteoViajes = ConteoViajes.rename(columns = {'index':'Fecha'})
#Existen algunos datos de añs pasados por lo que borraré esas filas
ConteoViajes['Fecha'] = ConteoViajes['Fecha'].map(lambda x: datetime.datetime.strptime(x,'%d/%m/%Y'))

test = list(ConteoViajes[ConteoViajes['Fecha'] < datetime.date(2018,12,31)].index)
ConteoViajes = ConteoViajes.drop(test,axis = 0)
ConteoViajes.sort_values('Fecha',inplace=True)
ConteoViajes.to_csv('ConteoViajes.csv',index=False)