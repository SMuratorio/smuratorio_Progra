#Creo una lista de películas:

# Id, Título, Género, fecha estreno, promedio, duración(en serie es cantidad de temporadas) 

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

def actualizar_contenido(contenido, item_id, titulo=None, tipo=None, genero=None, año=None):
    for item in contenido:
        if item['id'] == item_id:
            if titulo:
                item['titulo'] = titulo
            if tipo:
                item['tipo'] = tipo
            if genero:
                item['genero'] = genero
            if año:
                item['año'] = año
            print(f"{item['tipo']} con ID {item_id} actualizada.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")

contenido = []
proximo_id = 1
continuar = 0

while continuar == 0:
    
    titulo=input("Ingrese el nombre de la pelicula/serie: ")
    tipo=input("Indique si es una serie o pelicula: ")
    genero=input("Indique el genero: ")
    año=int(input("Indique su año de estreno: "))
    duracion=input("Indique la duracion: ")

    proximo_id=crear_contenido(contenido, proximo_id, titulo, tipo, genero, año, duracion)
    
    continuar = int(input("Si desea continuar ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if continuar == -1:
        continuar = -1

print("\nContenido registrado:")
leer_contenido(contenido)

# Actualizar contenido
print("\nActualizar contenido con ID 1:")

#Nuevo ingreso:

nuevo_id = int(input("Ingrese el id de la película/serie a cambiar: "))
print("¿Qué desea modificar?")

actualizar_contenido(contenido, nuevo_id , titulo="Origen", año=2010)