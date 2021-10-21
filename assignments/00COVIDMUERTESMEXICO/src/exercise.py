def main():
    #escribe tu código abajo de esta línea
    pass
    reg = "si" 
    print('-------------------------------------------')
    print('Base de datos COVID-19 México')
    print(' ')
    nomb = input('¿Cual es tu nombre? ')
    print ('Hola ' + str(nomb))
    print ('Este programa prensetara datos sobre los casos por covid, y las muertes por covid  en México desde Marzo 18 2020 hasta Octubre 18 2021')
    print (' ')
    while (reg == "si"): 
        print("1.-Numero de Muertes por covid ")
        #dentro de este habrán mas opciones para mostrar la grafica de definciones, a nivel nacional o los puros datos por estado
        print('2.- Numero de casos activos')
        #también da la opción de ver los datos a nivel estatal o nacional
        print("3.- Semaforo Epidemologico")
        #también da la opción de ver los datos a nivel estatal o nacional
        print("4.- Sintomas de COVID-19")
        #en este apartado entran las preguntas y dependiendo de cuantas contestes te dice da recomendaciones de que hacer
        num=int(input("Teclee el numero que coorresponda al apartado que sea de su interés: "))
        if num == "1" :
            print('¿A que nivel te gustaría consultar los datos?')
            print('')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num1= int(input())
        elif num == 2 :
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num2= int(input())
        elif num == 3 :
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num3= int(input())
        elif num == 4 :
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num4= int(input())
        else :
        #que te vuelva a preguntar hasta que contestes un numero
            print('Porfavor ingrese una opcion valida')
    


if __name__=='__main__':
    main()
