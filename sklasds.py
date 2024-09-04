import random

def crear_matriz(n, m):
    """
    pre: recibe n y m. Donde n: filas y m: columnas
    pos: devuelve una matriz de NxM creada con ceros
    """
    return [[0]*m for _ in range(n)]

def llenar_matriz(matriz, contenido):
    """
    pre: recibe una matriz ya creada y una lista de contenido.
    pos: llena la matriz con los datos del contenido. Asume que hay suficientes espacios en la matriz.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    idx = 0

    for fil in range(filas):
        for col in range(columnas):
            if idx < len(contenido):
                matriz[fil][col] = contenido[idx]['titulo']  # Puedes cambiar 'titulo' por otro campo si lo prefieres
                idx += 1
            else:
                matriz[fil][col] = ""  # Deja el espacio vacío si no hay más contenido

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

def imprimir_matriz(matriz, contenido):
    print(" " * 12, end="") 
    for cont in contenido: 
        print(f"{cont['titulo']:>20}", end="")
    print()

    for i in range(len(matriz)):
        print(f"{i:<12}", end="")  
        for j in range(len(matriz[i])): 
            print(f"{matriz[i][j]:>20}", end="") 
        print()

# Código principal
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

# Crear matriz
matriz = crear_matriz(len(contenido) // 6 + 1, 6)  # Asegúrate de que la matriz tenga el tamaño adecuado
# Llenar matriz con contenido
llenar_matriz(matriz, contenido)
# Imprimir matriz
imprimir_matriz(matriz, contenido)


