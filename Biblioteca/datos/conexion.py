import sqlite3

class Conexion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Conexion, cls).__new__(cls)
            cls._instancia._conectar()
        return cls._instancia

    def _conectar(self):
        self.conexion = sqlite3.connect("biblioteca.db")
        self.cursor = self.conexion.cursor()
        self._crear_tablas()

    def _crear_tablas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS socios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                email TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                disponible INTEGER
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                socio_id INTEGER,
                libro_id INTEGER,
                fecha TEXT,
                FOREIGN KEY(socio_id) REFERENCES socios(id),
                FOREIGN KEY(libro_id) REFERENCES libros(id)
            );
        """)
        self.conexion.commit()

    def ejecutar(self, query, parametros=()):
        self.cursor.execute(query, parametros)
        self.conexion.commit()
        return self.cursor

    def cerrar(self):
        self.conexion.close()
        Conexion._instancia = None
