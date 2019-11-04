Proyecto Pipelines

					Ramiro Maravilla Flores



En este proyecto se analizar� el comportamiento electoral en el estado de Aguascalientes, Mx.
La base de datos se obtuvo del portal C�mputos Distritales 2018 del Instituto Nacional Electoral.

Este trabajo se divide en tres partes:
1) Data Acquisition
2) Data Wrangling
3) Data Analysis

Data Acquisiton

1. Se carga la base de datos en formato .csv
2. Se describe la base de datos para verificar las variables que tiene (esta versi�n fue reducida previamente).
3. Obtenemos un describe() para saber cu�ntos registros de votantes hay en la base.
	De esta informaci�n se obtiene que hay 184,181 votantes regitrados.
	Otra informaci�n relevante es que la media de edad del votante de Ags es 40 a�os.


Data Wrangling

4.En esta base de datos no viene el nombre del los distritos electorales de Ags. 
	Por lo tanto, creamos un list comprehension para que ponga los nombres de los distritos.

5.Tiramos la variable Ponderador_Ok dado que no nos sirve para el an�lisis.
6.Verificamos el tipo de casilla que se tiene registrada en esos distritos.
	Eliminamos las casillas que tienen �nicamente "E1" (casilla especial), dado que su naturaleza
	de casilla especial hace que no se pueda comparar la votaci�n en �stas con el resto de las dem�s casillas.

7.Variable Voto.
	Verificamos qu� valores de voto hay. S�lo deber�a haber dos: 1(vot�); 2(no vot�).
	Creamos una funci�n para que en caso de que haya m�s valores en esta variable los tire y nos quedamos s�lo con 1 y 2.

8.Creamos variable "Voto_NoCodificado". Con una list comprehension asiganos el valor "Voto" a 1 y "No_voto" a 2. 
9.Ordenamos las columnas para facilitar su lectura
10. Metemos algunas string operations:
	Ponemos en min�sculas los valores de Nombre_Distrito y Voto_NoCodificado
	Quitamos el espacio y los acentos de la variable Nombre_Distrito

Data Analysis

10. Hago una funci�n para saber el Numero_de_regristros_de_votantes.
11. Hago una funci�n para saber PersonasQueVotaron.
12. Hago una funci�n para conocer el Porcentaje_PersonasQueVotaron.
13. Hago una funci�n para comparar la participaci�n electoral en los distritos de Ags con la nacional (Comparacion_ParticipacionNacional)
14. Hago una funci�n para comprobar en qu� secci�n se vot� m�s: rural, urbana, mixta (voto_por_seccion).
15. Hago una funci�n para conocer qu� sexo vot� m�s: mujeres vs hombres (batalla_sexos2).

