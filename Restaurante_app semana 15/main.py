import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_aplicacion(usuario):

    for widget in root.winfo_children():
        widget.destroy()

    MainView(
        root,
        servicio,
        usuario
    )


def main():

    global root
    global servicio

    servicio = RestauranteServicio()

    root = tk.Tk()

    LoginView(
        root,
        servicio,
        iniciar_aplicacion
    )

    root.mainloop()


if __name__ == "__main__":
    main()