from datos.conexion import Conexion

class SocioDAO:
    def __init__(self):
        self.db = Conexion()

    def agregar(self, socio):
        self.db.ejecutar("INSERT INTO socios (nombre, email) VALUES (?, ?)",
                         (socio.nombre, socio.email))

    def listar(self):
        resultado = self.db.ejecutar("SELECT * FROM socios")
        return resultado.fetchall()
