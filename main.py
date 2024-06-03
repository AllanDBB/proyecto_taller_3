import random

def limpiar_pantalla():
    # E: N/A
    # S: N/A
    # R: N/A

    for i in range(100):
        print()

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
    """
    Imprime una matriz en la consola con colores según el contenido de cada celda.

    Args:
        matriz: La matriz a imprimir.

    Returns:
        None
    """

    if not es_matriz(matriz):
        return 'Error: no es matriz'

    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    AZUL = "\033[94m"
    RESET = "\033[0m"

    n = len(matriz)
    m = len(matriz[0])

    # Imprimir índices de columnas
    print("     ", end="")
    for j in range(m):
        print(j, end="   ")
    print()

    for i in range(n):
        # Imprimir índice de fila
        print(i, end="  |  ")
        for j in range(m):
            if matriz[i][j] == "P":
                color = VERDE  # Proyecto en verde
            elif matriz[i][j] == "C":
                color = AMARILLO  # Cultura en amarillo
            elif matriz[i][j] == "I":
                color = AZUL  # Iniciativa en azul
            elif matriz[i][j] == "U":
                color = ROJO  # Usurpación en rojo
            else:
                color = RESET  # Celda vacía sin color

            print(color + str(matriz[i][j]) + RESET, end="   ")  # Imprimir con color
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

    """
    Función principal del juego Solar Punk.
    """

    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    RESET = "\033[0m"

    print(f"\n{VERDE}🌱 ¡Bienvenido a Solar Punk! 🌱{RESET}")
    print(f"{AMARILLO}¡Buena suerte construyendo un futuro sostenible!{RESET}\n")

    
    if primera_vez:
        dimensiones = input("Ingrese las dimensiones de la matriz (>=3): ")
        dimensiones_validadas = validar_cadena_numero(dimensiones)

        if dimensiones_validadas == False:
            print(f"{ROJO}⛔ ¡Error! Las dimensiones deben ser un número.{RESET}")
            return jugar(True, matriz)
        else:
            dimensiones = int(dimensiones)

            if dimensiones < 3:
                print(f"{ROJO}⛔ ¡Error! Las dimensiones deben ser al menos 3x3.{RESET}")
                return jugar(True, matriz)
            else:
                matriz = generar_matriz(dimensiones)
                imprimir_matriz(matriz)
                return matriz
    else:

        cantidad_usurpaciones = random.randint(1, len(matriz)//2)
        for i in range(cantidad_usurpaciones):
            usurpacion(matriz)

        print(f"\n{AMARILLO}¿Qué quieres hacer?{RESET}")
        print(f"1. 🌱 {VERDE}Plantar una iniciativa{RESET}")
        print(f"2. 🚧 {VERDE}Establecer un proyecto{RESET}")
        print(f"3. 🗣️ {VERDE}Difundir cultura{RESET}\n")

        opcion = input("Elige una opción (1-3): ")
        opcion_validada = validar_cadena_numero(opcion)

        if opcion_validada == False:
            print(f"{ROJO}⛔ ¡Error! La opción debe ser un número.{RESET}")
            return jugar(False, matriz)
        else:
            opcion = int(opcion)

            if opcion == 1:
                
                for iniciativa in range(2):

                    print(f"\n¿Dónde quieres plantar tu {iniciativa + 1}ª iniciativa?")

                    fila = input(f"{AMARILLO}Fila:{RESET} ")
                    fila_validada = validar_cadena_numero(fila)

                    columna = input(f"{AMARILLO}Columna:{RESET} ")
                    columna_validada = validar_cadena_numero(columna)

                    if fila_validada == False or columna_validada == False:
                        print(f"{ROJO}⛔ ¡Error! Las coordenadas deben ser números.{RESET}")
                        return jugar(False, matriz)
                    else:
                        colocar_elemento(matriz, "I", int(fila), int(columna))
                        imprimir_matriz(matriz)
                    

            elif opcion == 2:
                
                print("\n¿Dónde quieres establecer tu proyecto?")

                fila = input(f"{AMARILLO}Fila:{RESET} ")
                fila_validada = validar_cadena_numero(fila)

                columna = input(f"{AMARILLO}Columna:{RESET} ")
                columna_validada = validar_cadena_numero(columna)


                if fila_validada == False or columna_validada == False:
                    print(f"{ROJO}⛔ ¡Error! Las coordenadas deben ser números.{RESET}")
                    return jugar(False, matriz) 
                else:
                    colocar_elemento(matriz, "P", int(fila), int(columna))
                    imprimir_matriz(matriz)

                

            elif opcion == 3:
                
                probabilidad = random.randint(1, 3)
                # 1: Llena una fila de cultura vertical
                # 2: Llena una columna de cultura horizontal
                # 3: No ha podido difundir cultura

                if probabilidad == 1:
                    
                    print(f"\n{VERDE}¡Has difundido cultura de forma horizontal!{RESET}")
                    fila = input(f"{AMARILLO}¿En qué fila quieres difundir cultura?{RESET} ")
                    fila_validada = validar_cadena_numero(fila)

                    if fila_validada == False:
                        print(f"{ROJO}⛔ ¡Error! La fila debe ser un número.{RESET}")
                        return jugar(False, matriz)
                    else:
                        llenar_fila(matriz, "C", int(fila))
                        imprimir_matriz(matriz)
                
                elif probabilidad == 2:
                        
                    print(f"\n{VERDE}¡Has difundido cultura de forma horizontal!{RESET}")
                    columna = input(f"{AMARILLO}¿En qué columna quieres difundir cultura?{RESET} ")
                    columna_validada = validar_cadena_numero(columna)
    
                    if columna_validada == False:
                        print(f"{ROJO}⛔ ¡Error! La columna debe ser un número.{RESET}")
                        return jugar(False, matriz)
                    else:
                        llenar_columna(matriz, "C", int(columna))
                        imprimir_matriz(matriz)
                
                else:
                    print(f"\n{ROJO}¡No has podido difundir cultura!{RESET}")
                    imprimir_matriz(matriz)
    
            else:
                print(f"{ROJO}⛔ ¡Error! La opción debe ser un número entre 1 y 3.{RESET}")
                return jugar(False, matriz)
        
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] == "I":
                    matriz[i][j] = "P"

        for i in range(len(matriz)):
            if matriz[i].count("P") == len(matriz) or matriz[i].count("U") == len(matriz):
                print(f"\n{ROJO}¡Has perdido!{RESET}")
                return True
        
        return matriz
             
def tutorial():
    """
    Presenta el tutorial del juego Solar Punk de manera interactiva y amigable.
    """
    limpiar_pantalla()  # Limpia la pantalla para una mejor presentación

    print("\n¡Bienvenido al mundo de Solar Punk!\n")
    print("--------------------------------------------------")
    print("      🌱  UN FUTURO MÁS VERDE TE ESPERA  🌱        ")
    print("--------------------------------------------------\n")

    input("Presiona Enter para comenzar el tutorial... ")
    limpiar_pantalla()

    print("\n🌱  OBJETIVO DEL JUEGO 🌱")
    print("----------------------------")
    print("Sobrevive en un mundo  donde la naturaleza retoma su lugar. ")
    print("Tu misión es construir una sociedad sostenible y próspera.\n")

    input("Presiona Enter para continuar... ")
    limpiar_pantalla()

    print("\n⚙️  MECÁNICAS BÁSICAS ⚙️")
    print("----------------------------")
    print("- PLANTAR INICIATIVAS (I): Siembra las semillas de un futuro mejor.")
    print("- ESTABLECER PROYECTOS (P): Convierte tus iniciativas en proyectos concretos.")
    print("- DIFUNDIR CULTURA (C): Expande el conocimiento y la conciencia ecológica.")
    print("- USURPACIÓN (U): ¡Cuidado! Fuerzas opuestas intentarán sabotear tu progreso.\n")

    input("Presiona Enter para continuar... ")
    limpiar_pantalla()

    print("\n✨  ¡CONSEJOS PARA TRIUNFAR! ✨")
    print("--------------------------------")
    print("- Planifica estratégicamente dónde colocar tus iniciativas y proyectos.")
    print("- Prioriza la difusión de cultura para proteger tus logros.")
    print("- ¡No te rindas ante las usurpaciones! La perseverancia es clave.\n")

    print("--------------------------------------------------")
    print("      ¡LISTO PARA CONSTRUIR EL FUTURO!        ")
    print("--------------------------------------------------\n")
    input("Presiona Enter para volver al menú principal... ")
   
def instrucciones_solar_punk():
    """
    Presenta el mundo Solarpunk y sus beneficios de manera atractiva y colorida.
    """
    limpiar_pantalla()

    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{VERDE}🌿 ¡Bienvenido al mundo de Solar Punk! 🌿{RESET}\n")
    print("--------------------------------------------------")
    print(f"{AMARILLO}      ☀️  UN FUTURO RADIANTE Y SOSTENIBLE  ☀️      {RESET}")
    print("--------------------------------------------------\n")

    print(f"{VERDE}¿Qué es Solar Punk?{RESET}")
    print("Es un movimiento artístico y literario que imagina un futuro utópico donde la tecnología y la naturaleza conviven en armonía. Es una visión optimista y esperanzadora de un mundo donde la energía renovable, la sostenibilidad y la justicia social son pilares fundamentales.\n")

    print(f"{AMARILLO}¿Por qué Solar Punk?{RESET}")
    print("Porque nos ofrece una alternativa inspiradora al pesimismo y la distopía. Nos invita a soñar con un futuro mejor y a trabajar activamente para construirlo. Solar Punk nos muestra que otro mundo es posible, un mundo más justo, equitativo y en equilibrio con el medio ambiente.\n")

    print(f"{VERDE}Beneficios de un mundo Solar Punk:{RESET}")
    print("- ☀️ Energía limpia y renovable para todos.")
    print("- 🌿 Ciudades verdes y sostenibles integradas con la naturaleza.")
    print("- 🤝 Comunidades fuertes y colaborativas basadas en la justicia social.")
    print("- 🌍 Un planeta sano y regenerado para las futuras generaciones.\n")

    print("--------------------------------------------------")
    print(f"{AMARILLO}    ¡Únete a la revolución Solar Punk!   {RESET}")
    print("--------------------------------------------------\n")

    input("Presiona Enter para volver al menú principal... ")

def informacion_pueblos_originarios():
    """
    Presenta información sobre los pueblos originarios de Costa Rica.
    """
    limpiar_pantalla()

    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{VERDE}🌿 PUEBLOS ORIGINARIOS DE COSTA RICA 🌿{RESET}\n")
    print("--------------------------------------------------")
    print(f"{AMARILLO}      Un legado ancestral de sabiduría y resistencia      {RESET}")
    print("--------------------------------------------------\n")

    print(f"{VERDE}¿Quiénes son?{RESET}")
    print("Son las comunidades indígenas que han habitado el territorio costarricense desde tiempos inmemoriales. Son los guardianes de una rica herencia cultural, lingüística y espiritual, profundamente conectada con la naturaleza y sus ciclos.\n")

    print(f"{AMARILLO}Los ocho pueblos indígenas de Costa Rica:{RESET}")
    print("- Bribri")
    print("- Cabécar")
    print("- Maleku")
    print("- Térraba")
    print("- Boruca")
    print("- Huetar")
    print("- Ngäbe")
    print("- Chorotega\n")

    print(f"{VERDE}Su importancia:{RESET}")
    print("Los pueblos originarios son fundamentales para la identidad y la diversidad de Costa Rica. Su conocimiento ancestral sobre la tierra, la medicina natural y la conservación del medio ambiente es invaluable. Además, su lucha por la defensa de sus derechos y territorios es un ejemplo de resistencia y perseverancia.\n")

    print(f"{AMARILLO}Desafíos y esperanzas:{RESET}")
    print("A pesar de los desafíos históricos de discriminación y despojo territorial, los pueblos originarios siguen luchando por mantener vivas sus tradiciones y proteger sus tierras. Su resiliencia y su visión de un futuro sostenible son una fuente de inspiración para todos los costarricenses.\n")

    print("--------------------------------------------------")
    print(f"{VERDE}    ¡Honremos y aprendamos de nuestros pueblos originarios!   {RESET}")
    print("--------------------------------------------------\n")

    input("Presiona Enter para volver al menú principal... ")

def informacion_conflicto_cabaga():
    """
    Presenta información sobre el conflicto en el territorio indígena de Cabagra.
    """
    limpiar_pantalla()

    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{VERDE}🌿 CONFLICTO EN CABAGRA, PUNTARENAS 🌿{RESET}\n")
    print("--------------------------------------------------")
    print(f"{AMARILLO}      Lucha por la tierra y la seguridad en territorios indígenas      {RESET}")
    print("--------------------------------------------------\n")

    print(f"{VERDE}El problema:{RESET}")
    print("Cabagra, un territorio indígena en Puntarenas, enfrenta una creciente ola de usurpación de tierras. A pesar de la protección legal, personas externas invaden estos territorios de forma agresiva, generando violencia e inseguridad para los habitantes indígenas.\n")

    print(f"{AMARILLO}Incidentes recientes:{RESET}")
    print(f"- {AMARILLO}Febrero 2020:{RESET} Un intruso estableció un campamento con acompañantes armados, lo que generó alarma y preocupación por un posible aumento de la violencia.")
    print(f"- {AMARILLO}Noviembre 2022:{RESET} Un grupo indígena recuperó una finca ocupada, creando un ambiente hostil según las autoridades. Este incidente resalta la necesidad urgente de diálogo y soluciones pacíficas.\n")

    print(f"{VERDE}Consecuencias:{RESET}")
    print("La usurpación de tierras en Cabagra no solo viola los derechos de los pueblos originarios, sino que también pone en riesgo su seguridad y bienestar. La violencia asociada a estas invasiones genera un clima de miedo e incertidumbre en la comunidad.\n")

    print("--------------------------------------------------")
    print(f"{AMARILLO}    ¡La lucha por la tierra y la justicia continúa!   {RESET}")
    print("--------------------------------------------------\n")

    input("Presiona Enter para volver al menú principal... ")

def apa():
    # E: N/A
    # S: N/A
    # R: N/A

    print("APA")
    print("El APA es la Asociación de Personas Anónimas.")
    print("El APA es una organización que brinda apoyo a personas que sufren de adicciones.")
    print("Si necesitas ayuda, no dudes en contactar al APA.")
    print("¡No estás solo!")

def inicio():
    """
    Muestra el menú principal del juego y gestiona la navegación entre las opciones.
    """
    matriz_juego = []
    juego_activo = True
    turno = 0

    # Códigos ANSI de escape para colores
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    ROJO = "\033[91m"
    MAGENTA = "\033[95m"
    CIAN = "\033[96m"
    RESET = "\033[0m"

    while juego_activo:
        limpiar_pantalla()

        print(f"\n{VERDE}🌱 TURNO {turno} 🌱\n{RESET}")  # Turno actual con emojis y color verde
        print(f"{AMARILLO}🌿 ¡Bienvenido a Solar Punk! 🌿\n{RESET}")
        print(f"{CIAN}┌───────────────────────────────┐{RESET}")  # Borde superior
        print(f"{CIAN}│   --- MENÚ PRINCIPAL ---      │{RESET}")
        print(f"{CIAN}├───────────────────────────────┤{RESET}")  # Separador
        print(f"{CIAN} {AZUL}1. 📖 ¡Tutorial!             {RESET} ")
        print(f"{CIAN} {VERDE}2. ▶️ Jugar                 {RESET}  ")
        print(f"{CIAN} {AMARILLO}3. ℹ️ Solar Punk        {RESET}     ")
        print(f"{CIAN} {ROJO}4. 🌍 Pueblos Originarios   {RESET}   ")
        print(f"{CIAN} {MAGENTA}5. ⚔️ Conflicto de Cabagra  {RESET}")
        print(f"{CIAN} {VERDE}6. 💚 APA                   {RESET}")
        print(f"{CIAN} {ROJO}7. ❌ Salir                 {RESET}")
        print(f"{CIAN}└───────────────────────────────┘\n{RESET}")  # Borde inferior

        print(f"{MAGENTA} Matriz de juego: {RESET}")

        if matriz_juego != []:
            imprimir_matriz(matriz_juego)
        print("\n")
        opcion = input("Elige una opción: ")

        opcion_validada = validar_cadena_numero(opcion)

        if not opcion_validada:
            print(f"\n{ROJO}⛔ ¡Error! Debes ingresar un número.\n{RESET}") 
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
                print(f"\n{VERDE}¡Gracias por jugar Solar Punk! 🌿\n{RESET}")
                break
            else:
                print(f"\n{ROJO}⛔ ¡Error! Opción inválida. Elige un número entre 1 y 7.\n{RESET}") 

        turno += 1

inicio()
        
