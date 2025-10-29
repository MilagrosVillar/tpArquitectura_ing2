from datos.libro_dao import LibroDAO
from modelos.libro import Libro

class GestorLibros:
    def __init__(self):
        self.dao = LibroDAO()

    def agregar_libro(self, titulo, autor):
        libro = Libro(titulo, autor, True)
        self.dao.agregar(libro)

    def mostrar_libros(self):
        return self.dao.listar()
