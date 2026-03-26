usuarios = []

ROLES = ("Admin", "Usuario", "Invitado")

def agregar_usuario(nombre, edad, tipo):
    nombre_clean = nombre.strip().lower()
    if any(u["nombre"].strip().lower() == nombre_clean for u in usuarios):
        return False

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "tipo": tipo
    }
    usuarios.append(usuario)
    return True


def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados")
        return

    for u in usuarios:
        print(f"Nombre: {u['nombre']} - Edad: {u['edad']} - Tipo: {u['tipo']}")

def buscar_usuario(nombre):
    nombre_clean = nombre.strip().lower()
    for u in usuarios:
        if u["nombre"].strip().lower() == nombre_clean:
            return u
    return None

def eliminar_usuario(nombre):
    nombre_clean = nombre.strip().lower()
    for u in usuarios:
        if u["nombre"].strip().lower() == nombre_clean:
            usuarios.remove(u)
            return True
    return False