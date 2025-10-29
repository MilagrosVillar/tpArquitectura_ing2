from logica_negocio.gestor_libros import GestorLibros
from logica_negocio.gestor_socios import GestorSocios
from logica_negocio.gestor_prestamos import GestorPrestamos
from presentación.validaciones import validar_email, validar_texto

class InterfazUsuario:
    def __init__(self):
        self.libros = GestorLibros()
        self.socios = GestorSocios()
        self.prestamos = GestorPrestamos()

    def menu(self):
        while True:
            print("\n📚 Sistema de Biblioteca")
            print("1. Registrar socio")
            print("2. Agregar libro")
            print("3. Mostrar libros")
            print("4. Registrar préstamo")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_socio()
            elif opcion == "2":
                self.agregar_libro()
            elif opcion == "3":
                self.mostrar_libros()
            elif opcion == "4":
                self.registrar_prestamo()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("❌ Opción inválida.")

    def registrar_socio(self):
        nombre = input("Nombre del socio: ")
        email = input("Email: ")

        if validar_texto(nombre) and validar_email(email):
            self.socios.registrar_socio(nombre, email)
            print("✅ Socio registrado correctamente.")
        else:
            print("❌ Datos inválidos.")

    def agregar_libro(self):
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        if validar_texto(titulo) and validar_texto(autor):
            self.libros.agregar_libro(titulo, autor)
            print("✅ Libro agregado correctamente.")
        else:
            print("❌ Datos inválidos.")

    def mostrar_libros(self):
        libros = self.libros.mostrar_libros()
        print("\n📖 Lista de libros:")
        for libro in libros:
            print(f"{libro[0]} - {libro[1]} ({libro[2]}) - {'Disponible' if libro[3] else 'Prestado'}")

    def registrar_prestamo(self):
        socio_id = int(input("ID del socio: "))
        libro_id = int(input("ID del libro: "))
        self.prestamos.registrar_prestamo(socio_id, libro_id)
        print("✅ Préstamo registrado.")
