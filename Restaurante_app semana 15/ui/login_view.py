import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(self, root, servicio, iniciar_aplicacion):
        self.root = root
        self.servicio = servicio
        self.iniciar_aplicacion = iniciar_aplicacion

        self.root.title("Restaurante App - Inicio de sesión")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        marco = ttk.Frame(self.root, padding=30)
        marco.pack(fill="both", expand=True)

        titulo = ttk.Label(
            marco,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=(10, 5))

        subtitulo = ttk.Label(
            marco,
            text="Inicio de sesión",
            font=("Arial", 12)
        )
        subtitulo.pack(pady=(0, 25))

        ttk.Label(
            marco,
            text="Usuario:"
        ).pack(anchor="w")

        self.entrada_usuario = ttk.Entry(
            marco,
            width=35
        )
        self.entrada_usuario.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            marco,
            text="Contraseña:"
        ).pack(anchor="w")

        self.entrada_password = ttk.Entry(
            marco,
            width=35,
            show="*"
        )
        self.entrada_password.pack(
            fill="x",
            pady=(5, 20)
        )

        boton = ttk.Button(
            marco,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )
        boton.pack(pady=10)

        informacion = ttk.Label(
            marco,
            text="Usuario de prueba: admin | Contraseña: 1234"
        )
        informacion.pack(pady=(20, 0))

    def iniciar_sesion(self):

        usuario = self.entrada_usuario.get().strip()
        password = self.entrada_password.get().strip()

        usuario_validado = self.servicio.validar_login(
            usuario,
            password
        )

        if usuario_validado is None:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )
            return

        messagebox.showinfo(
            "Acceso correcto",
            f"Bienvenido, {usuario_validado.nombre}."
        )

        self.iniciar_aplicacion(usuario_validado)