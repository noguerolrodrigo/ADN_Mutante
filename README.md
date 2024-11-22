ADN Mutante

Este programa analiza secuencias de ADN representadas en matrices 6x6 para detectar mutaciones, generar mutaciones o sanarlas.

Participantes: NOGUEROL Rodrigo Jesus, KOGAN Gabriel

Cómo ejecutar el programa

1.  Clona el repositorio: git clone https://github.com/noguerolrodrigo/ADN_Mutante.git
2.  Navega la carpeta del proyecto
3.  Ejecuta el programa: python ejecutable.py
4.  Sigue las instrucciones en pantalla para ingresar la secuencia de ADN y seleccionar la acción deseada.

Funcionamiento del programa:

1° Hay que ingresar 6 secuencias de 6 caracteres que representan la matriz del ADN en una lista.
2° El programa pregunta que queremos hacer con esa matriz, donde nosotros escribiremos una de las opciones.
3° Segun las opciones el codigo ejecutara distintos metodos: 
-detectar: Detectará si la matriz ingresada es mutante o no.
-mutar: Pedirá una base nitrogenada, que se agrega a la matriz, haciendo que esta mute
-sanar: Cambiará la matriz mutante para que quede con la base nitrogenada de forma equilibrada, para que no sea mutante
-salir Se saldrá del programa
4° El programa nos mostrará el resultado de la acción realizada.

Ejemplo

Entrada:

Ingrese la secuencia de ADN (6 filas de 6 caracteres, ejemplo: AGATCA):

TTTTCA
GATTCA
CAATAT
GAGTTA
ATTGCG
CTGTTC

Seleccione una acción:

1. Detectar mutantes
2. Mutar
3. Sanar

1

Salida:

¡ADN mutante detectado!
