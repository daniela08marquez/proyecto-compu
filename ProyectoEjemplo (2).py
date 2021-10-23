#Librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def leerExcel():
    tabla = pd.read_excel("tiendaabarrotes.xlsx")
    return tabla

def graficaLinea(etiqueta, valores, titulo, tituloejex, tituloejey, tipo, pin, color, rotacion):
    plt.plot(etiqueta, valores, color=color, linestyle=tipo, marker=pin)
    plt.title(titulo)
    plt.xlabel(tituloejex)
    plt.ylabel(tituloejey)
    plt.xticks(rotation=rotacion)
    plt.legend(['ventas sucursal'])
    plt.show()

def graficaBarras(etiqueta, valores, titulo, tituloejex, tituloejey, color, rotacion):
    barlist=plt.bar(etiqueta, valores, color=color, edgecolor='black')
    plt.grid(color='gray', linestyle='--', linewidth=2, axis='y', alpha=0.2)
    plt.title(titulo)
    plt.xlabel(tituloejex)
    plt.ylabel(tituloejey)
    plt.xticks(rotation=rotacion)
    plt.show()

def graficaPie(etiqueta, valores, titulo):
    fig, x=plt.subplots()
    x.pie(valores, labels=etiqueta, autopct='%1.1f%%', shadow=True, startangle=90)
    x.axis('equal')
    plt.title(titulo)
    plt.show()

#proceso
opcion = 0
while opcion <=  4:
    #Este es el menú principal del sistema
    print("-------------------MENÚ--------------------")
    print("Reporte de ventas de sucursal ----------- 1")
    print("Reporte de ventas por día --------------- 2")
    print("Reporte de ventas por hora -------------- 3")
    print("Reporte de tipo de pago   --------------- 4")
    print("Para salir  ----------------------------- 5")
    #Aquí recibe la opción a elegir 
    opcion = int(input("Teclea la opción: "))

    if opcion < 0:
        print("Opción invalida")
        opcion=0
    
    elif opcion == 1:
        print("Reporte de ventas de sucursal")
        tabla = leerExcel()
        resultado=tabla.groupby('NOMBRE_COMERCIO', as_index=False).agg({"IMPORTE_TOTAL": "sum"})
        sucursal=resultado["NOMBRE_COMERCIO"]
        ventas = resultado["IMPORTE_TOTAL"]
        print(f"La media de las venta por Sucursal es:{np.mean(ventas)}")
        print(f"El valor máximo de las ventas por Sucursal es:{np.max(ventas)} ")
        print(f"El valor mínimo de las ventas por Sucursal es:{np.min(ventas)}")
        graficaLinea(sucursal, ventas, "Reporte de ventas de sucursal", "Sucursal", "Ventas", "--","o","red",20)
    elif opcion == 2:
        print("Reporte de ventas por día")
        tabla = leerExcel()
        resultado=tabla.groupby('DIA_SEMANA', as_index=False).agg({"IMPORTE_TOTAL": "sum"})
        dia=resultado["DIA_SEMANA"]
        ventas=resultado["IMPORTE_TOTAL"]
        graficaBarras(dia, ventas, "Reporte de ventas por día", "día","ventas", "pink",20 )
    elif opcion == 3:
        print("Reporte de ventas por hora")
        tabla = leerExcel()
        resultado=tabla.groupby('HORA', as_index=False).agg({"IMPORTE_TOTAL": "sum"})
        hora=resultado["HORA"]
        ventas=resultado["IMPORTE_TOTAL"]
        graficaLinea(hora, ventas, "Reporte de ventas por1 hota", "Hora", "Ventas", "-","*","blue",0)
    elif opcion == 4:
        print("Reporte tipo de pago")
        tabla = leerExcel()
        resultado=tabla.groupby(["FORMA_PAGO"])["CANTIDAD"].count().reset_index()
        forma_pago= resultado["FORMA_PAGO"]
        cantidad=resultado["CANTIDAD"]
        graficaPie(forma_pago, cantidad, "Reporte tipo de pago")

#Tomó otra opción mayor a 4 para salir
print("Bye")
