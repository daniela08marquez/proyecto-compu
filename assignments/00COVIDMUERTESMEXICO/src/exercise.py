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
            print('Porfavor eliga que apartado desea consultar: ')
            print(' ')
            print('1. Qué hacer para mantenerse y mantener a los demás a salvo de la COVID-19.')
            print('2. Indicaciones básicas sobre la manera de ponerse la mascarilla.')
            print('3. Normas básicas de la buena higiene')
            print('4. Cómo reforzar la seguridad de su entorno')
            print(' ')
            p_num=int(input())
            if p_num == 1:
                print('-----------------------------------------------------------------')
                print('Qué hacer para mantenerse y mantener a los demás a salvo de la COVID-19:')
                print('')
                print('- Guarde al menos 1 metro de distancia entre usted y otras personas. Cuanto mayor distancia, mejor.')
                print('- Convierta el uso de la mascarilla en una parte normal de su interacción con otras personas.')
                print('- Evite ir a lugares bastante concurridos.')
                print('')
                #FALTANTE:Poner para que se regrese al inicio
            elif p_num == 2:
                print('-----------------------------------------------------------------')
                print('Indicaciones básicas sobre la manera de ponerse la mascarilla:')
                print('')
                print('- Lávese las manos antes de ponerse la mascarilla, y también antes y después de quitársela y cada vez que la toque.')
                print('- Asegúrese de que le cubre la nariz, la boca y el mentón.')
                print('- Cuando se quite la mascarilla, guárdela en una bolsa de plástico limpia.')
                print('- No utilice mascarillas con válvulas.')
                print('')
                #FALTANTE:Poner para que pregunte si se quiere regresar al inicio
            elif p_num == 3:
                print('-----------------------------------------------------------------')
                print('Qué hacer para mantenerse y mantener a los demás a salvo de la COVID-19:')
                print('')
                print('Guarde al menos 1 metro de distancia entre usted y otras personas. Cuanto mayor distancia, mejor.')
                print('Convierta el uso de la mascarilla en una parte normal de su interacción con otras personas.')
                print('Evite ir a lugares bastante concurridos.')
                print('')
            elif p_num == 4:
                print('-----------------------------------------------------------------')
                print('Qué hacer para mantenerse y mantener a los demás a salvo de la COVID-19:')
                print('')
                print('Guarde al menos 1 metro de distancia entre usted y otras personas. Cuanto mayor distancia, mejor.')
                print('Convierta el uso de la mascarilla en una parte normal de su interacción con otras personas.')
                print('Evite ir a lugares bastante concurridos.')
                print('')
            else:
                print('Por favor eliga una opción valida.')


        else :
        #que te vuelva a preguntar hasta que contestes un numero
            print('Porfavor ingrese una opcion valida')
            #FALTANTE: poner para que se regrese al inicio
            
    


if __name__=='__main__':
    main()
