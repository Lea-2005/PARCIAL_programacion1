def pedir_entero(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    """Solicita al usuario que ingrese un número entero dentro de un rango específico. Repite la petición hasta que el usuario ingrese un entero válido dentro del rango.

    Parámetros:
        mensaje (str): Texto que se muestra para pedir la entrada al usuario.
        mensaje_error (str): Texto que se muestra cuando la entrada no es válida o está fuera del rango.
        minimo (int): Valor mínimo permitido (inclusive).
        maximo (int): Valor máximo permitido (inclusive).

    Retorna:
        int: Número entero válido ingresado por el usuario dentro del rango especificado.
    """
    while True:
        numero = input(mensaje)
        
        if validar_entero(numero) == True:
            numero = int(numero)
            
            if numero < minimo or numero > maximo:
                print(mensaje_error)
            else:
                return numero
        else:
            print(mensaje_error)

def validar_entero(dato: str) -> bool:
    """Valida si una cadena representa un número entero válido, pudiendo ser negativo.

    Parámetros:
        dato (str): Cadena a validar.

    Retorna:
        bool: True si la cadena es un entero válido (opcionalmente negativo), False en caso contrario.
    """
    retorno = True

    if dato != "":
        if dato[0] == "-" and len(dato) > 1:
            for i in range(1, len(dato)):
                ascii = ord(dato[i])
                if ascii < 48 or ascii > 57:
                    retorno = False
                    break
        else:
            for i in range(len(dato)):
                ascii = ord(dato[i])
                if ascii < 48 or ascii > 57:
                    retorno = False
                    break
    else:
        retorno = False

    return retorno

def validar_mayuscula(valor_ascii: int) -> bool:
    """Verifica si el valor ASCII corresponde a una letra mayúscula (A-Z) o vocal acentuada mayúscula.

    Parámetros:
        valor_ascii (int): Código ASCII a validar.

    Retorna:
        bool: True si es mayúscula válida, False en caso contrario.
    """
    retorno = True

    if (valor_ascii < 65 or valor_ascii > 90) and valor_ascii not in (193, 201, 205, 209, 211, 218):
        retorno = False
        
    return retorno

def validar_minuscula(valor_ascii: int) -> bool:
    """Verifica si el valor ASCII corresponde a una letra minúscula (a-z) o vocal acentuada minúscula.

    Parámetros:
        valor_ascii (int): Código ASCII a validar.

    Retorna:
        bool: True si es minúscula válida, False en caso contrario.
    """
    retorno = True

    if (valor_ascii < 97 or valor_ascii > 122) and valor_ascii not in (225, 233, 237, 241, 243, 250):
        retorno = False
        
    return retorno

def validar_abecedario(cadena: str) -> bool:
    """Valida que una cadena contenga solo letras (mayúsculas o minúsculas, incluyendo vocales acentuadas) o espacios.

    Parámetros:
        cadena (str): Cadena a validar.

    Retorna:
        bool: True si todos los caracteres son válidos, False si encuentra alguno inválido.
    """
    retorno = True

    for i in range(len(cadena)):
            valor_ASCII = ord(cadena[i])
            if validar_mayuscula(valor_ASCII) == False and validar_minuscula(valor_ASCII) == False and valor_ASCII != 32:
                retorno = False
                break

    return retorno

def pedir_cadena(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    """Solicita al usuario ingresar una cadena que cumpla ciertas condiciones:
    - Longitud mínima
    - Solo letras y espacios válidos
    - No comienza con espacio
    Reintenta un número determinado de veces.

    Parámetros:
        mensaje (str): Texto para pedir la entrada al usuario.
        mensaje_error (str): Mensaje de error para entradas inválidas.
        longitud (int): Longitud mínima que debe tener la cadena.
        reintentos (int): Cantidad máxima de intentos permitidos.

    Retorna:
        str | None: La cadena válida ingresada, o None si se agotaron los intentos.
    """
    intento = 0

    while intento < reintentos:
        cadena = input(mensaje)

        if len(cadena) < longitud or validar_abecedario(cadena) == False or (ord(cadena[0])) == 32:
            print(mensaje_error)
        else:
            return cadena
        
        intento += 1

    return None

def crear_array(cantidad: int) -> list:
    """Crea una lista (array) de tamaño especificado, inicializada con None.

    Parámetros:
        cantidad (int): Número de elementos que tendrá la lista.

    Retorna:
        list: Lista de tamaño 'cantidad' con todos sus elementos inicializados en None.
    """
    array = [None] * cantidad

    return array

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """Crea una matriz (lista de listas) con las dimensiones dadas, inicializando todos los valores con uno especificado.

    Parámetros:
        cantidad_filas (int): Número de filas de la matriz.
        cantidad_columnas (int): Número de columnas de la matriz.
        valor_inicial (any): Valor con el que se inicializan todas las posiciones de la matriz.

    Retorna:
        list: Matriz (lista de listas) con las dimensiones y valores especificados.
    """
    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz

def mostrar_matriz(matriz: list) -> None:
    """Muestra en pantalla el contenido de una matriz, fila por fila.

    Parámetros:
        matriz (list): Matriz (lista de listas) a mostrar.

    Retorna:
        None
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(f"{matriz[f][c]}", end = " ")
        print("")

def sumar_columna(matriz: list, indice_columna: int) -> int:
    """Suma todos los valores numéricos (int o float) de una columna específica de una matriz.

    Parámetros:
        matriz (list): Matriz (lista de listas) donde se realizará la suma.
        indice_columna (int): Índice de la columna a sumar.

    Retorna:
        int: Suma de los valores numéricos encontrados en la columna especificada.
    """
    suma_columna = 0
        
    for fil in range(len(matriz)):
        if type(matriz[fil][indice_columna]) == int or type(matriz[fil][indice_columna]) == float:
            suma_columna += matriz[fil][indice_columna]

    return suma_columna 

def sumar_fila(matriz: list, indice_fila: int) -> int:
    """Suma todos los valores numéricos (int o float) de una fila específica de una matriz.

    Parámetros:
        matriz (list): Matriz (lista de listas) donde se realizará la suma.
        indice_fila (int): Índice de la fila a sumar.

    Retorna:
        int: Suma de los valores numéricos encontrados en la fila especificada.
    """
    suma_fila = 0
    
    for col in range(len(matriz[0])):
        if type(matriz[indice_fila][col]) == int or type(matriz[indice_fila][col]) == float :
            suma_fila += matriz[indice_fila][col]
    
    return suma_fila

def calcular_promedio(suma: int | float, cantidad_total: int | float) -> float | None:
    """Calcula el promedio dividiendo la suma entre la cantidad total.

    Parámetros:
        v (int | float): Suma total.
        cantidad_toal (int | float): Número total.

    Retorna:
        float: El promedio calculado.
        None: si "cantidad_notas" es 0, para evitar error al intentar dividir por cero.
    """
    if cantidad_total != 0:
        promedio = suma / cantidad_total
    
        return promedio
    
    return None

def identificar_menor(array: list) -> int | float | None:
    """Identifica el valor menor dentro de una lista de números.

    Parámetros:
        array (list): Lista de valores numéricos.

    Retorna:
        int | float | None: El valor menor encontrado en la lista, o None si no se ingresó una lista.
    """
    if type(array) != list and len(array) < 0:
        return None
    else:
        bandera = True

        for i in range(len(array)):
            if bandera == True:
                numero_menor = array[i]
                bandera = False
            else:
                if array[i] < numero_menor:
                    numero_menor = array[i]
    
    return numero_menor
