import random  # Importamos la librería random para generar secuencias aleatorias de ADN

class Detector:
    """
    Clase encargada de detectar mutaciones en una secuencia de ADN.
    """
    def __init__(self):
        """
        Constructor de la clase Detector. 
        Inicializa los atributos longitud_minima_secuencia y bases_nitrogenadas.
        """
        self.longitud_minima_secuencia = 4  # Define la longitud mínima de la secuencia para considerarse mutación
        self.bases_nitrogenadas = ['A', 'T', 'C', 'G']  # Define las bases nitrogenadas válidas

    def detectar_mutantes(self, matriz_adn):
        """
        Detecta si hay un mutante horizontal, vertical o diagonal en la matriz de ADN.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          True si hay mutaciones, False si no hay.
        """
        # Llama a las funciones que detectan mutaciones en cada dirección y devuelve True si alguna encuentra una mutación
        return (self.detectar_mutante_horizontal(matriz_adn) or 
                self.detectar_mutante_vertical(matriz_adn) or 
                self.detectar_mutante_diagonal(matriz_adn))

    def detectar_mutante_horizontal(self, matriz_adn):
        """
        Detecta si hay un mutante horizontal en la matriz de ADN.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          True si hay un mutante horizontal, False si no hay.
        """
        for fila in matriz_adn:  # Recorre cada fila de la matriz
            for base in self.bases_nitrogenadas:  # Recorre cada base nitrogenada
                if base * self.longitud_minima_secuencia in fila:  # Verifica si hay 4 bases iguales consecutivas en la fila
                    return True  # Si encuentra una mutación, devuelve True
        return False  # Si no encuentra mutaciones en ninguna fila, devuelve False

    def detectar_mutante_vertical(self, matriz_adn):
        """
        Detecta si hay un mutante vertical en la matriz de ADN.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          True si hay un mutante vertical, False si no hay.
        """
        for columna in range(len(matriz_adn[0])):  # Recorre cada columna de la matriz
            secuencia_vertical = ''.join([fila[columna] for fila in matriz_adn])  # Construye la secuencia vertical de la columna
            for base in self.bases_nitrogenadas:  # Recorre cada base nitrogenada
                if base * self.longitud_minima_secuencia in secuencia_vertical:  # Verifica si hay 4 bases iguales consecutivas en la columna
                    return True  # Si encuentra una mutación, devuelve True
        return False  # Si no encuentra mutaciones en ninguna columna, devuelve False

    def detectar_mutante_diagonal(self, matriz_adn):
        """
        Detecta si hay un mutante diagonal en la matriz de ADN.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          True si hay un mutante diagonal, False si no hay.
        """
        # Diagonal principal y diagonales paralelas
        for i in range(len(matriz_adn) - self.longitud_minima_secuencia + 1):  # Recorre las diagonales principales y paralelas
            diagonal = ''.join([matriz_adn[j][i+j] for j in range(len(matriz_adn) - i)])  # Construye la secuencia de la diagonal
            for base in self.bases_nitrogenadas:  # Recorre cada base nitrogenada
                if base * self.longitud_minima_secuencia in diagonal:  # Verifica si hay 4 bases iguales consecutivas en la diagonal
                    return True  # Si encuentra una mutación, devuelve True
        # Diagonal secundaria y diagonales paralelas
        for i in range(1, len(matriz_adn) - self.longitud_minima_secuencia + 1):  # Recorre las diagonales secundarias y paralelas
            diagonal = ''.join([matriz_adn[j+i][j] for j in range(len(matriz_adn) - i)])  # Construye la secuencia de la diagonal
            for base in self.bases_nitrogenadas:  # Recorre cada base nitrogenada
                if base * self.longitud_minima_secuencia in diagonal:  # Verifica si hay 4 bases iguales consecutivas en la diagonal
                    return True  # Si encuentra una mutación, devuelve True
        return False  # Si no encuentra mutaciones en ninguna diagonal, devuelve False


class Mutador:
    """
    Superclase para las clases que crean mutaciones en el ADN.
    """
    def __init__(self, base_nitrogenada):
        """
        Constructor de la clase Mutador.
        Inicializa el atributo base_nitrogenada.
        """
        self.base_nitrogenada = base_nitrogenada  # Define la base nitrogenada que se usará para la mutación

    def crear_mutante(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method")  # Lanza un error si se llama a este método desde la superclase


class Radiacion(Mutador):
    """
    Clase que crea mutaciones horizontales o verticales en el ADN.
    """
    def __init__(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        """
        Constructor de la clase Radiacion.
        Inicializa los atributos base_nitrogenada, posicion_inicial y orientacion_de_la_mutacion.
        """
        super().__init__(base_nitrogenada)  # Llama al constructor de la superclase
        self.posicion_inicial = posicion_inicial  # Define la posición inicial de la mutación
        self.orientacion_de_la_mutacion = orientacion_de_la_mutacion  # Define la orientación de la mutación ("H" o "V")

    def crear_mutante(self, matriz_adn):
        """
        Crea una mutación horizontal o vertical en la matriz de ADN.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          La matriz de ADN con la mutación, o None si ocurre un error.
        """
        try:
            fila, columna = self.posicion_inicial  # Obtiene la fila y columna de la posición inicial
            if self.orientacion_de_la_mutacion == "H":
                # Mutar horizontalmente
                # Reemplaza 4 caracteres en la fila especificada con la base nitrogenada de la mutación
                return [fila[:columna] + self.base_nitrogenada * 4 + fila[columna + 4:] 
                        if i == fila else fila for i, fila in enumerate(matriz_adn)]
            elif self.orientacion_de_la_mutacion == "V":
                # Mutar verticalmente
                # Reemplaza el caracter en la columna especificada de cada fila con la base nitrogenada de la mutación
                return [fila[:columna] + self.base_nitrogenada + fila[columna + 1:] 
                        if fila <= fila + 3 else fila for i, fila in enumerate(matriz_adn)]
            else:
                raise ValueError("Orientación de mutación inválida")  # Lanza un error si la orientación no es "H" o "V"
        except (ValueError, IndexError) as e:
            print(f"Error al crear mutante: {e}")  # Imprime un mensaje de error si ocurre un error
            return None  # Devuelve None si ocurre un error


class Virus(Mutador):
    """
    Clase que crea mutaciones diagonales en el ADN.
    """
    def __init__(self, base_nitrogenada, posicion_inicial):
        """
        Constructor de la clase Virus.
        Inicializa los atributos base_nitrogenada y posicion_inicial.
        """
        super().__init__(base_nitrogenada)  # Llama al constructor de la superclase
        self.posicion_inicial = posicion_inicial  # Define la posición inicial de la mutación

    def crear_mutante(self, matriz_adn):
        """
        Crea una mutación diagonal en la matriz de ADN.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          La matriz de ADN con la mutación, o None si ocurre un error.
        """
        try:
            fila, columna = self.posicion_inicial  # Obtiene la fila y columna de la posición inicial
            # Mutar diagonalmente (principal)
            for i in range(4):  # Recorre 4 posiciones en la diagonal principal
                if 0 <= fila + i < len(matriz_adn) and 0 <= columna + i < len(matriz_adn[0]):  # Verifica si la posición está dentro de la matriz
                    # Reemplaza el caracter en la posición actual con la base nitrogenada de la mutación
                    matriz_adn[fila + i] = matriz_adn[fila + i][:columna + i] + self.base_nitrogenada + matriz_adn[fila + i][columna + i + 1:]
                else:
                    raise IndexError("Posición fuera de rango")  # Lanza un error si la posición está fuera de la matriz
            return matriz_adn  # Devuelve la matriz con la mutación
        except (ValueError, IndexError) as e:
            print(f"Error al crear mutante: {e}")  # Imprime un mensaje de error si ocurre un error
            return None  # Devuelve None si ocurre un error


class Sanador:
    """
    Clase encargada de sanar mutaciones en una secuencia de ADN.
    """
    def __init__(self):
        """
        Constructor de la clase Sanador.
        Inicializa el atributo detector.
        """
        self.detector = Detector()  # Crea una instancia de la clase Detector

    def sanar_mutantes(self, matriz_adn):
        """
        Sana las mutaciones en la matriz de ADN, si las hay.

        Args:
          matriz_adn: Una lista de strings que representa la matriz de ADN.

        Returns:
          La matriz de ADN sanada.
        """
        if self.detector.detectar_mutantes(matriz_adn):  # Verifica si hay mutaciones en la matriz
            return self.generar_adn_no_mutante()  # Si hay mutaciones, genera una nueva matriz sin mutaciones
        else:
            return matriz_adn  # Si no hay mutaciones, devuelve la matriz original

    def generar_adn_no_mutante(self):
        """
        Genera una nueva matriz de ADN sin mutaciones.

        Returns:
          Una nueva matriz de ADN sin mutaciones.
        """
        while True:  # Crea un bucle infinito
            nueva_matriz = []  # Crea una nueva lista para la matriz
            for _ in range(6):  # Crea 6 filas
                fila = ''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(6))  # Genera una fila aleatoria de 6 bases nitrogenadas
                nueva_matriz.append(fila)  # Agrega la fila a la matriz
            if not self.detector.detectar_mutantes(nueva_matriz):  # Verifica si la nueva matriz tiene mutaciones
                return nueva_matriz  # Si no tiene mutaciones, devuelve la nueva matriz