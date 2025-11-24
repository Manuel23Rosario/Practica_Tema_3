ruta = 'tareas.txt'

def delete_task():
    with open(ruta, 'r') as archivo:
        tareas = archivo.readlines()

        tarea_eliminar = int(input("Indique la tarea a eliminar:"))
        tareas.pop(tarea_eliminar - 1)

    with open(ruta, 'w') as archivo:
        archivo.writelines(tareas)

    print("\n---------------------------")
    print("Tarea Eliminada.")
    print("---------------------------\n")

delete_task()