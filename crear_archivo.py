import os

ruta = 'tareas.txt'

def create_txt():
    if os.path.exists(ruta):
        print("El archivo ya existe.")
    else:
        open(ruta, "w").close()
        print("Archivo Creado.")