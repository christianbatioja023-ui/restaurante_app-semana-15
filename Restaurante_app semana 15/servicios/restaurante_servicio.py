from pathlib import Path
from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


BASE_DIR = Path(__file__).resolve().parent.parent

PRODUCTOS_FILE = BASE_DIR / "datos" / "productos.json"
USUARIOS_FILE = BASE_DIR / "datos" / "usuarios.json"
VENTAS_FILE = BASE_DIR / "datos" / "ventas.json"


class RestauranteServicio:

    def __init__(self):
        self.archivo = ArchivoServicio()

    # =========================
    # PRODUCTOS
    # =========================

    def listar_productos(self):
        datos = self.archivo.cargar(PRODUCTOS_FILE)

        return [
            Producto.from_dict(item)
            for item in datos
        ]

    def obtener_producto(self, producto_id):
        try:
            producto_id = int(producto_id)
        except (TypeError, ValueError):
            return None

        productos = self.listar_productos()

        for producto in productos:
            if producto.id == producto_id:
                return producto

        return None

    def buscar_productos(self, texto):
        texto = str(texto).strip().lower()

        if not texto:
            return []

        productos = self.listar_productos()

        return [
            producto
            for producto in productos
            if texto in producto.nombre.lower()
        ]

    def registrar_producto(self, nombre, precio):
        nombre = str(nombre).strip()

        if not nombre:
            raise ValueError(
                "El nombre del producto es obligatorio."
            )

        try:
            precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser numérico."
            )

        if precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        productos = self.listar_productos()

        if productos:
            nuevo_id = max(
                producto.id for producto in productos
            ) + 1
        else:
            nuevo_id = 1

        producto = Producto(
            nuevo_id,
            nombre,
            precio
        )

        productos.append(producto)

        self.archivo.guardar(
            PRODUCTOS_FILE,
            [
                item.to_dict()
                for item in productos
            ]
        )

        return producto

    def actualizar_producto(
        self,
        producto_id,
        nombre,
        precio
    ):
        producto = self.obtener_producto(producto_id)

        if producto is None:
            raise ValueError(
                "No existe el producto seleccionado."
            )

        nombre = str(nombre).strip()

        if not nombre:
            raise ValueError(
                "El nombre del producto es obligatorio."
            )

        try:
            precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser numérico."
            )

        if precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        productos = self.listar_productos()

        for item in productos:
            if item.id == producto.id:
                item.nombre = nombre
                item.precio = precio

        self.archivo.guardar(
            PRODUCTOS_FILE,
            [
                item.to_dict()
                for item in productos
            ]
        )

        return producto

    def eliminar_producto(self, producto_id):
        producto = self.obtener_producto(producto_id)

        if producto is None:
            raise ValueError(
                "No existe el producto seleccionado."
            )

        productos = self.listar_productos()

        productos = [
            item
            for item in productos
            if item.id != producto.id
        ]

        self.archivo.guardar(
            PRODUCTOS_FILE,
            [
                item.to_dict()
                for item in productos
            ]
        )

    # =========================
    # USUARIOS
    # =========================

    def listar_usuarios(self):
        datos = self.archivo.cargar(USUARIOS_FILE)

        return [
            Usuario.from_dict(item)
            for item in datos
        ]

    def obtener_usuario(self, usuario_id):
        try:
            usuario_id = int(usuario_id)
        except (TypeError, ValueError):
            return None

        usuarios = self.listar_usuarios()

        for usuario in usuarios:
            if usuario.id == usuario_id:
                return usuario

        return None

    def registrar_usuario(
        self,
        nombre,
        usuario,
        password
    ):
        nombre = str(nombre).strip()
        usuario = str(usuario).strip()
        password = str(password).strip()

        if not nombre:
            raise ValueError(
                "El nombre es obligatorio."
            )

        if not usuario:
            raise ValueError(
                "El usuario es obligatorio."
            )

        if not password:
            raise ValueError(
                "La contraseña es obligatoria."
            )

        usuarios = self.listar_usuarios()

        for item in usuarios:
            if item.usuario.lower() == usuario.lower():
                raise ValueError(
                    "El nombre de usuario ya existe."
                )

        if usuarios:
            nuevo_id = max(
                item.id for item in usuarios
            ) + 1
        else:
            nuevo_id = 1

        nuevo_usuario = Usuario(
            nuevo_id,
            nombre,
            usuario,
            password
        )

        usuarios.append(nuevo_usuario)

        self.archivo.guardar(
            USUARIOS_FILE,
            [
                item.to_dict()
                for item in usuarios
            ]
        )

        return nuevo_usuario

    def validar_login(self, usuario, password):
        usuario = str(usuario).strip()
        password = str(password).strip()

        if not usuario or not password:
            return None

        usuarios = self.listar_usuarios()

        for item in usuarios:
            if (
                item.usuario == usuario
                and item.password == password
            ):
                return item

        return None

    # =========================
    # VENTAS
    # =========================

    def listar_ventas(self):
        datos = self.archivo.cargar(VENTAS_FILE)

        return [
            Venta.from_dict(item)
            for item in datos
        ]

    def registrar_venta(
        self,
        usuario_id,
        producto_id
    ):
        try:
            usuario_id = int(usuario_id)
            producto_id = int(producto_id)
        except (TypeError, ValueError):
            raise ValueError(
                "El usuario y el producto deben ser válidos."
            )

        usuario = self.obtener_usuario(usuario_id)

        if usuario is None:
            raise ValueError(
                "No existe el usuario seleccionado."
            )

        producto = self.obtener_producto(producto_id)

        if producto is None:
            raise ValueError(
                "No existe el producto seleccionado."
            )

        ventas = self.listar_ventas()

        if ventas:
            nuevo_id = max(
                venta.id for venta in ventas
            ) + 1
        else:
            nuevo_id = 1

        fecha = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        venta = Venta(
            nuevo_id,
            usuario.nombre,
            producto.nombre,
            fecha
        )

        ventas.append(venta)

        self.archivo.guardar(
            VENTAS_FILE,
            [
                item.to_dict()
                for item in ventas
            ]
        )

        return venta

    def ventas_por_usuario(self, usuario_id):
        usuario = self.obtener_usuario(usuario_id)

        if usuario is None:
            raise ValueError(
                "No existe el usuario seleccionado."
            )

        ventas = self.listar_ventas()

        return [
            venta
            for venta in ventas
            if venta.usuario == usuario.nombre
        ]
