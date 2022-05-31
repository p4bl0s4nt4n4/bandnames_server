import uuid

class Banda:
    id: str
    nombre: str
    votos: int

    def __init__(self, nombre) -> None:
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.votos = 0