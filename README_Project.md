![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: ¿La temperatura influye en el uso de Ecobicis?

## Overview

En este proyecto traté de encontrar algún patrón sobre el uso de Ecobicis y el clima, por ahora sólo utilice la temperatura promedio del día
de tres estaciones meteorologicas (Benito Juarez,Miguel Hidalgo y Merced) limitando un poco el espacio ya que no en toda la Ciudad de México
existen estaciones de Ecobicis.

Tambien se podrían obtener datos de otros factores meteorologicos como la lluvia , o incluso el índice de contaminación a distintas horas del día,
lo cual tendría un gran impacto en la creación de un nuevo control vehícular (más flexible).

---

## Technical Requirements

Se utilizaron las siguientes bibliotecas:

*Pandas
*requests
*matplotlib
*datetime

## Note:

Desgraciadamente para acceder a los datos de Ecobici es necesario contar con una API key, la cuál solicité y aún no han contestado,
encontré información "reciente" de los viajes diarios realizados y con ellos hice este proyecto, pero sólo los podía descargar en .csv.
Estos archivos se encuentran en la carpeta "Ecobici".

## Construction

Al principio pensdaba utilizar los datos de contaminación de la Ciudad de México por lo que investigué en la Dirección de Monitoreo Atmosférico,
en este sitio se puede consultar información por hora en formato JSON sobre los datos que recogen diferentes estaciones.

Decidí empezar por las temperaturas, escogí tres estaciones de mi interes y calculé el promedio de temperatura diario de cada estación. Para los datos
vacíos decidí utilizar el promedio general aproximado de cada columna para no alejar demasiado el promedio calculado al real.

Con los datos de Ecobici decidí solo contar el número de viajes diarios realizados para intentar relacionarlos con las temperaturas.
Creo que sería también útil revisar la duración de los viajes, ya que, probablemente si hay bajas temperaturas los usuarios prefieran realizar
viajes más cortos.

## Conclusiones

No logré ver un patrón en el número de viajes realizados y las temperaturas pero creo que es porque estoy considerando los fines de semanas,
y eso hace que las tendencias no sean muy claras a simple vista.

* [Monitoreo Atmosférico](http://www.aire.cdmx.gob.mx/default.php?opc=%27aKBhnmI=%27&opcion=Zw==)
* [Datos Abiertos Ecobici](https://www.ecobici.cdmx.gob.mx/es/informacion-del-servicio/open-data)
