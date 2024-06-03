import random

def generar_matriz(dimensiones):
    #E: un número entero
    #S: una matriz cuadrada de las dimensiones recibidas
    #R: las dimensiones deben ser enteras mayores o iguales a tres
    if type(dimensiones)!= int:
        return 'Error: las dimensiones deben ser un número entero'
    if dimensiones<3:
        return 'Error: las dimensiones deben ser al menos 3x3'
    matriz=[]
    for fila in range(dimensiones):
        nueva_fila=[]
        for elementos in range(dimensiones):
            nueva_fila+=[0]
        matriz+=[nueva_fila]
    return matriz

def es_vector(vector):
    #E: un vector (lista de numeros)
    #S: True o False
    #R: la entrada sea una lista de longitud mayor o igual a dos y todos sus elementos son numeros

    if type(vector)!=list:
        return False
    if len(vector)<2:
        return False
    return True

def es_matriz(matriz):
    #E: una matriz (lista de listas)
    #S: True o False
    #R: entrada debe ser una lista y sus elementos vectores

    if type(matriz)!=list:
        return False
    i=0
    f=len(matriz)
    longitud=len(matriz[0])
    while i<f:
        if es_vector(matriz[i])!=True or len(matriz[i])!=longitud:
            return False
        i+=1
    return True

def imprimir_matriz(matriz): 
    #E: una matriz
    #S: una matriz con el formato estandar
    #R: debe ser una matriz la entrada
    if es_matriz(matriz) != True:
        return 'Error: no es matriz'
    
    n = len(matriz)
    m = len(matriz[0])
    
    # Imprimir los índices de las columnas
    print("    ", end="")
    for j in range(m):
        print(j, end=" ")
    print()
    
    for i in range(n):
        # Imprimir el índice de la fila
        print(i, end=" | ")
        for j in range(m):
            print(matriz[i][j], end=" ")
        print()

    return None

def colocar_elemento(matriz, elemento, fila, columna):
    #E: una matriz, el elemento a insertar y las coordenadas donde se insertará el elemento
    #S: la matriz con el elemento insertado
    #R: la matriz debe ser una matriz, la fila y la columna deben de estar en las dimensiones de la matriz

    if es_matriz(matriz)!=True:
        return 'Error: no es una matriz'
    if fila>len(matriz)-1 or fila<0: #1 si aja y sin el -1 el len
        return 'Error: la fila no está en el rango aceptado'
    if columna>len(matriz)-1 or columna<0: #1 si aja y sin el -1 el len
        return 'Error: la columna no está en el rango aceptado'

    #fila-=1
    #columna-=1 si es que queremos contar desde el 1 y no desde el cero y entonces en las validaciones le sumamos uno al len
    matriz[fila][columna]=elemento
    return matriz

def llenar_fila(matriz, elemento, fila):
    #E: una matriz, un elemento para llenar y la fila para llenar
    #S: la matriz ya con la fila llena del elemento
    #R: la matriz sea matriz y la fila esté dentro de las dimensiones de la matriz

    if es_matriz(matriz)!=True:
        return 'Error: no es matriz'
    if type(fila)!=int:
        return 'Error: la fila debe ser un entero'
    if fila>len(matriz)-1 or fila<0: #si vamos a trabajarlo contando normal seria uno y sin -1 en len
        return 'Error: la fila no está en el rango aceptado'
    #fila-=1 en caso de aja

    nueva_fila=[]
    for i in range(len(matriz)):
        # Si hay una P, detenerse
        if matriz[fila][i] == "P":
            return matriz
        matriz[fila][i]=elemento
    return matriz

def llenar_columna(matriz, elemento, columna):
    #E: una matriz, un elemento para llenar y la columna para llenar
    #S: la matriz ya con la columna llena del elemento
    #R: la matriz sea matriz y la columna esté dentro de las dimensiones de la matriz

    if es_matriz(matriz) != True:
        return 'Error: no es matriz'
    
    elif type(columna) != int:
        return 'Error: la columna debe ser un entero'
    
    elif columna>len(matriz)-1 or columna<0: #si vamos a trabajarlo contando normal seria uno y mas uno
        return 'Error: la columna no está en el rango aceptado'
    
    #columna-=1 en caso de aja
    for i in range(len(matriz)):

        if matriz[i][columna] == "P":
            return matriz

        matriz[i][columna] = elemento

    return matriz

def validar_cadena_numero(cadena):
    #E: una cadena de caracteres
    #S: un booleano
    #R: la cadena debe ser un número
    
    for letra in cadena:
        if letra != '0' and letra != '1' and letra != '2' and letra != '3' and letra != '4' and letra != '5' and letra != '6' and letra != '7' and letra != '8' and letra != '9':
            return False
    else:
        return True

def usurpacion(matriz):

    #E: una matriz
    #S: la matriz con una casilla usurpada
    #R: la matriz debe ser una matriz

    if es_matriz(matriz) != True:
        return 'Error: no es matriz'
    
    while True:
        fila = random.randint(0, len(matriz)-1)
        columna = random.randint(0, len(matriz)-1)

        if matriz[fila][columna] == "U":
            continue
        elif matriz[fila][columna] == "P":
            matriz[fila][columna] = "U"
            break
        elif matriz[fila][columna] == "I":
            continue
        elif matriz[fila][columna] == "C":
            matriz[fila][columna] = "U"
            break
        else:
            matriz[fila][columna] = "U"
            break
    
def jugar(primera_vez = True, matriz = []):

    #E: N/A
    #S: N/A
    #R: N/A

    print("¡Bienvenido a Solar Punk!")
    print("¡Buena suerte!")

    
    if primera_vez:
        dimensiones = input("Ingrese las dimensiones de la matriz: ")
        dimensiones_validadas = validar_cadena_numero(dimensiones)

        if dimensiones_validadas == False:
            print("Error: las dimensiones deben ser un número.")
            jugar(True, matriz)
        else:
            dimensiones = int(dimensiones)

            if dimensiones < 3:
                jugar(True, matriz)
            else:
                matriz = generar_matriz(dimensiones)
                imprimir_matriz(matriz)
                return matriz
    else:

        cantidad_usurpaciones = random.randint(1, len(matriz)//2)
        for i in range(cantidad_usurpaciones):
            usurpacion(matriz)

        print("¿Qué quieres hacer?")
        print("1. Plantear una iniciativa")
        print("2. Establecer un proyecto")
        print("3. Difundir cultura")
        
        opcion = input("Ingrese el número de la opción que desea: ")
        opcion_validada = validar_cadena_numero(opcion)

        if opcion_validada == False:
            print("Error: la opción debe ser un número.")
            jugar(False, matriz)
        else:
            opcion = int(opcion)

            if opcion == 1:
                
                for iniciativa in range(2):

                    print(f"¿Dónde quieres plantar tu {iniciativa+1} iniciativa?")
                    print("Ingresa coordenadas para plantear una iniciativa.")                

                    fila = input("Fila: ")
                    fila_validada = validar_cadena_numero(fila)

                    columna = input("Columna: ")
                    columna_validada = validar_cadena_numero(columna)

                    if fila_validada == False or columna_validada == False:
                        print("Error: las coordenadas deben ser números.")
                        jugar(False, matriz)
                    else:
                        colocar_elemento(matriz, "I", int(fila), int(columna))
                        imprimir_matriz(matriz)
                    

            elif opcion == 2:
                
                print("¿Dónde quieres establecer tu proyecto?")
                print("Ingresa coordenadas para establecer un proyecto.")

                fila = input("Fila: ")
                fila_validada = validar_cadena_numero(fila)

                columna = input("Columna: ")
                columna_validada = validar_cadena_numero(columna)

                if fila_validada == False or columna_validada == False:
                    print("Error: las coordenadas deben ser números.")
                    jugar(False, matriz)
                else:
                    colocar_elemento(matriz, "P", int(fila), int(columna))
                    imprimir_matriz(matriz)

                

            elif opcion == 3:
                
                probabilidad = random.randint(1, 3)
                # 1: Llena una fila de cultura vertical
                # 2: Llena una columna de cultura horizontal
                # 3: No ha podido difundir cultura

                if probabilidad == 1:
                    
                    print("¡Has difundido cultura de forma vertical!")
                    print("¿En qué fila quieres difundir cultura?")
                    fila = input("Fila: ")
                    fila_validada = validar_cadena_numero(fila)

                    if fila_validada == False:
                        print("Error: la fila debe ser un número.")
                        jugar(False, matriz)
                    else:
                        llenar_fila(matriz, "C", int(fila))
                        imprimir_matriz(matriz)
                
                elif probabilidad == 2:
                        
                        print("¡Has difundido cultura de forma horizontal!")
                        print("¿En qué columna quieres difundir cultura?")
                        columna = input("Columna: ")
                        columna_validada = validar_cadena_numero(columna)
    
                        if columna_validada == False:
                            print("Error: la columna debe ser un número.")
                            jugar(False, matriz)

                        else:
                            llenar_columna(matriz, "C", int(columna))
                            imprimir_matriz(matriz)
                
                else:
                    print("¡No has podido difundir cultura!")
                    imprimir_matriz(matriz)
    
            else:
                print("Error: la opción debe ser un número entre 1 y 3.")
                jugar(False, matriz)
        
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] == "I":
                    matriz[i][j] = "P"

        for i in range(len(matriz)):
            if matriz[i].count("P") == len(matriz) or matriz[i].count("U") == len(matriz):
                print("¡Has perdido!")
                return True
        
        return matriz
            
        


def tutorial():

    # E: N/A
    # S: N/A
    # R: N/A

    print("¡Bienvenido al tutorial de Solar Punk!")
    print("En Solar Punk, debes sobrevivir en un mundo post-apocalíptico.")
    print("Para sobrevivir, debes recolectar recursos y construir edificaciones.")
    print("¡Buena suerte!")
    
def instrucciones_solar_punk():
    # E: N/A
    # S: N/A
    # R: N/A

    print("Instrucciones sobre Solar Punk")
    print("Solar Punk es un juego de estrategia en el que debes sobrevivir en un mundo post-apocalíptico.")
    print("El objetivo del juego es sobrevivir el mayor tiempo posible.")
    print("Para sobrevivir, debes recolectar recursos y construir edificaciones.")
    print("¡Buena suerte!")

def informacion_pueblos_originarios():
    # E: N/A
    # S: N/A
    # R: N/A

    print("Información sobre pueblos originarios")
    print("Los pueblos originarios son comunidades que han habitado un territorio por cientos o miles de años.")
    print("En Costa Rica, los pueblos originarios son los bribri, cabécar, maleku, ngäbe y naso.")
    print("Los pueblos originarios han sido desplazados y discriminados por la sociedad costarricense.")
    print("¡Es importante conocer y respetar a los pueblos originarios!")

def informacion_conflicto_cabaga():
    # E: N/A
    # S: N/A
    # R: N/A

    print("Información sobre el conflicto de Cabagra")
    print("El conflicto de Cabagra es un conflicto territorial entre los pueblos bribri y cabécar y el Estado costarricense.")
    print("Los pueblos bribri y cabécar reclaman la devolución de sus tierras ancestrales.")
    print("El Estado costarricense ha desatendido las demandas de los pueblos bribri y cabécar.")
    print("¡Es importante apoyar a los pueblos bribri y cabécar en su lucha por la justicia!")

def apa():
    # E: N/A
    # S: N/A
    # R: N/A

    print("APA")
    print("El APA es la Asociación de Personas Anónimas.")
    print("El APA es una organización que brinda apoyo a personas que sufren de adicciones.")
    print("Si necesitas ayuda, no dudes en contactar al APA.")
    print("¡No estás solo!")

# Inicio

def inicio():

    # Opciones:
    # 1. ¡Tutorial!
    # 2. Jugar
    # 3. Instrucciones sobre solar punk
    # 4. Información sobre pueblos originarios.
    # 5. Información sobre conflicto cabaga Costa Rica
    # 6. APA
    # 7. Salir
    matriz_juego = []
    juego_activo = True
    turno = 0
    while juego_activo == True:
        print(f"¡Estas en el turno {turno}")
        print("¡Bienvenido a Solar Punk!")
        print("1. ¡Tutorial!")
        print("2. Jugar")
        print("3. Instrucciones sobre solar punk")
        print("4. Información sobre pueblos originarios.")
        print("5. Información sobre conflicto cabaga Costa Rica")
        print("6. APA")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")
        opcion_validada = validar_cadena_numero(opcion)

        if opcion_validada == False:
            print("Error: la opción debe ser un número.")
        else:
            opcion = int(opcion)

            if opcion == 1:
                tutorial()
            elif opcion == 2:
                if turno == 0:
                    matriz_juego = jugar(True, matriz_juego)
                else:
                    matriz_juego = jugar(False, matriz_juego)
                    if matriz_juego == True:
                        juego_activo = False
            elif opcion == 3:
                instrucciones_solar_punk()
            elif opcion == 4:
                informacion_pueblos_originarios()
            elif opcion == 5:
                informacion_conflicto_cabaga()
            elif opcion == 6:
                apa()
            elif opcion == 7:
                print("¡Gracias por jugar Solar Punk!")
                break
            else:
                print("Error: la opción debe ser un número entre 1 y 7.")
        turno += 1
inicio()
        
