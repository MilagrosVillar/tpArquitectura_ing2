from datos.prestamo_dao import PrestamoDAO
from datetime import datetime

class GestorPrestamos:
    def __init__(self):
        self.dao = PrestamoDAO()

    def registrar_prestamo(self, socio_id, libro_id):
        fecha = datetime.now().strftime("%Y-%m-%d")
        self.dao.registrar(socio_id, libro_id, fecha)
