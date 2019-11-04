import pandas

viajes ={}
#No conseguí el API con ecobici, pero existe la posibilidad de descargar archivos con los datos básicos de viajes realizados
#Se crea un diccionario con un dataframe de viajes realizados.

for month in range(1,10):
    url = '.\\Ecobici\\2019-0%s.csv'%(month)
    viajes[month] = pandas.read_csv(url)

def cantidadViajesDiarios (viajes_mensual):
    dias = set(viajes_mensual['Fecha_Retiro'])
    columnas = ['Fecha','Numero_Viajes']
    viajes = pandas.DataFrame(index=dias, columns=columnas)
    viajes = viajes.fillna(0)

    for fecha in dias:
        viajes.loc[fecha]['Numero_Viajes'] = len(viajes_mensual[viajes_mensual['Fecha_Retiro']== fecha])

    return viajes

Cantidad_Viajes_Diarios = {}
for month in range(1,10):
    Cantidad_Viajes_Diarios[month] = cantidadViajesDiarios(viajes.get(month))

print(Cantidad_Viajes_Diarios)