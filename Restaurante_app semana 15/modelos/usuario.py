class Usuario:
    def __init__(self, id, nombre, usuario, password):
        self.id = int(id)
        self.nombre = str(nombre).strip()
        self.usuario = str(usuario).strip()
        self.password = str(password).strip()

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["nombre"],
            data["usuario"],
            data["password"]
        )