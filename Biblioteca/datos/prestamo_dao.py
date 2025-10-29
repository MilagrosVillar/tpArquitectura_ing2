from datos.conexion import Conexion

class PrestamoDAO:
    def __init__(self):
        self.db = Conexion()

    def registrar(self, socio_id, libro_id, fecha):
        self.db.ejecutar("INSERT INTO prestamos (socio_id, libro_id, fecha) VALUES (?, ?, ?)",
                         (socio_id, libro_id, fecha))

