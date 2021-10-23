#Librerías
import pandas as pd
import matplotlib.pyplot as plt

#funciones

#Pie
def graficapie (etiqueta, valores, titulo):
    x = plt.subplot ()
    x.pie (valores, labels=etiqueta, autopct = '%1.1f%%', shadow = True, startangle=90)
    x.axis ('equal')
    plt.title (titulo)
    
    #Salida
    plt.show ()

#Lines
def graficalineas (etiqueta, valores, titulo, ejex, ejey):
    plt.style.use ('dark_background')   
    plt.plot(listaNombres, listaSalarios, color='pink', linestyle='--', marker='o')
    
    plt.title (titulo)
    plt.xticks (rotation=30)
    plt.xlabel (ejex)
    plt.ylabel (ejey)

#Barras
def graficabarra (etiqueta, valores, titulo, ejex, ejey):
    plt.style.use ('dark_background')                               #Cambia el color del fondo
    barlist=plt.bar(listaNombres, listaSalarios, color= 'pink' , edgecolor= 'white')

    plt.title (titulo)
    plt.xticks (rotation=30)
    plt.xlabel (ejex)
    plt.ylabel (ejey)


    #Salida
    plt.show ()

#Entrada
tabla = pd.read_excel("vendedores.xlsx")                        #Lee el excel

#Proceso
tablaNorte = tabla.groupby ("REGION").get_group ("NORTE")        #Agrupa por región norte
listaNombres = tablaNorte ["NOMBRE"]
listaSalarios = tablaNorte ["SALARIO"]

graficapie (listaNombres, listaSalarios, "Gráfica Salarios Norte")

graficalineas (listaNombres, listaSalarios, "Gráfica Salarios Norte", "NOMBRES", "SALARIOS")

graficabarra (listaNombres, listaSalarios, "Gráfica Salarios Norte", "NOMBRES", "SALARIOS")

