![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Web and API proyect

## Proceso de obtencion de datos

Utilice la API de Banco de Mexico para obtener la historia de los indicadores a analizar
Obtener el Token fue muy sencillo, unicamente te solicita llenar un captcha

Para webscrap utilice la pagina de reuters para obtener los headers y el timestamp de las noticias


## Proceso

Al extraer la informacion de banxico me arrojo una informacion un poco complicada de leer ya que el
json se conformaba por un diccionario de listas con diccionarios.

Logre extraerla y llenar un data frame con los datos

Extraer con webscraping la informacion de la pagina de reuters fue mas sencillo ya que solicite de
manera especifica los headers y el timestamp.


## microanalisis

Se obtuvo el maximo y minimo de el tipo de cambio peso-dolar, y se comparo con la noticia del mismo dia y
dia anterior al dato.
se obtuvieron dos noticias que afectan de manera negativa la paridad del TC.


## Que sigue


Analizar casos especificos de combinaciones de palabras en noticias y observar el comportamiento de los
indicadores por ejemplo, TRUM y CHINA o TRUM y MEXICO como afectan el TC.
