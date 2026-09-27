import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class MainView:

    def __init__(self, root, servicio, usuario_actual):

        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.base_dir = Path(__file__).resolve().parent.parent
        self.assets_dir = self.base_dir / "assets"

        self.root.title("Restaurante App - Sistema")
        self.root.geometry("950x680")
        self.root.resizable(False, False)

        self.crear_menu()
        self.crear_interfaz()

        self.cargar_usuarios()
        self.cargar_productos()
        self.cargar_ventas()

    # ==================================================
    # MENÚ PRINCIPAL
    # ==================================================

    def crear_menu(self):

        barra_menu = tk.Menu(self.root)

        menu_opciones = tk.Menu(
            barra_menu,
            tearoff=0
        )

        menu_opciones.add_command(
            label="1. Registrar producto",
            command=self.registrar_producto
        )

        menu_opciones.add_command(
            label="2. Listar productos",
            command=self.listar_productos
        )

        menu_opciones.add_command(
            label="3. Buscar producto",
            command=self.buscar_producto
        )

        menu_opciones.add_command(
            label="4. Actualizar producto",
            command=self.actualizar_producto
        )

        menu_opciones.add_command(
            label="5. Eliminar producto",
            command=self.eliminar_producto
        )

        menu_opciones.add_separator()

        menu_opciones.add_command(
            label="6. Registrar usuario",
            command=self.registrar_usuario
        )

        menu_opciones.add_command(
            label="7. Listar usuarios",
            command=self.listar_usuarios
        )

        menu_opciones.add_separator()

        menu_opciones.add_command(
            label="8. Realizar venta",
            command=self.mostrar_ventas
        )

        menu_opciones.add_command(
            label="9. Consultar ventas de un usuario",
            command=self.consultar_ventas_usuario
        )

        menu_opciones.add_separator()

        menu_opciones.add_command(
            label="10. Salir",
            command=self.salir
        )

        barra_menu.add_cascade(
            label="Menú",
            menu=menu_opciones
        )

        self.root.config(
            menu=barra_menu
        )

    # ==================================================
    # INTERFAZ PRINCIPAL
    # ==================================================

    def crear_interfaz(self):

        contenedor = ttk.Frame(
            self.root,
            padding=20
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        # --------------------------
        # LOGO
        # --------------------------

        ruta_logo = (
            self.assets_dir /
            "logo_restaurante.png"
        )

        try:

            self.logo = tk.PhotoImage(
                file=str(ruta_logo)
            )

            self.logo = self.logo.subsample(
                4,
                4
            )

            etiqueta_logo = ttk.Label(
                contenedor,
                image=self.logo
            )

            etiqueta_logo.pack(
                pady=(0, 5)
            )

        except tk.TclError:

            ttk.Label(
                contenedor,
                text="RESTAURANTE APP",
                font=("Arial", 20, "bold")
            ).pack(
                pady=(0, 5)
            )

        ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        ).pack(
            pady=(0, 5)
        )

        ttk.Label(
            contenedor,
            text=f"Usuario: {self.usuario_actual.nombre}",
            font=("Arial", 11)
        ).pack(
            pady=(0, 15)
        )

        # ==================================================
        # SECCIÓN DE VENTA
        # ==================================================

        marco_venta = ttk.LabelFrame(
            contenedor,
            text="Realizar venta",
            padding=15
        )

        marco_venta.pack(
            fill="x",
            pady=(0, 15)
        )

        ruta_icono = (
            self.assets_dir /
            "icono_venta.png"
        )

        try:

            self.icono_venta = tk.PhotoImage(
                file=str(ruta_icono)
            )

            self.icono_venta = (
                self.icono_venta.subsample(
                    8,
                    8
                )
            )

            ttk.Label(
                marco_venta,
                image=self.icono_venta
            ).grid(
                row=0,
                column=0,
                rowspan=2,
                padx=10,
                pady=5
            )

            columna = 1

        except tk.TclError:

            columna = 0

        ttk.Label(
            marco_venta,
            text="Usuario:"
        ).grid(
            row=0,
            column=columna,
            padx=10,
            pady=8
        )

        self.combo_usuario = ttk.Combobox(
            marco_venta,
            state="readonly",
            width=25
        )

        self.combo_usuario.grid(
            row=0,
            column=columna + 1,
            padx=10,
            pady=8
        )

        ttk.Label(
            marco_venta,
            text="Producto:"
        ).grid(
            row=0,
            column=columna + 2,
            padx=10,
            pady=8
        )

        self.combo_producto = ttk.Combobox(
            marco_venta,
            state="readonly",
            width=25
        )

        self.combo_producto.grid(
            row=0,
            column=columna + 3,
            padx=10,
            pady=8
        )

        ttk.Button(
            marco_venta,
            text="Registrar venta",
            command=self.registrar_venta
        ).grid(
            row=1,
            column=columna,
            columnspan=4,
            pady=10
        )

        # ==================================================
        # TABLA DE VENTAS
        # ==================================================

        marco_ventas = ttk.LabelFrame(
            contenedor,
            text="Ventas registradas",
            padding=15
        )

        marco_ventas.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "id",
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            marco_ventas,
            columns=columnas,
            show="headings",
            height=13
        )

        self.tabla_ventas.heading(
            "id",
            text="ID"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tabla_ventas.column(
            "usuario",
            width=230
        )

        self.tabla_ventas.column(
            "producto",
            width=230
        )

        self.tabla_ventas.column(
            "fecha",
            width=230
        )

        self.tabla_ventas.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # BARRA DE ESTADO
        # ==================================================

        self.barra_estado = ttk.Label(
            contenedor,
            text="Sistema listo.",
            relief="sunken",
            anchor="w"
        )

        self.barra_estado.pack(
            fill="x",
            pady=(10, 0)
        )

    # ==================================================
    # CARGAR DATOS
    # ==================================================

    def cargar_usuarios(self):

        self.usuarios = self.servicio.listar_usuarios()

        opciones = [
            f"{usuario.id} - {usuario.nombre}"
            for usuario in self.usuarios
        ]

        self.combo_usuario["values"] = opciones

        if opciones:
            self.combo_usuario.current(0)

    def cargar_productos(self):

        self.productos = (
            self.servicio.listar_productos()
        )

        opciones = [
            f"{producto.id} - "
            f"{producto.nombre} - "
            f"${producto.precio:.2f}"
            for producto in self.productos
        ]

        self.combo_producto["values"] = opciones

        if opciones:
            self.combo_producto.current(0)

    def cargar_ventas(self):

        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)

        ventas = self.servicio.listar_ventas()

        for venta in ventas:

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.id,
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )

    # ==================================================
    # 1. REGISTRAR PRODUCTO
    # ==================================================

    def registrar_producto(self):

        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar producto")
        ventana.geometry("420x320")
        ventana.resizable(False, False)

        marco = ttk.Frame(
            ventana,
            padding=25
        )

        marco.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            marco,
            text="REGISTRAR PRODUCTO",
            font=("Arial", 16, "bold")
        ).pack(
            pady=(0, 20)
        )

        ttk.Label(
            marco,
            text="Nombre:"
        ).pack(
            anchor="w"
        )

        entrada_nombre = ttk.Entry(
            marco,
            width=40
        )

        entrada_nombre.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            marco,
            text="Precio:"
        ).pack(
            anchor="w"
        )

        entrada_precio = ttk.Entry(
            marco,
            width=40
        )

        entrada_precio.pack(
            fill="x",
            pady=(5, 20)
        )

        def guardar():

            try:

                producto = (
                    self.servicio.registrar_producto(
                        entrada_nombre.get(),
                        entrada_precio.get()
                    )
                )

                self.cargar_productos()

                self.barra_estado.config(
                    text=(
                        f"Producto #{producto.id} "
                        f"registrado correctamente."
                    )
                )

                messagebox.showinfo(
                    "Correcto",
                    (
                        "Producto registrado.\n\n"
                        f"ID: {producto.id}\n"
                        f"Nombre: {producto.nombre}\n"
                        f"Precio: ${producto.precio:.2f}"
                    ),
                    parent=ventana
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        ttk.Button(
            marco,
            text="Guardar producto",
            command=guardar
        ).pack()

    # ==================================================
    # 2. LISTAR PRODUCTOS
    # ==================================================

    def listar_productos(self):

        productos = self.servicio.listar_productos()

        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de productos")
        ventana.geometry("600x400")

        tabla = ttk.Treeview(
            ventana,
            columns=("id", "nombre", "precio"),
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")

        tabla.column("id", width=60)
        tabla.column("nombre", width=300)
        tabla.column("precio", width=120)

        tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        for producto in productos:

            tabla.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    f"${producto.precio:.2f}"
                )
            )

    # ==================================================
    # 3. BUSCAR PRODUCTO
    # ==================================================

    def buscar_producto(self):

        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar producto")
        ventana.geometry("600x400")

        marco = ttk.Frame(
            ventana,
            padding=20
        )

        marco.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            marco,
            text="Nombre del producto:"
        ).pack(
            anchor="w"
        )

        entrada = ttk.Entry(
            marco,
            width=40
        )

        entrada.pack(
            fill="x",
            pady=10
        )

        tabla = ttk.Treeview(
            marco,
            columns=("id", "nombre", "precio"),
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")

        tabla.column("id", width=60)
        tabla.column("nombre", width=280)
        tabla.column("precio", width=120)

        tabla.pack(
            fill="both",
            expand=True,
            pady=10
        )

        def buscar():

            for fila in tabla.get_children():
                tabla.delete(fila)

            productos = (
                self.servicio.buscar_productos(
                    entrada.get()
                )
            )

            for producto in productos:

                tabla.insert(
                    "",
                    "end",
                    values=(
                        producto.id,
                        producto.nombre,
                        f"${producto.precio:.2f}"
                    )
                )

        ttk.Button(
            marco,
            text="Buscar",
            command=buscar
        ).pack()

    # ==================================================
    # 4. ACTUALIZAR PRODUCTO
    # ==================================================

    def actualizar_producto(self):

        productos = self.servicio.listar_productos()

        if not productos:

            messagebox.showinfo(
                "Productos",
                "No existen productos."
            )

            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar producto")
        ventana.geometry("450x400")

        marco = ttk.Frame(
            ventana,
            padding=25
        )

        marco.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            marco,
            text="Producto:"
        ).pack(
            anchor="w"
        )

        combo = ttk.Combobox(
            marco,
            state="readonly",
            width=40
        )

        combo["values"] = [
            f"{p.id} - {p.nombre}"
            for p in productos
        ]

        combo.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            marco,
            text="Nuevo nombre:"
        ).pack(
            anchor="w"
        )

        entrada_nombre = ttk.Entry(
            marco,
            width=40
        )

        entrada_nombre.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            marco,
            text="Nuevo precio:"
        ).pack(
            anchor="w"
        )

        entrada_precio = ttk.Entry(
            marco,
            width=40
        )

        entrada_precio.pack(
            fill="x",
            pady=(5, 20)
        )

        def actualizar():

            if not combo.get():

                messagebox.showwarning(
                    "Validación",
                    "Seleccione un producto.",
                    parent=ventana
                )

                return

            try:

                producto_id = int(
                    combo.get().split(" - ")[0]
                )

                producto = (
                    self.servicio.actualizar_producto(
                        producto_id,
                        entrada_nombre.get(),
                        entrada_precio.get()
                    )
                )

                self.cargar_productos()

                self.barra_estado.config(
                    text=(
                        f"Producto #{producto.id} "
                        "actualizado correctamente."
                    )
                )

                messagebox.showinfo(
                    "Correcto",
                    "Producto actualizado correctamente.",
                    parent=ventana
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        ttk.Button(
            marco,
            text="Actualizar",
            command=actualizar
        ).pack()

    # ==================================================
    # 5. ELIMINAR PRODUCTO
    # ==================================================

    def eliminar_producto(self):

        productos = self.servicio.listar_productos()

        if not productos:

            messagebox.showinfo(
                "Productos",
                "No existen productos."
            )

            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar producto")
        ventana.geometry("420x250")

        marco = ttk.Frame(
            ventana,
            padding=25
        )

        marco.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            marco,
            text="Seleccione un producto:"
        ).pack(
            anchor="w"
        )

        combo = ttk.Combobox(
            marco,
            state="readonly",
            width=35
        )

        combo["values"] = [
            f"{p.id} - {p.nombre}"
            for p in productos
        ]

        combo.pack(
            fill="x",
            pady=15
        )

        def eliminar():

            if not combo.get():

                messagebox.showwarning(
                    "Validación",
                    "Seleccione un producto.",
                    parent=ventana
                )

                return

            producto_id = int(
                combo.get().split(" - ")[0]
            )

            confirmar = messagebox.askyesno(
                "Confirmar",
                "¿Desea eliminar este producto?",
                parent=ventana
            )

            if not confirmar:
                return

            try:

                self.servicio.eliminar_producto(
                    producto_id
                )

                self.cargar_productos()

                self.barra_estado.config(
                    text="Producto eliminado correctamente."
                )

                messagebox.showinfo(
                    "Correcto",
                    "Producto eliminado correctamente.",
                    parent=ventana
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        ttk.Button(
            marco,
            text="Eliminar producto",
            command=eliminar
        ).pack()

    # ==================================================
    # 6. REGISTRAR USUARIO
    # ==================================================

    def registrar_usuario(self):

        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar usuario")
        ventana.geometry("450x420")

        marco = ttk.Frame(
            ventana,
            padding=25
        )

        marco.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            marco,
            text="REGISTRAR USUARIO",
            font=("Arial", 16, "bold")
        ).pack(
            pady=(0, 20)
        )

        ttk.Label(
            marco,
            text="Nombre:"
        ).pack(
            anchor="w"
        )

        entrada_nombre = ttk.Entry(
            marco,
            width=40
        )

        entrada_nombre.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            marco,
            text="Usuario:"
        ).pack(
            anchor="w"
        )

        entrada_usuario = ttk.Entry(
            marco,
            width=40
        )

        entrada_usuario.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            marco,
            text="Contraseña:"
        ).pack(
            anchor="w"
        )

        entrada_password = ttk.Entry(
            marco,
            width=40,
            show="*"
        )

        entrada_password.pack(
            fill="x",
            pady=(5, 20)
        )

        def guardar():

            try:

                usuario = (
                    self.servicio.registrar_usuario(
                        entrada_nombre.get(),
                        entrada_usuario.get(),
                        entrada_password.get()
                    )
                )

                self.cargar_usuarios()

                self.barra_estado.config(
                    text=(
                        f"Usuario #{usuario.id} "
                        "registrado correctamente."
                    )
                )

                messagebox.showinfo(
                    "Correcto",
                    (
                        "Usuario registrado.\n\n"
                        f"ID: {usuario.id}\n"
                        f"Nombre: {usuario.nombre}\n"
                        f"Usuario: {usuario.usuario}"
                    ),
                    parent=ventana
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        ttk.Button(
            marco,
            text="Guardar usuario",
            command=guardar
        ).pack()

    # ==================================================
    # 7. LISTAR USUARIOS
    # ==================================================

    def listar_usuarios(self):

        usuarios = self.servicio.listar_usuarios()

        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de usuarios")
        ventana.geometry("650x400")

        tabla = ttk.Treeview(
            ventana,
            columns=("id", "nombre", "usuario"),
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("usuario", text="Usuario")

        tabla.column("id", width=60)
        tabla.column("nombre", width=300)
        tabla.column("usuario", width=200)

        tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        for usuario in usuarios:

            tabla.insert(
                "",
                "end",
                values=(
                    usuario.id,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # ==================================================
    # 8. REALIZAR VENTA
    # ==================================================

    def mostrar_ventas(self):

        self.combo_usuario.focus()

        self.barra_estado.config(
            text="Seleccione un usuario y un producto para realizar una venta."
        )

    def registrar_venta(self):

        seleccion_usuario = (
            self.combo_usuario.get()
        )

        seleccion_producto = (
            self.combo_producto.get()
        )

        if not seleccion_usuario:

            messagebox.showwarning(
                "Validación",
                "Debe seleccionar un usuario."
            )

            return

        if not seleccion_producto:

            messagebox.showwarning(
                "Validación",
                "Debe seleccionar un producto."
            )

            return

        try:

            usuario_id = int(
                seleccion_usuario.split(" - ")[0]
            )

            producto_id = int(
                seleccion_producto.split(" - ")[0]
            )

            venta = (
                self.servicio.registrar_venta(
                    usuario_id,
                    producto_id
                )
            )

            self.cargar_ventas()

            self.barra_estado.config(
                text=(
                    f"Venta #{venta.id} "
                    "registrada correctamente."
                )
            )

            messagebox.showinfo(
                "Venta registrada",
                (
                    f"Venta #{venta.id} registrada correctamente.\n\n"
                    f"Usuario: {venta.usuario}\n"
                    f"Producto: {venta.producto}\n"
                    f"Fecha: {venta.fecha}"
                )
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==================================================
    # 9. CONSULTAR VENTAS DE UN USUARIO
    # ==================================================

    def consultar_ventas_usuario(self):

        usuarios = self.servicio.listar_usuarios()

        ventana = tk.Toplevel(self.root)
        ventana.title("Ventas de un usuario")
        ventana.geometry("750x450")

        marco = ttk.Frame(
            ventana,
            padding=20
        )

        marco.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            marco,
            text="Seleccione un usuario:"
        ).pack(
            anchor="w"
        )

        combo = ttk.Combobox(
            marco,
            state="readonly",
            width=40
        )

        combo["values"] = [
            f"{u.id} - {u.nombre}"
            for u in usuarios
        ]

        combo.pack(
            fill="x",
            pady=10
        )

        tabla = ttk.Treeview(
            marco,
            columns=(
                "id",
                "usuario",
                "producto",
                "fecha"
            ),
            show="headings"
        )

        tabla.heading(
            "id",
            text="ID"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.heading(
            "producto",
            text="Producto"
        )

        tabla.heading(
            "fecha",
            text="Fecha"
        )

        tabla.column(
            "id",
            width=60
        )

        tabla.column(
            "usuario",
            width=180
        )

        tabla.column(
            "producto",
            width=200
        )

        tabla.column(
            "fecha",
            width=200
        )

        tabla.pack(
            fill="both",
            expand=True,
            pady=10
        )

        def consultar():

            for fila in tabla.get_children():
                tabla.delete(fila)

            if not combo.get():

                messagebox.showwarning(
                    "Validación",
                    "Seleccione un usuario.",
                    parent=ventana
                )

                return

            usuario_id = int(
                combo.get().split(" - ")[0]
            )

            try:

                ventas = (
                    self.servicio.ventas_por_usuario(
                        usuario_id
                    )
                )

                if not ventas:

                    messagebox.showinfo(
                        "Consulta",
                        "El usuario no tiene ventas registradas.",
                        parent=ventana
                    )

                    return

                for venta in ventas:

                    tabla.insert(
                        "",
                        "end",
                        values=(
                            venta.id,
                            venta.usuario,
                            venta.producto,
                            venta.fecha
                        )
                    )

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        ttk.Button(
            marco,
            text="Consultar ventas",
            command=consultar
        ).pack()

    # ==================================================
    # 10. SALIR
    # ==================================================

    def salir(self):

        respuesta = messagebox.askyesno(
            "Salir",
            "¿Desea cerrar Restaurante App?"
        )

        if respuesta:
            self.root.destroy()