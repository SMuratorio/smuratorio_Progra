import matriz_peliculas, matriz_usuarios
# Matriz peliculas

contenido = []
proximo_id_peliculas = 1
continuar = 0

while continuar == 0:
    titulo = input("Ingrese el nombre de la película/serie: ")
    tipo = input("Indique si es una serie o película: ")
    genero = input("Indique el género: ")
    año = int(input("Indique su año de estreno: "))
    duracion = input("Indique la duración: ")

    conte = matriz_peliculas.crear_contenido_peliculas(contenido, proximo_id_peliculas, titulo, tipo, genero, año, duracion)
    proximo_id_peliculas+=1
    
    continuar = int(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if continuar == -1:
        continuar = -1


#print(cont)
print("\nContenido registrado:")
matriz_peliculas.leer_contenido_peliculas(contenido)

# Preguntar si se desea actualizar contenido
actualizar_opcion_peliculas = input("\n¿Desea actualizar contenido? (s/n): ").lower()

while actualizar_opcion_peliculas == 's':
    print("\nActualizar contenido:")

    nuevo_id_peliculas = int(input("Ingrese el ID de la película/serie a cambiar: "))
    print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

    nuevo_titulo = input("Nuevo título (deje en blanco para no cambiar): ")
    nuevo_tipo = input("Nuevo tipo (deje en blanco para no cambiar): ")
    nuevo_genero = input("Nuevo género (deje en blanco para no cambiar): ")
    nuevo_año_str = input("Nuevo año (deje en blanco para no cambiar): ")
    nuevo_duracion = input("Nueva duración (deje en blanco para no cambiar): ")

    # Convertir nuevo año a entero si no está vacío
    nuevo_año = int(nuevo_año_str) if nuevo_año_str else None

    matriz_peliculas.actualizar_contenido_peliculas(contenido, nuevo_id_peliculas, titulo=nuevo_titulo, tipo=nuevo_tipo, genero=nuevo_genero, año=nuevo_año, duracion=nuevo_duracion)

    print("\nContenido actualizado:")
    matriz_peliculas.leer_contenido_peliculas(contenido)
    
    # Preguntar si se desea seguir actualizando
    actualizar_opcion_peliculas = input("\n¿Desea seguir actualizando contenido? (s/n): ").lower()

# Preguntar si se desea eliminar contenido
eliminar_opcion_peliculas = input("\n¿Desea eliminar contenido? (s/n): ").lower()

while eliminar_opcion_peliculas == 's':
    print("\nEliminar contenido:")

    eliminar_id_peliculas = int(input("Ingrese el ID de la película/serie a eliminar: "))
    matriz_peliculas.eliminar_contenido_peliculas(contenido, eliminar_id_peliculas)

    print("\nContenido después de la eliminación:")
    matriz_peliculas.leer_contenido_peliculas(contenido)
    
    # Preguntar si se desea seguir eliminando
    eliminar_opcion_peliculas = input("\n¿Desea seguir eliminando contenido? (s/n): ").lower()

print("\nProceso finalizado.")


# Programa principal

#Recortar los títulos a un máximo de 8 caracteres
for i in range(len(contenido)):
    contenido[i][1] = contenido[i][1][:8]  #Recortar el título a 8 caracteres

# Ordenar la lista por año de estreno (ascendente)
peliculas_ordenadas = sorted(contenido, key=lambda x: x[4])

#crear matriz
matriz = matriz_peliculas.crear_matriz_peliculas (len(contenido),6)

#llenar matriz
matriz_peliculas.llenar_matriz_peliculas(matriz, peliculas_ordenadas)

#imprimir matriz
ids_peliculas=[item[1] for item in peliculas_ordenadas]  # Nombres de las películas/series
encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

matriz_peliculas.imprimir_matriz_peliculas(matriz, ids_peliculas, encabezado)





# Matriz de usuarios
contenido_usuarios = []
proximo_id_usuarios = 1
seguir = 0

while seguir == 0:
    nombre = input("Ingrese el nombre del usuario: ")
    apellido=input("Ingrese el apellido del usuario: ")
    dni = input("Ingrese el DNI del usuario: ")
    correo = input("Ingrese su correo electronico: ")
    
    conteni = matriz_usuarios.crear_contenido_usuarios(contenido_usuarios, proximo_id_usuarios, nombre, apellido, dni, correo)
    proximo_id_usuarios+=1
    
    seguir = int(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if seguir == -1:
        seguir = -1


#print(cont)
print("\nContenido registrado:")
matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)

# Preguntar si se desea actualizar contenido
actualizar_opcion_usuarios = input("\n¿Desea actualizar contenido? (s/n): ").lower()

while actualizar_opcion_usuarios == 's':
    print("\nActualizar contenido:")

    nuevo_id_usuarios = int(input("Ingrese el ID del usuario a cambiar: "))
    print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

    nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")
    nuevo_apellido = input("Nuevo apellido (deje en blanco para no cambiar): ")
    nuevo_dni_str = (input("Nuevo DNI (deje en blanco para no cambiar): "))
    nuevo_correo = input("Nuevo correo (deje en blanco para no cambiar): ")

    #Convertir nuevo año a entero si no está vacío
    nuevo_dni = int(nuevo_dni_str) if nuevo_dni_str else None

    matriz_usuarios.actualizar_contenido_usuarios(contenido_usuarios, nuevo_id_usuarios, nombre=nuevo_nombre, apellido=nuevo_apellido, dni=nuevo_dni, correo=nuevo_correo)

    print("\nContenido actualizado:")
    matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)
    
    # Preguntar si se desea seguir actualizando
    actualizar_opcion_usuarios = input("\n¿Desea seguir actualizando contenido? (s/n): ").lower()

# Preguntar si se desea eliminar contenido
eliminar_opcion_usuarios = input("\n¿Desea eliminar contenido? (s/n): ").lower()

while eliminar_opcion_usuarios == 's':
    print("\nEliminar contenido:")

    eliminar_id_usuarios = int(input("Ingrese el ID del usuario a eliminar: "))
    matriz_usuarios.eliminar_contenido_usuarios(contenido_usuarios, eliminar_id_usuarios)

    print("\nContenido después de la eliminación:")
    matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)
    
    # Preguntar si se desea seguir eliminando
    eliminar_opcion_usuarios = input("\n¿Desea seguir eliminando contenido? (s/n): ").lower()

print("\nProceso finalizado.")

# Programa principal
#Recortar los títulos a un máximo de 8 caracteres
for i in range(len(contenido_usuarios)):
    contenido_usuarios[i][1] = contenido_usuarios[i][1][:8]  #Recortar el nombre a 8 caracteres

# Ordenar la lista por año de estreno (ascendente)
usuarios_ordenados = sorted(contenido_usuarios, key=lambda x: x[1])

#crear matriz
matriz = matriz_usuarios.crear_matriz_usuarios (len(contenido_usuarios),5)

#llenar matriz
matriz_usuarios.llenar_matriz_usuarios(matriz, usuarios_ordenados)

#imprimir matriz
ids_usuarios=[item[1] for item in usuarios_ordenados]  # Nombres de los usuarios
encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido

matriz_usuarios.imprimir_matriz_usuarios(matriz, ids_usuarios, encabezado_usuarios)





