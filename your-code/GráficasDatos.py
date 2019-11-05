import matplotlib.pyplot as plt
import pandas

promedios_diarios_temperaturas = pandas.read_csv('PromediosDiarios2019.csv')
numero_viajes_diarios = pandas.read_csv('ConteoViajes.csv')

ax = plt.gca()
promedios_diarios_temperaturas.plot(kind = 'line',x ='Fecha',y='BJU',color ='red',ax = ax)
promedios_diarios_temperaturas.plot(kind = 'line',x ='Fecha',y='MGH', color ='blue', ax = ax)
promedios_diarios_temperaturas.plot(kind = 'line',x ='Fecha',y='MER', color ='orange', ax = ax)

numero_viajes_diarios.plot(kind = 'line',x = 'Fecha', y = 'Numero_Viajes')

plt.show()
