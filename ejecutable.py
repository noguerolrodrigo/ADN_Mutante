from clases import Detector, Radiacion, Virus, Sanador  # Importa las clases del archivo clases.py

def obtener_matriz_adn():
    """
    Obtiene la matriz de ADN del usuario.

    Returns:
      Una lista de strings que representa la matriz de ADN.
    """
    matriz_adn = []  # Crea una lista vacía para almacenar la matriz
    print("Ingrese la secuencia de ADN (6 filas de 6 caracteres, ejemplo: AGATCA):")
    for i in range(6):  # Itera 6 veces para obtener las 6 filas
        while True:  # Crea un bucle infinito para validar la entrada del usuario
            fila = input(f"Fila {i+1}: ").upper()  # Obtiene la fila del usuario y la convierte a mayúsculas
            if len(fila) == 6 and all(c in "ATCG" for c in fila):  # Verifica si la fila tiene 6 caracteres y si todos son bases nitrogenadas válidas
                matriz_adn.append(fila)  # Si la fila es válida, la agrega a la matriz
                break  # Sale del bucle
            else:
                print("Fila inválida. Ingrese 6 caracteres con bases válidas (A, T, C, G).")  # Si la fila no es válida, muestra un mensaje de error
    return matriz_adn  # Devuelve la matriz de ADN

def main():
    """
    Función principal del programa.
    """
    matriz_adn = obtener_matriz_adn()  # Obtiene la matriz de ADN del usuario
    
    while (True): 
        print("\nSeleccione una acción:")  # Muestra las opciones al usuario
        print("1. Detectar mutantes")
        print("2. Mutar")
        print("3. Sanar")
        print("4. Salir")

        opcion = input("> ")  # Obtiene la opción del usuario

        if opcion == "1":  # Si el usuario selecciona la opción 1
            detector = Detector()  # Crea una instancia de la clase Detector
            if detector.detectar_mutantes(matriz_adn):  # Llama al método detectar_mutantes para verificar si hay mutaciones
                print("¡ADN mutante detectado!")  # Si hay mutaciones, muestra un mensaje
            else:
                print("No se detectaron mutaciones.")  # Si no hay mutaciones, muestra otro mensaje
        elif opcion == "2":  # Si el usuario selecciona la opción 2
            base = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()  # Obtiene la base nitrogenada para la mutación
            fila = int(input("Ingrese la fila de la posición inicial (1-6): ")) - 1  # Obtiene la fila de la posición inicial
            columna = int(input("Ingrese la columna de la posición inicial (1-6): ")) - 1  # Obtiene la columna de la posición inicial
            orientacion = input("Ingrese la orientación de la mutación (H: horizontal, V: vertical, D: diagonal): ").upper()  # Obtiene la orientación de la mutación

            if orientacion == "H" or orientacion == "V":  # Si la orientación es horizontal o vertical
                mutador = Radiacion(base, (fila, columna), orientacion)  # Crea una instancia de la clase Radiacion
            elif orientacion == "D":  # Si la orientación es diagonal
                mutador = Virus(base, (fila, columna))  # Crea una instancia de la clase Virus
            else:
                print("Orientación inválida.")  # Si la orientación no es válida, muestra un mensaje de error
                return False  # Sale de la función

            matriz_mutada = mutador.crear_mutante(matriz_adn)  # Llama al método crear_mutante para crear la mutación
            if matriz_mutada:  # Si la mutación se creó correctamente
                print("\nADN mutado:")  # Muestra un mensaje
                for fila in matriz_mutada:  # Recorre la matriz mutada
                    print(fila)  # Imprime cada fila
        elif opcion == "3":  # Si el usuario selecciona la opción 3
            sanador = Sanador()  # Crea una instancia de la clase Sanador
            matriz_sanada = sanador.sanar_mutantes(matriz_adn)  # Llama al método sanar_mutantes para sanar las mutaciones
            print("\nADN sanado:")  # Muestra un mensaje
            for fila in matriz_sanada:  # Recorre la matriz sanada
                print(fila)  # Imprime cada fila
        elif opcion == "4":
            print("¡Hasta luego!")  # Muestra un mensaje de despedida
            break  # Sale del bucle principal y finaliza la ejecucion
        else:
            print("Opción inválida.")  # Si la opción no es válida, muestra un mensaje de error
if __name__ == "__main__":  # Verifica si el script se está ejecutando como programa principal
    main()  # Llama a la función principal