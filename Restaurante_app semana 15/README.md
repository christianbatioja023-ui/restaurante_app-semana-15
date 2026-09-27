# Restaurante App

## Datos del estudiante

* **Nombre:** Christian Vladimir Batioja Plaza
* **Asignatura:** Programación Orientada a Objetos
* **Semana:** 15
* **Fecha:** 27/09/2026
* **Proyecto:** Restaurante App

---

## 1. Descripción del proyecto

**Restaurante App** es una aplicación de escritorio desarrollada en Python utilizando programación orientada a objetos y la biblioteca Tkinter.

El sistema permite administrar productos, usuarios y ventas mediante una interfaz gráfica. La información se almacena en archivos JSON para conservar los datos aunque la aplicación se cierre y se vuelva a ejecutar.

En la Semana 15 se incorporó principalmente el manejo fundamental de eventos mediante botones y callbacks utilizando el parámetro `command=` de Tkinter.

---

## 2. Evolución del proyecto

El proyecto se ha desarrollado progresivamente durante las diferentes semanas de trabajo.

Se inició con las funcionalidades básicas de administración de productos y usuarios. Posteriormente se incorporó la persistencia de información mediante archivos JSON.

En esta Semana 15 se fortaleció la interfaz gráfica y el manejo de eventos, incorporando el registro de ventas mediante una interacción entre:

**Interfaz gráfica → Evento `command=` → Callback → Servicio → Persistencia → Actualización de la interfaz**

También se conservaron las funcionalidades desarrolladas anteriormente para mantener la continuidad del proyecto.

---

## 3. Funcionalidades principales

El sistema cuenta con las siguientes 10 opciones:

1. Registrar producto
2. Listar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Registrar usuario
7. Listar usuarios
8. Realizar venta
9. Consultar ventas de un usuario
10. Salir

Todas estas opciones se encuentran disponibles desde el menú principal de la aplicación.

---

## 4. Gestión de productos

La aplicación permite administrar los productos registrados.

### Registrar producto

Permite ingresar:

* ID del producto
* Nombre
* Precio

Los datos son enviados al servicio correspondiente y posteriormente almacenados en `productos.json`.

### Listar productos

Muestra los productos registrados en una tabla utilizando `Treeview`.

### Buscar producto

Permite buscar productos utilizando su nombre.

### Actualizar producto

Permite modificar los datos de un producto existente.

### Eliminar producto

Permite seleccionar un producto y eliminarlo después de solicitar una confirmación al usuario.

---

## 5. Gestión de usuarios

El sistema permite administrar los usuarios de la aplicación.

### Registrar usuario

Permite registrar:

* ID
* Nombre
* Usuario
* Contraseña

La información se almacena en `usuarios.json`.

### Listar usuarios

Muestra los usuarios registrados mediante una tabla.

### Inicio de sesión

La aplicación cuenta con una ventana inicial de autenticación.

Para realizar las pruebas se puede utilizar:

* **Usuario:** `admin`
* **Contraseña:** `1234`

Después de una autenticación correcta se muestra la ventana principal.

---

## 6. Gestión de ventas

La Semana 15 incorpora la gestión de ventas como una de las funcionalidades principales.

Para registrar una venta, el usuario selecciona:

* Usuario existente
* Producto existente

Al presionar el botón **Registrar venta**, la aplicación ejecuta el evento correspondiente.

La venta registra:

* ID de venta
* Usuario
* Producto
* Fecha

La información se almacena en:

```text
datos/ventas.json
```

Las ventas también se muestran inmediatamente en la interfaz mediante un `Treeview`.

---

## 7. Manejo de eventos

Uno de los objetivos principales de la Semana 15 es comprender y aplicar el manejo fundamental de eventos en Tkinter.

Los botones utilizan el parámetro:

```python
command=
```

Por ejemplo, el botón para registrar una venta utiliza:

```python
command=self.registrar_venta
```

Cuando el usuario presiona el botón, Tkinter ejecuta el método correspondiente.

El flujo implementado es:

```text
Usuario presiona el botón
        ↓
Evento command=
        ↓
Método callback
        ↓
Obtención de datos de la interfaz
        ↓
RestauranteServicio
        ↓
Validación de la operación
        ↓
Registro de la venta
        ↓
Guardado en ventas.json
        ↓
Actualización del Treeview
        ↓
Mensaje de resultado
```

De esta manera, la lógica de negocio no se concentra directamente en la interfaz gráfica.

---

## 8. Separación de responsabilidades

El proyecto utiliza una estructura modular para separar las diferentes responsabilidades.

### Modelos

Los modelos representan las entidades principales del sistema:

* `Producto`
* `Usuario`
* `Venta`

Cada modelo cuenta con métodos para convertir los objetos a diccionarios y reconstruirlos desde datos JSON.

### Servicios

Los servicios contienen la lógica relacionada con los datos y las operaciones del restaurante.

`RestauranteServicio` se encarga de:

* Productos
* Usuarios
* Ventas
* Validaciones
* Operaciones de negocio
* Comunicación con el almacenamiento

`ArchivoServicio` se encarga de:

* Leer archivos JSON
* Guardar archivos JSON
* Manejar errores relacionados con los archivos

### Interfaz gráfica

La carpeta `ui` contiene las ventanas de la aplicación:

* `login_view.py`
* `main_view.py`

La interfaz se encarga principalmente de mostrar información, recibir entradas del usuario y ejecutar los callbacks correspondientes.

---

## 9. Persistencia de datos

El proyecto utiliza archivos JSON para conservar la información.

Los archivos principales son:

```text
datos/
├── productos.json
├── usuarios.json
└── ventas.json
```

### productos.json

Almacena los productos registrados.

### usuarios.json

Almacena los usuarios registrados.

### ventas.json

Almacena las ventas realizadas.

Las ventas registradas permanecen guardadas después de cerrar la aplicación.

Al volver a iniciar el programa, las ventas almacenadas en `ventas.json` se cargan nuevamente y aparecen en la interfaz.

---

## 10. Estructura del proyecto

La estructura actual del proyecto es:

```text
restaurante_app/
│
├── assets/
│   ├── logo_restaurante.png
│   └── icono_venta.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

---

## 11. Recursos visuales

La carpeta `assets` contiene recursos utilizados por la interfaz gráfica.

Actualmente se utilizan:

* `logo_restaurante.png`
* `icono_venta.png`

El logo se muestra en la interfaz principal y el ícono se utiliza como recurso visual relacionado con la gestión de ventas.

Estos elementos permiten mejorar la presentación y organización visual de la aplicación.

---

## 12. Interfaz gráfica

La interfaz fue desarrollada con:

```text
Tkinter
```

Se utilizan componentes como:

* `Tk`
* `Frame`
* `Label`
* `Entry`
* `Button`
* `Combobox`
* `Treeview`
* `Toplevel`
* `messagebox`

La ventana principal cuenta con un menú que permite acceder a las diferentes funcionalidades del sistema.

Las ventas se presentan en una tabla para facilitar su visualización.

---

## 13. Validaciones

Las operaciones principales son procesadas mediante la capa de servicios.

Entre las validaciones realizadas se encuentran:

* Comprobación de datos requeridos.
* Verificación de existencia de productos.
* Verificación de existencia de usuarios.
* Validación de usuario y contraseña.
* Validación de precios.
* Validación de identificadores.
* Confirmación antes de eliminar registros.
* Control de errores relacionados con archivos JSON.

La interfaz comunica al usuario el resultado de las operaciones mediante mensajes.

---

## 14. Tecnologías utilizadas

El proyecto utiliza:

* **Python 3**
* **Programación Orientada a Objetos**
* **Tkinter**
* **ttk**
* **JSON**
* **Archivos locales**
* **Treeview**
* **Git/GitHub** (si se utiliza para el control de versiones)

---

## 15. Ejecución del proyecto

Para ejecutar la aplicación se debe abrir una terminal dentro de la carpeta principal:

```text
restaurante_app
```

Luego ejecutar:

```bash
python main.py
```

Se abrirá la ventana de inicio de sesión.

Para realizar una prueba rápida:

```text
Usuario: admin
Contraseña: 1234
```

Después de iniciar sesión se mostrará la ventana principal del sistema.

---

## 16. Prueba del registro de ventas

Para probar la funcionalidad principal de la Semana 15:

1. Iniciar sesión.
2. Seleccionar un usuario existente.
3. Seleccionar un producto existente.
4. Presionar **Registrar venta**.
5. Verificar que aparezca un mensaje indicando que la venta fue registrada.
6. Verificar que la venta aparezca inmediatamente en la tabla.
7. Abrir `datos/ventas.json`.
8. Comprobar que la nueva venta se encuentre almacenada.
9. Cerrar la aplicación.
10. Ejecutar nuevamente `python main.py`.
11. Iniciar sesión nuevamente.
12. Verificar que la venta continúe apareciendo en la tabla.

Esta prueba permite comprobar tanto el manejo de eventos como la persistencia de información.

---

## 17. Conclusión

En la Semana 15 se implementó el manejo fundamental de eventos en la aplicación `restaurante_app`.

El proyecto permite administrar productos y usuarios, registrar ventas y consultar las ventas realizadas.

La funcionalidad de registro de ventas utiliza eventos mediante `command=`, callbacks y una capa de servicios para mantener separada la interfaz de la lógica de negocio.

Además, la información se mantiene mediante archivos JSON, permitiendo recuperar los datos después de cerrar y volver a ejecutar la aplicación.

El proyecto conserva las funcionalidades desarrolladas anteriormente y continúa utilizando una estructura modular basada en programación orientada a objetos.
