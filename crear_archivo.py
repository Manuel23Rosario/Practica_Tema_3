import os

ruta = 'tareas.txt'

def create_txt():
    if os.path.exists(ruta):
        print("\n---------------------------")
        print("El archivo ya existe.")
        print("---------------------------\n")
    else:
        open(ruta, "w").close()
        print("\n---------------------------")
        print("Archivo Creado.")
        print("---------------------------\n")