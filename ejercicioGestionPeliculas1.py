def menu():
    imprimir_caracteres_separacion()
    eleccion_usuario = int(input("Elige la acción que deseas realizar: \n" \
    "1.Añadir películas. \n" \
    "2. Eliminar películas. \n" \
    "3. Mostrar lista de películas. \n" \
    "4. Buscar películas. \n" \
    "5. Salir del programa \n"))
    if eleccion_usuario >= 1 and eleccion_usuario <=5:
        return eleccion_usuario
    else: 
        print("Caracter no permitido. Vuelva a intentarlo")

def peliculas_minusculas(pelicula):
    return pelicula.lower().strip()

def imprimir_caracteres_separacion():
    print(6*"=")

def aniadir_pelicula(peliculas):
    imprimir_caracteres_separacion()
    pelicula_usuario = input("Introduce el nombre de la película: ")
    pelicula_guardada = peliculas_minusculas(pelicula_usuario)
    if pelicula_guardada not in peliculas and pelicula_guardada is not None:
        peliculas.append(pelicula_guardada)
    print(f"{pelicula_usuario} añadida con éxito.")

def eliminar_pelicula(peliculas):
    imprimir_caracteres_separacion()
    pelicula_usuario = input("¿Qué película deseas eliminar? ")
    pelicula_eliminar = peliculas_minusculas(pelicula_usuario)
    if pelicula_eliminar not in peliculas:
        print("Película no encontrada")
    else:
        pelicula_eliminada = peliculas.pop(pelicula_eliminar)
        print(f"{pelicula_eliminada} eliminada con éxito")

def mostrar_lista_peliculas(peliculas):
    imprimir_caracteres_separacion()
    print("Lista de películas guardadas:")
    for pelicula in peliculas:
        print(pelicula.capitalize())

def buscar_peliculas(peliculas):
    imprimir_caracteres_separacion()
    pelicula_usuario = input("¿Qué película deseas buscar? ")
    pelicula_buscar = peliculas_minusculas(pelicula_usuario)
    
    for pelicula_lista in peliculas:
        if pelicula_buscar == pelicula_lista:
            print(f"{pelicula_usuario} encontrada en la lista")

    
def main():
    lista_peliculas = []
    respuesta_usuario = menu()
    while True:
        if(respuesta_usuario == 1):
            aniadir_pelicula(lista_peliculas)
        elif(respuesta_usuario == 2):
            eliminar_pelicula(lista_peliculas)
        elif(respuesta_usuario == 3):
            mostrar_lista_peliculas(lista_peliculas)
        elif(respuesta_usuario == 4):
            buscar_peliculas(lista_peliculas)
        elif (respuesta_usuario == 5):
            print("Saliendo del programa...")
            break
        respuesta_usuario = menu()

            


if __name__ == "__main__":
    main()