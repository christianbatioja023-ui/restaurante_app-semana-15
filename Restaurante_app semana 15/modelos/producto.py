class Producto:
    def __init__(self, id, nombre, precio):
        self.id = int(id)
        self.nombre = str(nombre).strip()
        self.precio = float(precio)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["nombre"],
            data["precio"]
        )