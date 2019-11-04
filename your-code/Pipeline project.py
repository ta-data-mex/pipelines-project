#Import libraries
import pandas as pd

#DATA ACQUISITION
#Cargamos la dirección y la guardamos como un data frame
direccion = "C:/Users/Ramiro Antonio/Documents/ironhack_labs/pipelines-project/your-code/Voto_Nulo_Ags.csv"
voto_nulo = pd.read_csv(direccion, index_col=0)
voto_nulo.head(10)

voto_nulo.describe()


#DATA WRANGLING

#Esta base de datos no dice el nombre del distrito electoral, sólo el ID. Eso no da información, por lo que incluímos los nombres
voto_nulo["Nombre_Distrito"] = ["José María" if x == 1 else "Aguascalientes" if x ==2 else "Hidroaguas" for x in voto_nulo["Distrito"]]
voto_nulo.head(5)

#La variable de Ponderador_OK no nos interesa, por lo que la tiramos
voto_nulo = voto_nulo.drop(["Ponderador_OK"], axis = 1)

#Tipos de casillas.
print(set(voto_nulo['Casilla']))

#Queremos eliminar Casillas Especiales (E1) que están solas, dado que no tienen padrón electoral predeterminado y sesgan análisis
voto_nulo = voto_nulo[voto_nulo.Casilla != "E1"]
print(set(voto_nulo['Casilla']))

#Codificar variable Voto

#Se verifica si la "Voto" tiene valores anómalos (sólo debería haber dos valores)
print(set(voto_nulo["Voto"]))

#En este caso sólo se tienen dos tipos de votos. Sin embargo, en caso hacemos una función para eliminar las valores que no
#sean 1 (Votó) y 2 (No votó)

def LimpiarValoresVoto(df):
    #if (df.Voto != 1) or (df.Voto != 2):
    #   df = df[df.Voto == 1]
    #df.drop(df[(df['Voto'] != 1) and (df['Voto'] != 2)].index)
    #df.drop(df[(df['Voto'] != 1) and (df['Voto'] != 2)].index)
    #df = df.drop(df[df['Voto'] > 2])
    #df = df[df["Voto"].ge(3)]
    df = df[df["Voto"] <= 2]
    return pd.DataFrame(df)

print(LimpiarValoresVoto(voto_nulo))

#Actualmente la variable "Voto" tiene dos valores: 1 y 2. Para facilitar la codificación se desea
#Integrar el código 1 = Votó, 2 = No votó.

#Para hacerlo, vamos a crear una nueva variable que se llame Voto_NoCodificado
voto_nulo["Voto_NoCodificado"] = ["Voto" if x == 1 else "No_voto" for x in voto_nulo["Voto"]]
voto_nulo.head(3)

#Orden de columnas
voto_nulo.columns

voto_nulo = voto_nulo[['Distrito', 'Nombre_Distrito', 'Municipio', 'Seccion', 'Tipo_secc', 'Edad', 'Sexo',
       'Casilla', 'Voto', 'Voto_NoCodificado']]

#String operations

#vamos a pasar todas las mayuscúlas a minúsculas y eliminar los acentos y espacios en la variable "Nombre_Distrito"

voto_nulo["Nombre_Distrito"] = voto_nulo.Nombre_Distrito.str.lower()
voto_nulo["Voto_NoCodificado"] = voto_nulo.Voto_NoCodificado.str.lower()

#Quitar el espacio
voto_nulo["Nombre_Distrito"] = voto_nulo['Nombre_Distrito'].str.replace(" ","")
voto_nulo["Nombre_Distrito"] = voto_nulo['Nombre_Distrito'].str.replace("é","e")
voto_nulo["Nombre_Distrito"] = voto_nulo['Nombre_Distrito'].str.replace("í","i")

print(set(voto_nulo["Nombre_Distrito"]))

#Data Analysis

def Número_de_registros_de_votantes(df):
    return df.count(axis = 0)

print(Número_de_registros_de_votantes(voto_nulo))

def PersonasQueVotaron(df):
    return df.loc[df.Voto == 1, 'Voto'].count()

print(f'La cantidad de votos registrados es {PersonasQueVotaron(voto_nulo)}')

def Porcentaje_PersonasQueVotaron(df):
    return (df.loc[df.Voto == 1, 'Voto'].count())/len(df)*100

print(f'El porcentaje de participación en la Entidad Federativa es {Porcentaje_PersonasQueVotaron(voto_nulo)}')

#Comparación con el promedio nacional. La participación nacional fue de 63.43%.
def Comparacion_ParticipacionNacional(df):
    if (df.loc[df.Voto == 1, 'Voto'].count())/len(df)*100 < 63.43:
        print("En los distritos de esta entidad federativa hubo menor participación que en el promedio nacional")
    else:
        return "En los distritos de esta entidad federativa hubo mayor particiación que en el promedio nacional"

print(Comparacion_ParticipacionNacional(voto_nulo))


#Para saber los votos por sección
def voto_por_seccion(df):
    df_temp= df[df.Voto == 1]
    urbanas = len([x for x in df_temp["Tipo_secc"] if x == "U"])
    rurales = len([x for x in df_temp["Tipo_secc"] if x == "R"])
    mixtas = len([x for x in df_temp["Tipo_secc"] if x == "M"])
    return f'En las secciones urbanas hubo {urbanas} votos. \n En las mixtas hubo {mixtas} votos. \n En las rurales {rurales} votos.'
print(voto_por_seccion(voto_nulo))

#Comparación participación mujeres  y hombres
def batalla_sexos2(df):
    df_temp= df[df.Voto == 1] #Guarda todos los que votaron (antes de df había puesto voto_nulo)
    if df_temp.loc[df_temp.Sexo == "M", "Sexo"].count() > df_temp.loc[df_temp.Sexo == "H", "Sexo"].count():
        print(f'Votaron más mujeres. El porcentaje de mujeres que votó fue {df_temp.loc[df_temp.Sexo == "M", "Sexo"].count()/len(df_temp)*100}')
    else:
        return f'Votaron más hombres. El porcentaje de hombres que votó fue {df_temp.loc[df_temp.Sexo == "H", "Sexo"].count()/len(df_temp)*100}'

print(batalla_sexos2(voto_nulo))

voto_nulo