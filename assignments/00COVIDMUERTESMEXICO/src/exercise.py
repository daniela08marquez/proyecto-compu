def semaforos():
    #aquí van en que semaforo se encuentran los estados 
  sinaloa = "verde"  
def main():
    #escribe tu código abajo de esta línea
    pass
    reg = "si" 
    print('-------------------------------------------')
    print('Base de datos COVID-19 México')
    print(' ')
    nomb = input('¿Cual es tu nombre? ')
    print ('Hola ' + str(nomb))
    print('Bienvenid@ a la base de datos de COVID-19 México, por favor eliga el tipo de datos que le gustaría consultar.')
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
        print("5.- Protegerse y prevenir el COVID-19")
        #se da una lista de recomendaciones de como ciudarse pa q no te de cobis 
        num=int(input("Teclee el numero que coorresponda al apartado que sea de su interés: "))

        if num == "1" :
            print('¿A que nivel te gustaría consultar los datos?')
            print('')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num1= int(input())
            if num1 == 1 : 
                #numero de muertes 
                print('El numero de muertes acumuladas en México de Marzo 2020 a Octubre 2021 es de 284,295') 
                #aqui va la grafica de muertes 
            elif num1 == 2: 
                print ('Seleccione su estado')
                print ('')
            else: 
                print('')

        elif num == 2 :
            #num casos activos 
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num2= int(input())

        elif num == 3 :
            #semaforos 
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num3= int(input())

        elif num == 4 :
            #sintomas, agregar un contador por cada pregunta 
            print('Selecciona que quieres hacer: ')
            print(' ')
            print(' 1.- Ver sintomas  ')
            print(' 2.- Tomar test  ')
            num4= int(input())
        
        elif num == 5 :
            #recomendaciones de prevención 
            print('A continuación se mostrarán tips emitidos por la OMS (Organización Mundial de la Salud')
            print('para prevenir el contagio ')
        else :
        #que te vuelva a preguntar hasta que contestes un numero
            print('Porfavor ingrese una opcion valida')
            #FALTANTE: poner para que se regrese al inicio
            
    


if __name__=='__main__':
    main()
