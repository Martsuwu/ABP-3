from modulos.menu import mostrar_menu
from modulos.gestion_de_datos import (
    agregar_usuario,
    listar_usuarios,
    buscar_usuario,
    eliminar_usuario,
)
from modulos.validaciones import validar_edad


def main():
    while True:
        opcion = mostrar_menu().strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            edad_input = input("Edad: ").strip()
            edad = validar_edad(edad_input)
            if edad is None:
                print("Edad inválida")
                continue
            tipo = input("Tipo (Admin/Usuario/Invitado): ").strip()

            if agregar_usuario(nombre, edad, tipo):
                print("Usuario agregado correctamente")
            else:
                print("Ya existe un usuario con ese nombre")

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            usuario = buscar_usuario(nombre)
            print(usuario if usuario else "No encontrado")

        elif opcion == "4":
            nombre = input("Nombre a eliminar: ").strip()
            print("Eliminado" if eliminar_usuario(nombre) else "No encontrado")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
