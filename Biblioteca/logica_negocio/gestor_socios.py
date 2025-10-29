from datos.socio_dao import SocioDAO
from modelos.socio import Socio

class GestorSocios:
    def __init__(self):
        self.dao = SocioDAO()

    def registrar_socio(self, nombre, email):
        socio = Socio(nombre, email)
        self.dao.agregar(socio)

    def listar_socios(self):
        return self.dao.listar()
