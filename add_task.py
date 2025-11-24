from crear_archivo import ruta

def add_task():
    with open(ruta, 'a') as archivo:
        tarea = input("\nIngresa una tarea:")
        archivo.write(f"{tarea}\n")
    print("\n---------------------------")
    print("Tarea Agregada")
    print("---------------------------\n")