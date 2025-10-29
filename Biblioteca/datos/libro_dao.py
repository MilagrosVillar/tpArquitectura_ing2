from datos.conexion import Conexion

class LibroDAO:
    def __init__(self):
        self.db = Conexion()

    def agregar(self, libro):
        self.db.ejecutar("INSERT INTO libros (titulo, autor, disponible) VALUES (?, ?, ?)",
                         (libro.titulo, libro.autor, libro.disponible))

    def listar(self):
        resultado = self.db.ejecutar("SELECT * FROM libros")
        return resultado.fetchall()
