from adicionales import *

def cargar_participantes(array: list) -> bool:
    """Solicita al usuario ingresar nombres para cada participante y los almacena en la lista dada. 

    Parámetros:
        array (list): Lista que se actualizará con los nombres de los participantes. Debe tener espacio asignado previamente.

    Retorna:
        bool: True si se cargaron todos los nombres correctamente, False si hubo algún error o si se interrumpió la carga.

    Observaciones:
        - La función espera que 'array' tenga una longitud mayor a cero.
        - Si se ingresa un nombre que ya se había escrito antes, el usuario deberá ingresar otro nombre hasta que no coincidan.
    """
    if type(array) == list and len(array) > 0:
        nombres_guardados = []
        retorno = True
        
        for i in range(len(array)):
            nombre = pedir_cadena(f"• Ingrese nombre de participante {i + 1}: ", "Error. Debe ser un nombre real.", 3, 5)
            while nombre in nombres_guardados:
                print("No se puede repetir nombres.")
                nombre = pedir_cadena(f"• Reingrese nombre de participante {i + 1}: ", "Error. Debe ser un nombre real.", 3, 1)
            
            if nombre == None:
                retorno = False
                break

            array[i] = nombre
            nombres_guardados += [nombre]
    else:
        retorno = False

    return retorno

def cargar_puntuacion(matriz_puntuacion: list, array_participantes: list) -> bool:
    """Solicita al usuario ingresar puntuaciones para cada participante, registrándolas en una matriz dada.

    Parámetros:
        matriz_puntuacion (list): Matriz (lista de listas) donde se almacenarán las puntuaciones. Cada fila corresponde a un jurado.
        array_participantes (list): Lista de participantes, usada para mostrar a quién se le está ingresando la puntuación.

    Retorna:
        bool: True si todas las puntuaciones fueron ingresadas correctamente, False si la matriz no es válida.
    
    Observaciones:
        - La función espera que 'matriz' tenga al menos una fila y que 'array' tenga participantes.
        - Se asume que cada fila de la matriz tiene el mismo número de columnas que participantes.
    """
    if type(matriz_puntuacion) == list and len(matriz_puntuacion) > 0:
        for f in range(len(matriz_puntuacion)):
            print(f"Jurado número {f + 1}:")
            for c in range(len(matriz_puntuacion[f])):
                puntuacion = pedir_entero(f"• Ingresar puntuación de {array_participantes[c]}: ", "Error. La puntuación debe ser entre (1-10).", 1, 10)

                matriz_puntuacion[f][c] = puntuacion
            print("")
        retorno = True
    else:
        retorno = False

    return retorno

def mostrar_puntuaciones(matriz_puntuacion: list, array_participantes: list) -> bool:
    """Muestra la puntuación otorgada por cada jurado a cada participante, junto con su promedio.

    Parámetros:
        matriz_puntuacion (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.
        array_participantes (list): Lista con los nombres de los participantes.

    Retorna:
        bool: True si la lista de participantes no está vacía y se muestran los resultados, False si no hay participantes.
    """
    if type(array_participantes) == list and len(array_participantes) > 0:
        for i in range(len(array_participantes)):
            cantidad = sumar_columna(matriz_puntuacion, i)
            promedio = calcular_promedio(cantidad, len(matriz_puntuacion))

            print(f"• Participante: {array_participantes[i]}")
            print(f"Puntaje jurado 1: {matriz_puntuacion[0][i]}")
            print(f"Puntaje jurado 2: {matriz_puntuacion[1][i]}")
            print(f"Puntaje jurado 3: {matriz_puntuacion[2][i]}")
            print(f"Promedio: {round(promedio, 2)}/10\n")

        retorno = True
    else:
        retorno = False

    return retorno

def mostrar_promedio_cuatro(matriz_puntuacion: list, array_participantes: list) -> None:
    """Muestra los participantes cuyo promedio de puntuación es mayor a 4.

    Parámetros:
        matriz_puntuacion (list): Matriz con las puntuaciones de los participantes (columnas) dadas por los jurados (filas).
        array_participantes (list): Lista con los nombres de los participantes.

    Retorna:
        None: Imprime los participantes con promedio mayor a 4. Si no hay ninguno, muestra un mensaje indicándolo.

    Observaciones:
        - El promedio se calcula dividiendo la suma de las puntuaciones por la cantidad de jurados,
        que se obtiene dinámicamente con len(matriz_puntuacion).
    """
    contador = 0

    print("• Participantes con promedio mayor a 4:")
    for i in range(len(array_participantes)):
        cantidad = sumar_columna(matriz_puntuacion, i)
        promedio = calcular_promedio(cantidad, len(matriz_puntuacion))

        if promedio > 4:
            print(f"Participante: {array_participantes[i]}")
            print(f"Promedio: {round(promedio, 2)}/10\n")
            contador += 1

    if contador == 0:
        print("- No se han encontrado participantes con un promedio mayor a 4.\n")

def mostrar_promedio_siete(matriz_puntuacion: list, array_participantes: list) -> None:
    """Muestra los participantes cuyo promedio de puntuación es mayor a 7.

    Parámetros:
        matriz_puntuacion (list): Matriz con las puntuaciones de los participantes (columnas) dadas por los jurados (filas).
        array_participantes (list): Lista con los nombres de los participantes.

    Retorna:
        None: Imprime los participantes con promedio mayor a 7. Si no hay ninguno, muestra un mensaje indicándolo.

    Observaciones:
        - El promedio se calcula dividiendo la suma de las puntuaciones por la cantidad de jurados,
        que se obtiene dinámicamente con len(matriz_puntuacion).
    """
    contador = 0

    print("• Participantes con promedio mayor a 7:")
    for i in range(len(array_participantes)):
        cantidad = sumar_columna(matriz_puntuacion, i)
        promedio = calcular_promedio(cantidad, len(matriz_puntuacion))

        if promedio > 7:
            print(f"Participante: {array_participantes[i]}")
            print(f"Promedio: {round(promedio, 2)}/10\n")
            contador += 1

    if contador == 0:
        print("- No se han encontrado participantes con un promedio mayor a 7.\n")

def calcular_promedio_jurado(matriz_puntuacion: list, array_participantes: list) -> list:
    """Calcula el promedio de puntuaciones otorgadas por cada jurado.

    Parámetros:
        matriz_puntuacion (list): Matriz de puntuaciones donde cada fila representa a un jurado y cada columna a un participante.
        array_participantes (list): Lista que representa la cantidad de participantes (se usa para obtener el divisor dinámico).

    Retorna:
        list: Lista con el promedio de puntuación para cada jurado.

    Observaciones:
        - El promedio se calcula dividiendo la suma de las puntuaciones de cada jurado
        por la cantidad de participantes (longitud del array).
    """
    promedios = []

    for i in range(len(matriz_puntuacion)):
        cantidad = sumar_fila(matriz_puntuacion, i)
        promedio = calcular_promedio(cantidad, len(array_participantes))

        promedios += [promedio]
    return promedios

def mostrar_promedios_jurados(matriz_puntuacion: list, array_participantes: list) -> None:
    """Muestra el promedio de puntuación que cada jurado ha otorgado.

    Parámetros:
        matriz_puntuacion (list): Matriz de puntuaciones donde cada fila representa a un jurado.
        array_participantes (list): Lista con los nombres de los participantes.

    Retorna:
        None: Imprime los promedios de cada jurado.
    """
    array_promedios = calcular_promedio_jurado(matriz_puntuacion, array_participantes)
    
    print("• Promedios de jurados:")
    for i in range(len(array_promedios)):
        print(f"Jurado N°{i + 1}:")
        print(f"Promedio: {round(array_promedios[i], 2)}/10\n")

def mostrar_jurados_estrictos(matriz_puntuacion: list, array_participantes: list) -> None:
    """Muestra los jurados que son más estrictos, es decir, que tienen el promedio de puntuación más bajo.

    Parámetros:
        matriz_puntuaciones (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.
        array_participantes (list): Lista con los nombres de los participantes.

    Retorna:
        None: Imprime los jurados con el promedio más bajo.
    """
    array_promedios = calcular_promedio_jurado(matriz_puntuacion, array_participantes)
    numero_menor = identificar_menor(array_promedios)
    
    print("• Jurados más estrictos:")
    for i in range(len(array_promedios)):
        if array_promedios[i] == numero_menor:
            print(f"Jurado N°{i + 1} ha dado, en promedio, {round(array_promedios[i], 2)}/10 de puntuación.")
    print("")

def mostrar_participante_especifico(array_participantes: list, matriz_puntuacion: list, nombre: str) -> bool:
    """Muestra la puntuación y promedio de un participante específico, si existe en la lista.

    Parámetros:
        array_participantes (list): Lista con los nombres de los participantes.
        matriz_puntuaciones (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.
        nombre (str): Nombre del participante a buscar.

    Retorna:
        bool: True si el participante fue encontrado y mostrado, False si no existe.
    """
    for i in range(len(array_participantes)):
        if array_participantes[i] == nombre:
            cantidad = sumar_columna(matriz_puntuacion, i)
            promedio = calcular_promedio(cantidad, len(matriz_puntuacion))

            print(f"• Participante: {array_participantes[i]}")
            print(f"Puntaje jurado 1: {matriz_puntuacion[0][i]}")
            print(f"Puntaje jurado 2: {matriz_puntuacion[1][i]}")
            print(f"Puntaje jurado 3: {matriz_puntuacion[2][i]}")
            print(f"Promedio: {round(promedio, 2)}/10\n")

            return True
    return False

def calcular_promedio_puntuacion(matriz_puntuacion: list) -> list:
    """Calcula el promedio de puntuaciones para cada participante (columna).

    Parámetros:
        matriz_puntuaciones (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.

    Retorna:
        list: Lista con el promedio de puntuación por participante.
    """
    lista_promedios = []

    for col in range(len(matriz_puntuacion[0])):
        cantidad = sumar_columna(matriz_puntuacion, col)
        promedio = calcular_promedio(cantidad, len(matriz_puntuacion))

        lista_promedios += [promedio]
    return lista_promedios

def ordenar_puntuaciones_promedios(array_participantes: list, matriz_puntuaciones: list) -> None:
    """Ordena los participantes y sus puntuaciones en orden ascendente según el promedio de puntuaciones.

    Parámetros:
        array_participantes (list): Lista con los nombres de los participantes.
        matriz_puntuaciones (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.

    Retorna:
        None: Modifica los parámetros directamente para ordenar participantes y sus puntuaciones.
    """
    promedios = calcular_promedio_puntuacion(matriz_puntuaciones)

    for izq in range(len(promedios) - 1):
        for der in range((izq + 1), len(promedios)):        
            if promedios[izq] > promedios[der]:

                intercambiar_elementos(array_participantes, izq, der)
                intercambiar_columnas(matriz_puntuaciones, izq, der)
                intercambiar_elementos(promedios, izq, der)

def mostrar_top_3(matriz_puntuacion: list, array_participantes: list) -> bool:
    """
    Muestra los 3 participantes con los mejores promedios de puntuación.

    Parámetros:
        matriz_puntuaciones (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.
        array_participantes (list): Lista con nombres de participantes.

    Retorna:
        bool: True si se muestra correctamente el top 3, False si la lista de participantes está vacía o no es lista.
    """
    if type(array_participantes) == list and len(array_participantes) > 0:
        ordenar_puntuaciones_promedios(array_participantes, matriz_puntuacion)

        contador = 5
        print("> Top 3 de participantes según su promedio de puntuaciones:")

        for i in range(len(array_participantes)):
            cantidad = sumar_columna(matriz_puntuacion, i)
            promedio = calcular_promedio(cantidad, 3)

            if contador < 4:
                print(f"Top {contador}")
                print(f"• Participante: {array_participantes[i]}")
                print(f"Puntaje jurado 1: {matriz_puntuacion[0][i]}")
                print(f"Puntaje jurado 2: {matriz_puntuacion[1][i]}")
                print(f"Puntaje jurado 3: {matriz_puntuacion[2][i]}")
                print(f"Promedio: {round(promedio, 2)}/10\n")
            contador -= 1
        retorno = True
    else:
        retorno = False
        
    return retorno

def ordenar_participantes_alfabeticamente(array_participantes: list, matriz_puntuaciones: list) -> None:
    """Ordena los participantes y sus puntuaciones alfabéticamente por nombre.

    Parámetros:
        array_participantes (list): Lista con los nombres de los participantes.
        matriz_puntuaciones (list): Matriz con las puntuaciones, donde cada fila es un jurado y cada columna un participante.

    Retorna:
        None: Modifica directamente los parámetros para ordenar los datos.
    """
    for izq in range(len(array_participantes) - 1):
        for der in range((izq + 1), len(array_participantes)):        
            if array_participantes[izq] > array_participantes[der]:
              
                intercambiar_elementos(array_participantes, izq, der)
                intercambiar_columnas(matriz_puntuaciones, izq, der)

def intercambiar_elementos(array_participantes: list, izq: int, der: int) -> None:
    """Intercambia dos elementos en una lista.

    Parámetros:
        array_participantes (list): Lista con los nombres de los participantes.
        izq (int): Índice del primer elemento.
        der (int): Índice del segundo elemento.

    Retorna:
        None. Modifica la lista original.
    """
    auxiliar = array_participantes[izq]
    array_participantes[izq] = array_participantes[der]
    array_participantes[der] = auxiliar

def intercambiar_columnas(matriz_puntuaciones: list, col1: int, col2: int) -> None:
    """Intercambia dos columnas específicas en una matriz (lista de listas) de puntuaciones.

    Parámetros:
        matriz_puntuaciones (list): Matriz de puntuaciones, donde cada fila representa un jurado y cada columna un participante.
        col1 (int): Índice de la primera columna a intercambiar.
        col2 (int): Índice de la segunda columna a intercambiar.

    Retorna:
        None: La matriz se modifica directamente intercambiando los valores en las columnas indicadas.
    """

    for fila in range(len(matriz_puntuaciones)):
        auxiliar = matriz_puntuaciones[fila][col1]
        matriz_puntuaciones[fila][col1] = matriz_puntuaciones[fila][col2]
        matriz_puntuaciones[fila][col2] = auxiliar
