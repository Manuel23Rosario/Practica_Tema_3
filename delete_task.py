from crear_archivo import ruta

def delete_task():
    try:
        with open(ruta, 'r') as archivo:
            tareas = archivo.readlines()

            tarea_eliminar = int(input("Indique la tarea a eliminar:"))
            tareas.pop(tarea_eliminar - 1)

        with open(ruta, 'w') as archivo:
            archivo.writelines(tareas)

        print("\n---------------------------")
        print("Tarea Eliminada.")
        print("---------------------------\n")
    except IndexError:
        print("Tarea no encontrada, Verifique el id de su tarea oh confirme si la lista no este vacia.")