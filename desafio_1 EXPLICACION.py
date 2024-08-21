import random

def crear_matriz (n, m):
    """
    pre: recibe n y m. Donde n: filas y m:columnas
    pos: devuelve una matriz de NxM creada con ceros
    
    """
    return [[0]*m for fil in range (n)]
    #crea una lista de m ceros
    #el for se ejecuta n veces (una vez por fila)

    #Juntando todo, esto crea una lista de listas (una matriz). P
    #Para cada iteración del bucle, se genera una fila de m ceros, y esto se repite n veces, generando n filas en total.


def llenar_matriz (m):
    """
    pre: recibe una matriz ya creada.
    pos: llena la matriz con valores aleatorios entre 1 y 10.

    """
    filas = len (m) # Cantidad de filas - devuelve el número de filas de la matriz
    columnas = len (m [0]) # Cantidad de columnas - evuelve el número de elementos (columnas) en la primera fila de la matriz.
    for fil in range (filas): #Recorre cada fila de la matriz
        for col in range (columnas): #Para cada fila, recorre cada columna
            num_aleatorio = random.randint (1, 10)
            m [fil][col] = num_aleatorio #El número aleatorio generado se asigna a la posición correspondiente en la matriz.


def imprimir_matriz (matriz, estudiantes, materias):
    """
    pre: recibe una matriz ya creada.
    pos: muestra por consola los elementos de la matriz.
    
    """
    # Imprimir el encabezado de las materias
    print(" " * 12, end="")  # Espacio para alinear con los nombres de los estudiantes, se imprime 12 espacios en blanco
                            #Este espacio es necesario porque cada fila de datos comenzará con el nombre de un estudiante que ocupa el lugar de
                            #12 caracteres(ajustable según la longitud del nombre más largo).
    for materia in materias: #Se itera a través de cada materia en la lista materias
        print(f"{materia:>20}", end="") #Dentro del bucle, cada materia se imprime alineada a la derecha (>) en un espacio de 20 caracteres 
                                        #Este espacio asegura que los nombres de las materias se alineen correctamente sobre las columnas de datos.
    print()

    # Imprimir cada fila con el nombre del estudiante como encabezado
    for i in range(len(matriz)): #Se itera a través de cada fila de la matriz. El índice i representa la fila actual.
        print(f"{estudiantes[i]:<12}", end="")  # Encabezado del estudiante. Para cada fila, se imprime el nombre del estudiante correspondiente (estudiantes[i])
                                                 #alineado a la izquierda (<) en un espacio de 12 caracteres (12).
        for j in range(len(matriz[i])): #Dentro de cada fila, se itera a través de cada columna. El índice j representa la columna actual.
            print(f"{matriz[i][j]:>20}", end="") #Se imprime cada elemento de la matriz (matriz[i][j]) alineado a la derecha (>) 
                                                #dentro de un espacio de 20 caracteres.
        print()

    #NO LO USAMOS
    """filas = len (matriz) #Obtiene el número de filas de la matriz
    columnas = len (matriz [0]) #Obtiene el número de columnas de la matriz, tomando la longitud de la primera fila.
    #Calcula la longitud de esta lista, que es 3. Esto nos dice cuántas columnas tiene la matriz

    for fil in range (filas): #Recorre cada fila de la matriz.
        for col in range (columnas): #Dentro de cada fila, recorre cada columna
            print ("%3d" % matriz [fil][col], end= "") 
            #Este formato de cadena imprime cada número con un ancho fijo de 3 caracteres, alineado a la derecha
        print ()"""

def calcular_promedio_estudiantes(matriz):
    print("Promedio de calificaciones por estudiante:")
    for i in range(len(matriz)): #filas
        suma = 0
        for j in range(len(matriz[i])): #Devuelve el número de calificaciones (columnas) que tiene el estudiante i.
            suma += matriz[i][j] #Se suma cada calificación del estudiante a la variable suma.
        promedio = suma / len(matriz[i])
        print(f"{estudiantes[i]}: {promedio:.2f}")

def calcular_promedio_materias(matriz):
    print("Promedio de calificaciones por materia:")
    for j in range(len(materias)):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        promedio = suma / len(matriz)
        print(f"{materias[j]}: {promedio:.2f}")



# Programa principal
estudiantes=["Juliana", "Ayelen", "Sofia", "Barbara", "Daiana", "Martina", "Delfina", "Juan", "Mateo", "Emma"]
materias=["Programacion", "Algebra", "Quimica", "Teorias", "Sistemas"]
matriz = crear_matriz (10, 5)
llenar_matriz (matriz)
imprimir_matriz (matriz, estudiantes, materias)

# 4. Calcular y mostrar los promedios
calcular_promedio_estudiantes(matriz)
calcular_promedio_materias(matriz)

