from crear_archivo import ruta

def update_task():
    try:
        with open(ruta, 'r') as archivo:
            tareas = archivo.readlines()

        if not tareas:
            print("\n---------------------------")
            print("No hay tareas para modificar.")
            print("---------------------------\n")
            return

        tarea_modificar = int(input("\nIndique el número de la tarea a modificar: "))
        print("======================================================")

        # Validar rango
        if tarea_modificar < 1 or tarea_modificar > len(tareas):
            print("\n---------------------------")
            print("Número de tarea inválido.")
            print("---------------------------\n")
            return

        tarea_nueva = input("Ingrese la nueva tarea: ")

        # Modificar correctamente la línea
        tareas[tarea_modificar - 1] = tarea_nueva + "\n"

        # Guardar cambios
        with open(ruta, 'w') as archivo:
            archivo.writelines(tareas)

        print("\n---------------------------")
        print("Tarea Actualizada.")
        print("---------------------------\n")

    except ValueError:
        print("\nDebes escribir un número válido.\n")

    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}\n")