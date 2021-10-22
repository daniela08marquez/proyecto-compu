def main():
    #escribe tu código abajo de esta línea
    reg = "si" 
    print('-------------------------------------------')
    print('Base de datos COVID-19 México')
    print(' ')
    nomb = input('¿Cual es tu nombre? ')
    print ('Hola ' + str(nomb))
    print('Bienvenid@ a la base de datos de COVID-19 México, por favor eliga el tipo de datos que le gustaría consultar.')
    print (' ')
    while (reg == "si"): 
        print("1.-Numero de Muertes por COVID-19. ")
        #dentro de este habrán mas opciones para mostrar la grafica de definciones, a nivel nacional o los puros datos por estado
        print('2.- Numero de casos activos.')
        #también da la opción de ver los datos a nivel estatal o nacional
        print("3.- Semaforo Epidemologico.")
        #también da la opción de ver los datos a nivel estatal o nacional
        print("4.- Sintomas de COVID-19.")
        #en este apartado entran las preguntas y dependiendo de cuantas contestes te dice da recomendaciones de que hacer
        print("5.- Protegerse y prevenir el COVID-19.")
        #se da una lista de recomendaciones de como ciudarse pa q no te de cobis 
        num=int(input("Teclee el numero que coorresponda al apartado que sea de su interés: "))

        if num == "1" :
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Numero de Muertes por COVID-19.')
            print('¿A que nivel te gustaría consultar los datos?')
            print('')
            print(' 1.- Nacional ')
            print(' 2.- Estatal ')
            num1= int(input())
            if num1 == 1 : 
                #numero de muertes 
                print('El numero de muertes acumuladas en México de Marzo 2020 a Octubre 2021 es de 284,295') 
                #aqui va la grafica de muertes 
                reg = int ('¿Desea volver al menu principal? ')
            elif num1 == 2: 
                print ('Seleccione su estado')
                print ('')
                reg = int ('¿Desea volver al menu principal? ')
            else: 
                print('Selecione una opcion valida')
            

        elif num == 2 :
            #num casos activos 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Numero de casos activos.')
            print('A nivel nacional desde Marzo 2020 hasta octubre 2021 hay 3,767,758 casos confirmados')
            print('A nivel nacional desde Marzo 2020 hasta octubre 2021 hay 3,986,789 casos estimados')
            num2= int(input())

        elif num == 3 :
            #semaforos 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Semaforo Epidemologico.')
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Rojo ')
            print(' 2.- Naranja ')
            print(' 3.- Amarillo ')
            print(' 4.- Verde ') 
            num3= int(input())
            if num3 == 1:
                #matriz estados rojos
                print ('Los estados en semaforo rojo son: ')
                rojo = ['Ninguno']
                print (rojo)
                reg = input('¿Desea volver al menu principal? ')
            elif num3 == 2: 
                #matriz estados naranja
                print ('Los estados en semaforo naranja son: ')
                naranja = [e1]
                print (naranja)
                reg = input('¿Desea volver al menu principal? ')
            elif num3 == 3:
                #matriz estados amarillo
                print ('Los estados en semaforo amarillo son: ')
                amarilla = ['e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12']
                reg = input('¿Desea volver al menu principal? ')
            elif num3 == 4 : 
                #matriz estados verdes
                print ('Los estados en semaforo verde son: ')
                amarilla = ['e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32']
                reg = input('¿Desea volver al menu principal? ')
            else: 
                print ('Porfavor ingrese una opcion valid')

        elif num == 4 :
            #sintomas, agregar un contador por cada pregunta 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Síntomas.')
            print('Selecciona que quieres hacer: ')
            print(' ')
            print(' 1.- Ver sintomas.  ')
            print(' 2.- Tomar test. ')
            num4= int(input())

            if num4 == 1 :
                print('-----------------------------------------------------------------')
                print('De acuerdo con la OMS, los sintomas de COVID-19 son los siguientes:')
                sintomas=['- Fiebre', '- Tos', '- Cansancio', '- Pérdida del gusto o del olfato']
                #FALTA: matrices que digan los sintomas 

            elif num4== 2:
                #hacer contador con las respuestas que vaya dando la persona
                print('Porfavor responda las preguntas siguientes:') 
                print('')
                print('En los últimos 10 días, ¿Has presentado uno o')
                print('más de los siguientes signos o síntomas? responde "si" o "no"')
                print('-----------------------------------------------------------------')
                pregunta1=input('Temperatura mayor a 37.5 grados centigrados: ')
                cont=0
                respuesta= "si" or "SI" or "Si"
                for r1 in pregunta1 :
                    if r1==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta2=input('Dolor de cabeza intenso: ')
                for r2 in pregunta2 :
                    if r2==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta3=input('Tos de reciente aparición: ')
                for r3 in pregunta3 :
                    if r3==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta4=input('Dificultad para respirar: ')
                for r4 in pregunta4 :
                    if r4==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta5=input('Dificultad para percibir olores: ')
                for r5 in pregunta5 :
                    if r5==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta6=input('Dificultad para percibir sabores: ')
                for r6 in pregunta6 :
                    if r6==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta7=input('Dolor muscular: ')
                for r7 in pregunta7 :
                    if r7==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta8=input('Dolor en las articulaciones: ')
                for r8 in pregunta8 :
                    if r8==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta9=input('Dolor de garganta o al tragar: ')
                for r9 in pregunta9 :
                    if r9==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta10=input('Irritación en los ojos(ardor y/o comezón: ')
                for r10 in pregunta10 :
                    if r10==respuesta :
                        cont = cont+1
                print('-----------------------------------------------------------------')
                if cont<=4:
                    print('El número de sintomas que usted presenta es igual a:'+str(cont))
                    print('La probabilidad de que padezcas de COVID-19 es baja, pero')
                    print('eso no significa que debas de bajar la guardia, aquí te dejamos')
                    print('algunas recomendaciones a seguir:')
                    print('-Lavarse las ')
                    print('- Guarde al menos 1 metro de distancia entre usted y otras personas. Cuanto mayor distancia, mejor.')
                    print('- Convierta el uso de la mascarilla en una parte normal de su interacción con otras personas.')
                    print('- Evite ir a lugares bastante concurridos.')
                    print('')
                    reg = input ('¿Quieres volver al menú princial?')
                elif cont<=7:
                    print('El número de sintomas que usted presenta es igual a:'+str(cont))
                    print('La probabilidad de que padezcas de COVID-19 es intermedia,')
                    print('aquí le dejamos algunas recomendaciones a seguir:')
                    print('Evitar el contacto con otras personas')


            else:
                print('-----------------------------------------------------------------')

        
        elif num == 5 :
            #recomendaciones de prevención 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Protegerse y prevenir el COVID-19.')
            print('')
            print('A continuación se mostrarán tips emitidos por la OMS (Organización Mundial de la Salud')
            print('Porfavor eliga que apartado desea consultar: ')
            print(' ')
            print('1. Qué hacer para mantenerse y mantener a los demás a salvo de la COVID-19.')
            print('2. Indicaciones básicas sobre la manera de ponerse la mascarilla.')
            print('3. Normas básicas de la buena higiene')
            print(' ')
            num5=int(input())

            if num5 == 1:
                print('-----------------------------------------------------------------')
                print('Qué hacer para mantenerse y mantener a los demás a salvo de la COVID-19:')
                print('')
                print('- Guarde al menos 1 metro de distancia entre usted y otras personas. Cuanto mayor distancia, mejor.')
                print('- Convierta el uso de la mascarilla en una parte normal de su interacción con otras personas.')
                print('- Evite ir a lugares bastante concurridos.')
                print('')
                #FALTANTE:Poner para que pregunte si se quiere regresar al inicio
                reg = input ('¿Quieres volver al menú princial?')
               
            elif num5 == 2:
                print('-----------------------------------------------------------------')
                print('Indicaciones básicas sobre la manera de ponerse la mascarilla:')
                print('')
                print('- Lávese las manos antes de ponerse la mascarilla, y también antes y después de quitársela y cada vez que la toque.')
                print('- Asegúrese de que le cubre la nariz, la boca y el mentón.')
                print('- Cuando se quite la mascarilla, guárdela en una bolsa de plástico limpia.')
                print('- No utilice mascarillas con válvulas.')
                print('')
                #FALTANTE:Poner para que pregunte si se quiere regresar al inicio
                reg = input ('¿Quieres volver al menú princial?')

            elif num5 == 3:
                print('-----------------------------------------------------------------')
                print('Normas básicas de la buena higiene:')
                print('')
                print('- Lávese periódica y cuidadosamente las manos con un gel hidroalcohólico o con agua y jabón. ')
                print('- Evite tocarse los ojos, la nariz y la boca. ')
                print('- Al toser o estornudar cúbrase la boca y la nariz con el codo flexionado o con un pañuelo.')
                print('- Limpie y desinfecte frecuentemente las superficies, en particular las que se tocan con regularidad.')
                print('')
                #FALTANTE:Poner para que pregunte si se quiere regresar al inicio
                reg = input ('¿Quieres volver al menú princial?')
                #FALTANTE:poner funcion para que finalice el programa 

            else:
                print('Por favor eliga una opción valida.')


        else :
        #que te vuelva a preguntar hasta que contestes un numero
            print('Porfavor ingrese una opcion valida')
            #FALTANTE: poner para que se regrese al inicio
            
    


if __name__=='__main__':
    main()
