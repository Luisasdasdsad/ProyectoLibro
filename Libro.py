import os

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        if not isinstance(titulo, str):
            raise ValueError("El título debe ser una cadena de caracteres.")
        if not titulo:
            raise ValueError("El libro debe tener un título.")
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena de caracteres.")
        if not autor:
            raise ValueError("El libro debe tener un autor.")
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        raise ValueError(f"No se encontró ningún libro con el título '{titulo}'.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")

def main():
    biblioteca = Biblioteca()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Buscar libro por título")
        print("3. Mostrar todos los libros")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                titulo = input("Ingrese el título del libro: ")
                if titulo.isdigit():
                    raise ValueError("El título no puede ser un número.")
                autor = input("Ingrese el autor del libro: ")
                if autor.isdigit():
                    raise ValueError("El autor no puede ser un número.")
                año_publicacion = input("Ingrese el año de publicación del libro: ")

                libro = Libro(titulo, autor, año_publicacion)
                biblioteca.agregar_libro(libro)
            except ValueError as e:
                print(e)
            input("Presione Enter para continuar...")

        elif opcion == "2":
            titulo = input("Ingrese el título del libro a buscar: ")
            try:
                libro_encontrado = biblioteca.buscar_libro(titulo)
                print(f"Libro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")
            except ValueError as e:
                print(e)
            input("Presione Enter para continuar...")

        elif opcion == "3":
            biblioteca.mostrar_libros()
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()