"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd



def ingest_data():

    df=pd.read_table("clusters_report.txt",header=None)
    #df.columns=["cluster","cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]

    i=0
    df.drop([ 0,1,2],axis=0, inplace=True)
    tabla=[]
    fila = {}
    for i in range(len(df)):
        #separar las palabras por espacios
        line=df.iloc[i][0].strip().split()
        if line[0].isnumeric():
            if len(fila)>0:
                tabla.append(fila)
            fila={}
            fila["cluster"]=int(line[0])
            fila["cantidad_de_palabras_clave"]=int(line[1])
            fila["porcentaje_de_palabras_clave"]=float(line[2].replace(",","."))
            fila["principales_palabras_clave"]=" ".join(line[4:])
        else:
            fila["principales_palabras_clave"]+=" "+" ".join(line)
            if fila["principales_palabras_clave"][-1]==".":
                fila["principales_palabras_clave"]=fila["principales_palabras_clave"][:-1]
    if len(fila) > 0:
        tabla.append(fila)
    df=pd.DataFrame(tabla)
    #print(df)
    return df
#ingest_data()