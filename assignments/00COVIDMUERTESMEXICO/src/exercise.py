from matplotlib import pyplot as plt
def grafico_muertes_hombres():
    print("Grafico de barras hombres")

    edad=["0-4", "5-9", "10-14", "15-19", "20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90-94","95-99"]
    muertes=[257, 0, 0, 195, 711, 1835, 3307, 5775, 8499, 13256, 16464, 20465, 23105, 23514, 21129, 16763, 11506, 6527, 2260, 563]
    xs = [i for i,_ in enumerate(edad)]
    plt.bar(xs, muertes)

    plt.ylabel("# de muertes")
    plt.title("Muertes de covid (hombre)")
    plt.xticks([i for i,_ in enumerate(edad)], edad)

    plt.savefig('grafico_muertes_hombres.png')
    plt.show()
    
def grafico_muertes_mujeres():
    print("Grafico de barras mujeres")

    edad=["0-4", "5-9", "10-14", "15-19", "20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90-94","95-99"]
    muertes=[215, 0, 0, 218, 489, 1112, 1728, 2678, 3971, 6750, 8870, 12571, 15034, 15466, 13786, 11295, 7840, 4477, 1838, 449]
    xs = [i for i,_ in enumerate(edad)]
    plt.bar(xs, muertes)

    plt.ylabel("# de muertes")
    plt.title("Muertes de covid (mujer)")
    plt.xticks([i for i,_ in enumerate(edad)], edad)

    plt.savefig('grafico_muertes_mujeres.png')
    plt.show()

def main():
    #escribe tu código abajo de esta línea
    reg = "si" 
    print('')
    print('-------------------------------------------')
    print('Base de datos COVID-19 México')
    print(' ')
    nomb = input('¿Cuál es tu nombre? ')
    print ('Hola ' + str(nomb))
    print('Bienvenid@ a la base de datos de COVID-19 México, por favor eliga el tipo de datos que desea consultar.')
    print (' ')
    while (reg == "si"): 
        print("1.-Número de Muertes por COVID-19. ")
        #dentro de este habrán mas opciones para mostrar la grafica de definciones, a nivel nacional o los puros datos por estado
        print('2.- Número de casos activos.')
        #también da la opción de ver los datos a nivel estatal o nacional
        print("3.- Semáforo Epidemiológico.")
        #también da la opción de ver los datos a nivel estatal o nacional
        print("4.- Sintomas de COVID-19.")
        #en este apartado entran las preguntas y dependiendo de cuantas contestes te dice da recomendaciones de que hacer
        print("5.- Protegerse y prevenir el COVID-19.")
        #se da una lista de recomendaciones de como ciudarse pa q no te de cobis 
        num=int(input("Teclee el número que coorresponda al apartado que sea de su interés: "))

        if num == 1 :
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Número de Muertes por COVID-19.')
            print('')
            print('El numero de muertes acumuladas en México desde Marzo 2020 hasta Octubre 2021 es de 284,295.') 
            g = input('¿Desea ver las graficas muertes de hombres y mujeres por edades? (si o no)')
            if g == 'si': 
                grafico_muertes_hombres()
                grafico_muertes_mujeres()
                reg = input('¿Desea volver al menú principal? ') 
        

        elif num == 2 :
            #num casos activos 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de número de casos activos.')
            print('')
            print('- A nivel nacional desde Marzo 2020 hasta octubre 2021 hay 3,767,758 casos confirmados.')
            print('- A nivel nacional desde Marzo 2020 hasta octubre 2021 hay 3,986,789 casos estimados.')
            print('')
            reg = input('¿Desea volver al menú principal? ')

        elif num == 3 :
            #semaforos 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Semáforo Epidemiológico.')
            print('')
            print('¿A que nivel te gustaría consultar los datos? ')
            print(' ')
            print(' 1.- Rojo ')
            print(' 2.- Naranja ')
            print(' 3.- Amarillo ')
            print(' 4.- Verde ') 
            num3= int(input())
            if num3 == 1:
                #matriz estados rojos
                print ('Los estados en semáforo rojo son: ')
                rojo = ['Ninguno']
                print (rojo)
                reg = input('¿Desea volver al menú principal? ')
            elif num3 == 2: 
                #matriz estados naranja
                print ('Los estados en semáforo naranja son: ')
                naranja = ['Baja California']
                print (naranja)
                reg = input('¿Desea volver al menú principal? ')
            elif num3 == 3:
                #matriz estados amarillo
                print ('Los estados en semáforo amarillo son: ')
                amarilla = ['Chihuahua, Coahuila, Jalisco, Aguascalientes, Colima, Guanajuato, Querétaro, Morelos, Tabasco, Campeche, Yucatán']
                print (amarilla)
                reg = input('¿Desea volver al menú principal? ')
            elif num3 == 4 : 
                #matriz estados verdes
                print ('Los estados en semáforo verde son: ')
                verde = ['Sonora, Baja California sur, Sinaloa, Durango, Nayarit, Zacatecas, San Luis Potosí, Nuevo León, Tamaulipas, Veracruz, Puebla, Tlaxcala, Hidalgo, Estado de México, Ciudad de México, Michoacán, Guerrero, Oaxaca, Chiapas, Quintana Roo']
                print (verde)
                reg = input('¿Desea volver al menú principal? ')
            else: 
                print ('Por favor ingrese una opción valida.')

        elif num == 4 :
            #sintomas, agregar un contador por cada pregunta 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Síntomas.')
            print('')
            print('Selecciona que quieres hacer: ')
            print(' ')
            print(' 1.- Ver sintomas.  ')
            print(' 2.- Tomar test. ')
            num4= int(input())

            if num4 == 1 :
                print('-----------------------------------------------------------------')
                print('De acuerdo con la OMS, los síntomas de COVID-19 son: ')
                print('Los síntomas más habituales:')
                print('Fiebre, Tos, Cansancio, Pérdida del gusto o del olfato')
                print('')
                print('Los síntomas menos habituales')
                print('Dolor de garganta, dolor de cabeza, molestias y dolores, ')
                print('diarrea, Erupción cutánea o pérdida del color de los dedos')
                print('de las manos o los pies y Ojos rojos o irritados.')
                print('')
                print('Los síntomas mas serios:')
                print('Dificultad para respirar, pérdida de movilidad o del habla')
                print('o sensación de confusión y dolor en el pecho.')
                print('')
                #FALTA: matrices que digan los sintomas 
                reg = input('¿Desea volver al menú principal? ')

            elif num4== 2:
                #hacer contador con las respuestas que vaya dando la persona
                print('Por favor responda las siguientes preguntas:') 
                print('')
                print('En los últimos 10 días, ¿Has presentado uno o mas')
                print('de los siguientes signos o síntomas? responde "si" o "no"')
                cont=0
                respuesta= 'si'
                print('-----------------------------------------------------------------')
                pregunta1=input('Temperatura mayor a 37.5 grados centigrados: ')
                if pregunta1=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta2=input('Dolor de cabeza intenso: ')
                if pregunta2=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta3=input('Tos de reciente aparición: ')
                if pregunta3=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta4=input('Dificultad para respirar: ')
                if pregunta4=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta5=input('Dificultad para percibir olores: ')
                if pregunta5=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta6=input('Dificultad para percibir sabores: ')
                if pregunta6=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta7=input('Dolor muscular: ')
                if pregunta7=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta8=input('Dolor en las articulaciones: ')
                if pregunta8=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta9=input('Dolor de garganta o al tragar: ')
                if pregunta9=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                pregunta10=input('Irritación en los ojos(ardor y/o comezón: ')
                if pregunta10=='si' :
                    cont = cont+1
                print('-----------------------------------------------------------------')
                print (cont)
                if cont<=4:
                    print('El número de sintomas que usted presenta es igual a: '+str(cont))
                    print('')
                    print('La probabilidad de que padezcas de COVID-19 es baja,')
                    print('pero eso no significa que debas de bajar la guardia,')
                    print('aquí te dejamos algunas recomendaciones a seguir:')
                    print('')
                    print('- Lavarse las manos con agua y con jabón como pimpon.')
                    print('- Guarde al menos 1 metro de distancia entre usted y otras personas. Cuanto mayor distancia, mejor.')
                    print('- Convierta el uso de la mascarilla en una parte normal de su interacción con otras personas.')
                    print('- Evite ir a lugares bastante concurridos.')
                    print('')
                elif cont>4:
                    print('El número de sintomas que usted presenta es igual a:'+str(cont))
                    print('')
                    print('La probabilidad de que padezcas de COVID-19 es intermedia,')
                    print('aquí le dejamos algunas recomendaciones a seguir:')
                    print('')
                    print('- Evitar el contacto con otras personas')
                    print('- Acudir al medico')
                    print('')
                else:
                    print('-----------------------------------------------------------------')
                reg = input('¿Desea volver al menú principal? ')

        
        elif num == 5 :
            #recomendaciones de prevención 
            print('-----------------------------------------------------------------')
            print('Haz seleccionado el apartado de Protegerse y prevenir el COVID-19.')
            print('')
            print('A continuación se mostrarán tips emitidos por la OMS (Organización Mundial de la Salud')
            print('Por favor eliga que apartado desea consultar: ')
            print(' ')
            print('1. Qué hacer para mantenerse y mantener a los demás a salvo del COVID-19.')
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
                reg = input ('¿Quieres volver al menú principal? ')
               
            elif num5 == 2:
                print('-----------------------------------------------------------------')
                print('Indicaciones básicas sobre la manera de ponerse la mascarilla:')
                print('')
                print('- Lávese las manos antes de ponerse la mascarilla, y también antes y después de quitársela y cada vez que la toque.')
                print('- Asegúrese de que le cubre la nariz, la boca y el mentón.')
                print('- Cuando se quite la mascarilla, guárdela en una bolsa de plástico limpia.')
                print('- No utilice mascarillas con válvulas.')
                print('')
                reg = input ('¿Quieres volver al menú principal? ')

            elif num5 == 3:
                print('-----------------------------------------------------------------')
                print('Normas básicas de la buena higiene:')
                print('')
                print('- Lávese periódica y cuidadosamente las manos con un gel hidroalcohólico o con agua y jabón. ')
                print('- Evite tocarse los ojos, la nariz y la boca. ')
                print('- Al toser o estornudar cúbrase la boca y la nariz con el codo flexionado o con un pañuelo.')
                print('- Limpie y desinfecte frecuentemente las superficies, en particular las que se tocan con regularidad.')
                print('')
                reg = input ('¿Quieres volver al menú principal? ')

            else:
                print('Por favor eliga una opción valida.')


        else :
        #que te vuelva a preguntar hasta que contestes un numero
            print('Por favor ingrese una opción valida.')
            reg = input('¿Desea volver al menu principal? ')
        
        if reg == 'no' :
            print('Recuerde seguir las indicaciones emitidas por las autoridades')
            print('para cuidarse a usted y sus seres queridos. ')
            print ('Muchas gracias por usar nuestro programa c:')
            print('A fregar a toda su mauser programación <3')
    

if __name__=='__main__':
    main()
