ruta = 'tareas.txt'

def reed_task():
    with open(ruta, 'r') as archivo:
        cant_task = 0
        lineas = archivo.readlines()
        if len(lineas) == 0:
            print("No hay Tareas.")
        else:
            for l in lineas:
                cant_task += 1
                print(f"{cant_task}-{l.replace('\n', '')}")