ruta = 'tareas.txt'

def add_task():
    with open(ruta, 'a') as archivo:
        tarea = input("Ingresa una tarea:")
        archivo.write(f"{tarea}\n")
    print("\n---------------------------")
    print("Tarea Agregada")
    print("---------------------------\n")