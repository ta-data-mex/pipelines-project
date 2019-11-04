Proyecto Pipelines

					Ramiro Maravilla Flores



En este proyecto se analizará el comportamiento electoral en el estado de Aguascalientes, Mx.
La base de datos se obtuvo del portal Cómputos Distritales 2018 del Instituto Nacional Electoral.

Este trabajo se divide en tres partes:
1) Data Acquisition
2) Data Wrangling
3) Data Analysis

Data Acquisiton

1. Se carga la base de datos en formato .csv
2. Se describe la base de datos para verificar las variables que tiene (esta versión fue reducida previamente).
3. Obtenemos un describe() para saber cuántos registros de votantes hay en la base.
	De esta información se obtiene que hay 184,181 votantes regitrados.
	Otra información relevante es que la media de edad del votante de Ags es 40 años.


Data Wrangling

4.En esta base de datos no viene el nombre del los distritos electorales de Ags. 
	Por lo tanto, creamos un list comprehension para que ponga los nombres de los distritos.

5.Tiramos la variable Ponderador_Ok dado que no nos sirve para el análisis.
6.Verificamos el tipo de casilla que se tiene registrada en esos distritos.
	Eliminamos las casillas que tienen únicamente "E1" (casilla especial), dado que su naturaleza
	de casilla especial hace que no se pueda comparar la votación en éstas con el resto de las demás casillas.

7.Variable Voto.
	Verificamos qué valores de voto hay. Sólo debería haber dos: 1(votó); 2(no votó).
	Creamos una función para que en caso de que haya más valores en esta variable los tire y nos quedamos sólo con 1 y 2.

8.Creamos variable "Voto_NoCodificado". Con una list comprehension asiganos el valor "Voto" a 1 y "No_voto" a 2. 
9.Ordenamos las columnas para facilitar su lectura
10. Metemos algunas string operations:
	Ponemos en minúsculas los valores de Nombre_Distrito y Voto_NoCodificado
	Quitamos el espacio y los acentos de la variable Nombre_Distrito

Data Analysis

10. Hago una función para saber el Numero_de_regristros_de_votantes.
11. Hago una función para saber PersonasQueVotaron.
12. Hago una función para conocer el Porcentaje_PersonasQueVotaron.
13. Hago una función para comparar la participación electoral en los distritos de Ags con la nacional (Comparacion_ParticipacionNacional)
14. Hago una función para comprobar en qué sección se votó más: rural, urbana, mixta (voto_por_seccion).
15. Hago una función para conocer qué sexo votó más: mujeres vs hombres (batalla_sexos2).

