ruta = 'tareas.txt'

def update_task():
    with open(ruta, 'r') as archivo:
        tareas = archivo.readlines()

        tarea_modificar = int(input("Indique la tarea a modificar:"))
        print("======================================================")
        tarea_nueva = input("Ingrese la tarea nueva:")

        tareas[tarea_modificar - 1] = tarea_nueva, "\n"

    with open(ruta, 'w') as archivo:
        archivo.writelines(tarea_nueva)
    print("\n---------------------------")
    print("Tarea Actualizada.")
    print("---------------------------\n")