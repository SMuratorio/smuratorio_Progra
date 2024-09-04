def crear_matriz (n, m):
    """
    pre: recibe n y m. Donde n: filas y m:columnas
    pos: devuelve una matriz de NxM creada con ceros
    
    """
    return [[0]*m for fil in range (n)]

def llenar_matriz (m):
    """
    pre: recibe una matriz ya creada.
    pos: llena la matriz con valores aleatorios entre 1 y 10.

    """
    filas = len (m) # Cantidad de filas - devuelve el número de filas de la matriz
    columnas = len (m [0]) # Cantidad de columnas - evuelve el número de elementos (columnas) en la primera fila de la matriz.
    for fil in range (filas): #Recorre cada fila de la matriz
        for col in range (columnas): #Para cada fila, recorre cada columna
            m [fil][col] = contenido
            
            
def crear_contenido(contenido, proximo_id, titulo, tipo, genero, año, duracion):
    item = {
        'id': proximo_id,
        'titulo': titulo,
        'tipo': tipo,  # Puede ser 'Película' o 'Serie'
        'genero': genero,
        'año': año,
        'duracion': duracion
    }

    contenido.append(item)
    print(f"La {tipo} '{titulo}' creada con ID {item['id']}.")

    return proximo_id + 1

def leer_contenido(contenido):
    if not contenido:
        print("No hay contenido registrado.")
        return
    for item in contenido:
        print(f"ID: {item['id']}, Título: {item['titulo']}, Tipo: {item['tipo']}, Género: {item['genero']}, Año: {item['año']}, Duración: {item['duracion']}")

def actualizar_contenido(contenido, item_id, titulo=None, tipo=None, genero=None, año=None, duracion=None):
    for item in contenido:
        if item['id'] == item_id:
            if titulo is not None:
                item['titulo'] = titulo
            if tipo is not None:
                item['tipo'] = tipo
            if genero is not None:
                item['genero'] = genero
            if año is not None:
                item['año'] = año
            if duracion is not None:
                item['duracion'] = duracion
            print(f"{item['tipo']} con ID {item_id} actualizada.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")

def imprimir_matriz(matriz, proximo_id, contenido):
    
    print(" " * 12, end="") 
    for cont in contenido: 
        print(f"{cont:>20}", end="")
    print()

    
    for i in range(len(matriz)):
        print(f"{proximo_id[i]:<12}", end="")  
        for j in range(len(matriz[i])): 
            print(f"{matriz[i][j]:>20}", end="") 
        print()
        
contenido = []
proximo_id = 1
continuar = 0

while continuar == 0:
    titulo = input("Ingrese el nombre de la película/serie: ")
    tipo = input("Indique si es una serie o película: ")
    genero = input("Indique el género: ")
    año = int(input("Indique su año de estreno: "))
    duracion = input("Indique la duración: ")

    proximo_id = crear_contenido(contenido, proximo_id, titulo, tipo, genero, año, duracion)
    
    continuar = int(input("Si desea continuar ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if continuar == -1:
        continuar = -1

print("\nContenido registrado:")
leer_contenido(contenido)

"""
# Actualizar contenido
print("\nActualizar contenido:")

nuevo_id = int(input("Ingrese el ID de la película/serie a cambiar: "))
print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

nuevo_titulo = input("Nuevo título: ")
nuevo_tipo = input("Nuevo tipo: ")
nuevo_genero = input("Nuevo género: ")
nuevo_año_str = input("Nuevo año: ")
nuevo_duracion = input("Nueva duración: ")


# Convertir nuevo año a entero si no está vacío
nuevo_año = int(nuevo_año_str) if nuevo_año_str else None

actualizar_contenido(contenido, nuevo_id, titulo=nuevo_titulo, tipo=nuevo_tipo, genero=nuevo_genero, año=nuevo_año, duracion=nuevo_duracion)

print("\nContenido actualizado:")
leer_contenido(contenido)
""" 

#Crear matriz
matriz = crear_matriz(proximo_id, 6)
#Imprimir matriz
llenar_matriz(matriz)
imprimir_matriz(matriz, proximo_id, contenido)