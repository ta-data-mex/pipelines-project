Hipótesis: 
Hay más noticias relacionadas a VIOLENCIA contra las Mujeres que las relacionadas a Ciencia, Tecnología o Política.

Objetivos:

* Recolectar información de un periódico internacional (API) 
* Obtener información de distintos feeds de blogs o revistas online relacionados a Tecnología, Ciencia, Redes Sociales (RSS FEED).  
* Hacer un cruce y análisis de los datos. (DATA FRAMES) 

API
Se hace una conexión a la API del periódico The Guardian. 
#La conexión con la API de The Guardian. Únicamente se envió un correo y automáticamente enviaron las credenciales. The Guardian tiene un apartado que se llama "Explore", donde se busca el contenido. 
El siguiente paso fue importar las librerías y leer el json. 
#Se construye un DataFrame. 
#Se renombra la columna de 'webTitle' a 'Title'.
#Se crea una columna nueva para clasificar la información y determinar si el título tiene la(s) palabra(s): Women, Girl o Woman. Se integró .lowe() para que reconociera las minúsculas y además una expresión para que identificara la palabras. El resultado en la columna es un boleano: True or False.
#Se exporta la información a un archivo .csv para que toda esta información consolidada permanezca.
#Se define un nuevo Data Frame con sólo dos columnas para el análisis general. 
#Se lee el .csv generado con la información de los feeds. 
#Finalmente se concatenan los dos Data Frames para obtener un consolidado. 
#Se obtiene el número total de "True" (si en los títulos aparece la(s) palabra(s) Women, Girl, Woman). Al ser pocos resultados, busqué la categoría (o tema) directamente en el medio y con el título. Los próximos pasos de este proyecto incluirán la categorización automatizada de los resultados. Por ejemplo: Violencia, Tecnología, Ciencia, Deportes. 

RSS feed (parsing) 
#Los blogs que se utilizaron para este análisis fueron:  
Business Insider (Negocios)
Mashable (Tecnología y Social Media) 
Wired Science (Tecnología. Específicamente Ciencia)
Yahoo news (Popular)

#Se importa la librería feedparser se utilizarán para leer y hacer el "parsing" del feed de distintos tipos de blogs.
#También se importa pandas para el trabajo con los data frames. 
#Se buscan los keys del diccionario para conocer si existen títulos de las entradas. 
#Se crea un data frame nuevo con una columna con los títulos de la entrada.  
#Se crea una columna nueva para clasificar la información y determinar si el título tiene la(s) palabra(s): Women, Girl o Woman. Se integró .lowe() para que reconociera las minúsculas y además una expresión para que identificara la palabras. El resultado en la columna es un boleano: True or False.
#A partir de este momento el proceso se repite con los blogs Mashable, Wired y Yahoo. Se recopila la información y se limpia el data set. 
#Se hace un data frame concatenado con todos los data frames realizados. El arreglo es el primer argumento.
#Del data frame consolidado, se obtiene el número total de "True" (si en los títulos aparece la(s) palabra(s) Women, Girl, Woman). Al ser pocos resultados, busqué la categoría (o tema) directamente en el medio y con el título. 
#Se exporta la información al archivo .csv para poder manipularlo y concatenarlo en el file de la API.

En la carpeta del proyecto se incluyen los csv. 

RESULTADOS: 

Del DATAFRAME de la API se rastrearon en el periodo de tiempo 9 resutados, de los cuales 5 de ellos estaban relacionados con violencia contra las mujeres. File: Project_Women_API.csv
Del DATAFRAME de las lecutras de los feed RSS se rastrearon 110 resultados de noticias generales, de los cuales, en los títulos, las mujeres sólo fueron mencionadas en 4 veces (en el hábito de ciencia, tecnología, noticias generales), y las cuatro noticias eran relacionadas a violencia.Project_Women_Feed.csv

