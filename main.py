import os
from adicionales import *
from funciones_parcial import *

array_participantes = crear_array(5)

bandera_participanes = False
bandera_jurados = False

while True:
    print("--- Menú de opciones ---")
    print("1. Cargar participantes\n2. Cargar puntuaciones\n3. Mostrar puntuaciones\n4. Participantes con promedio mayor a 4\n5. Participantes con promedio mayor a 7\n6. Promedio de cada jurado\n7. Jurado más estricto\n8. Buscar participante por nombre\n9. Top 3\n10. Participantes ordenados alfabéticamente\n")
    opcion = pedir_entero("• Tu opción: ", "Error. Ingrese un número entre (1-10)", 1, 10)

    os.system("cls")
    
    match opcion:
        case 1:
            bandera_jurados = False
            bandera_participanes = cargar_participantes(array_participantes)  
            matriz_puntuacion = crear_matriz(3, 5, 0)

            print("")
            if bandera_participanes == True:
                print("¡Datos cargados con éxito!")
            else:
                print("No se ha podido completar la carga.")
        case 2:
            if bandera_participanes == True:
                bandera_jurados = cargar_puntuacion(matriz_puntuacion, array_participantes)

                if bandera_jurados == True:
                    print("¡Puntuaciones asignadas con éxito!")
                else:
                    print("No se logró cargar las puntuaciones.")
            else:
                print("Antes de cargar las puntuaciones, se necesitan los datos de los participantes.")
        case 3:
            if (bandera_jurados and bandera_participanes) == True:
                if mostrar_puntuaciones(matriz_puntuacion, array_participantes) == True:
                    print("Puntuaciones mostradas correctamente.")
                else:
                    print("No se encontraron datos para mostrar.")
            else:
                print("Para mostrar esta opción se necesita la puntuación de los jurados.")
        case 4:
            if (bandera_jurados and bandera_participanes) == True:
                mostrar_promedio_cuatro(matriz_puntuacion, array_participantes)
            else:
                print("Antes de mostrar el promedio, se necesitan todos los datos de los participantes.")
        case 5:
            if (bandera_jurados and bandera_participanes) == True:
                mostrar_promedio_siete(matriz_puntuacion, array_participantes)
            else:
                print("Antes de mostrar el promedio, se necesitan todos los datos de los participantes.")
        case 6:
            if (bandera_jurados and bandera_participanes) == True:
                mostrar_promedios_jurados(matriz_puntuacion, array_participantes)
            else:
                print("Antes de mostrar el promedio, los jurados deben de puntuar a los participantes.")
        case 7:
            if (bandera_jurados and bandera_participanes) == True:
                mostrar_jurados_estrictos(matriz_puntuacion, array_participantes)
            else:
                print("Antes de mostrar el promedio, los jurados deben de puntuar a los participantes.")
        case 8:
            if (bandera_jurados and bandera_participanes) == True:
                nombre = pedir_cadena(f"• Ingrese nombre del participante: ", "Error. Debe ser un nombre real.", 3, 5)
                nombre_encontrado = mostrar_participante_especifico(array_participantes, matriz_puntuacion, nombre)

                if nombre_encontrado == True:
                    print("¡Participante encontrado con éxito!")
                else:
                    print("\nNo existe ningún participante con ese nombre.")
            else:
                print("Antes de mostrar el promedio, los jurados deben de puntuar a los participantes.")
        case 9:
            if (bandera_jurados and bandera_participanes) == True:
                validacion_top = mostrar_top_3(matriz_puntuacion, array_participantes)

                if validacion_top == True:
                    print("¡Top 3 encontrado con éxito!")
                else:
                    print("No se pudo encontrar a los participantes.")
            else:
                print("Antes de mostrar el promedio, los jurados deben de puntuar a los participantes.")
        case 10:
            if (bandera_jurados and bandera_participanes) == True:
                print("> Lista de participantes ordenada alfabeticamente")

                ordenar_participantes_alfabeticamente(array_participantes, matriz_puntuacion)
                if mostrar_puntuaciones(matriz_puntuacion, array_participantes) == True:
                    print("Puntuaciones ordenadas correctamente.")
                else:
                    print("No se encontraron datos para mostrar.")
            else:
                print("Antes de mostrar el promedio, los jurados deben de puntuar a los participantes.")

    input("> Presione enter para continuar... ")
    os.system("cls")
