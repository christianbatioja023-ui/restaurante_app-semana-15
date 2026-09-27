class Venta:
    def __init__(self, id, usuario, producto, fecha):
        self.id = int(id)
        self.usuario = str(usuario).strip()
        self.producto = str(producto).strip()
        self.fecha = str(fecha).strip()

    def to_dict(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["usuario"],
            data["producto"],
            data["fecha"]
        )