from Lista import Lista
from Menu import Menu

if __name__=='__main__':
    lista=Lista()
    menu=Menu()
    salir=False
    while not salir:
        print("\n---------------------MENU---------------------")
        print("1. Insertar un vehiculo en la coleccion en una posicion determinada.")
        print("2. Agregar un vehiculo a la coleccion.")
        print("3. Mostrar tipos de objetos en una posicion.")
        print("4. Modificar precio base de vehiculo usado.")
        print("5. Mostrar vehiculo mas economico.")
        print("6. Listar vehiculos")
        print("7. Almacenar los objetos en memoria.")
        print("0. Salir")
        print("----------------------------------------------------\n")

        opcion=int(input("\nIngrese opcion: "))
        menu.opcion(opcion,lista)
        salir=opcion==0