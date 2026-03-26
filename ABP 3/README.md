# Sistema de Gestión de Usuarios

## Descripción
Aplicación de consola en Python para administrar usuarios con las operaciones CRUD básicas.

## Estructura del proyecto
- `main.py` : entrada del programa y menú interactivo.
- `modulos/menu.py` : función `mostrar_menu()` y presentación de opciones.
- `modulos/gestion_de_datos.py` : lógica de usuarios en memoria (`agregar_usuario`, `listar_usuarios`, `buscar_usuario`, `eliminar_usuario`).
- `modulos/validaciones.py` : validación de edad.

## Funcionalidades
- Registrar usuarios (nombre, edad, tipo).
- Listar usuarios registrados.
- Buscar usuario por nombre.
- Eliminar usuario por nombre.

## Reglas de validación
- Edad debe ser entero mayor a 0.
- Nombre no puede repetirse (case-insensitive).
- Tipos admitidos: `Admin`, `Usuario`, `Invitado`.

## Requisitos
- Python 3.14 (o superior).

## Ejecución
Desde la raíz del proyecto:

```bash
cd "c:\\Users\\marti\\Desktop\\alke wallte\\ABP 3"
python main.py
```

## Uso
1. Selecciona opción `1` para registrar usuario.
2. Ingresa nombre, edad y tipo.
3. Usa opción `2` para listar.
4. Usa `3` para buscar y `4` para eliminar.
5. Opción `5` para salir.

## Subir a GitHub
1. Inicializar repo si no existe:
   ```bash
git init
git add .
git commit -m "Proyecto ABP 3 - gestor de usuarios"
git branch -M main
git remote add origin https://github.com/<tu_usuario>/<tu_repo>.git
git push -u origin main
```
2. En futuras actualizaciones:
   ```bash
git add .
git commit -m "Mejoras en validaciones y README"
git push
```
