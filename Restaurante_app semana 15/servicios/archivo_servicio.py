import json


class ArchivoServicio:

    def cargar(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            raise ValueError(
                "El archivo JSON contiene datos inválidos."
            )

        except PermissionError:
            raise PermissionError(
                f"No se tiene permiso para leer el archivo: {ruta}"
            )

    def guardar(self, ruta, datos):
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            raise PermissionError(
                f"No se tiene permiso para escribir el archivo: {ruta}"
            )