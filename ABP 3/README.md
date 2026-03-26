# Sistema de Gestión de Usuarios

# Descripción
Aplicación de consola en Python para administrar usuarios.

# Estructura del proyecto
- `main.py` : entrada del programa y menú interactivo.
- `modulos/menu.py` :presentación de opciones.
- `modulos/gestion_de_datos.py` : lógica de usuarios en memoria (`agregar_usuario`, `listar_usuarios`, `buscar_usuario`, `eliminar_usuario`).
- `modulos/validaciones.py` : validación de edad.

# Funcionalidades
- Registrar usuarios (nombre, edad, tipo).
- Listar usuarios registrados.
- Buscar usuario por nombre.
- Eliminar usuario por nombre.

# Reglas de validación
- Edad debe ser entero mayor a 0.
- Nombre no puede repetirse (case-insensitive).
- Tipos admitidos: `Admin`, `Usuario`, `Invitado`.

# Uso
1. Selecciona opción `1` para registrar usuario.
2. Ingresa nombre, edad y tipo.
3. Usa opción `2` para listar.
4. Usa `3` para buscar y `4` para eliminar.
5. Opción `5` para salir.

