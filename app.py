from crear_archivo import create_txt
from add_task import add_task
from update_task import update_task
from reed_task import reed_task
from delete_task import delete_task
from close_app import close_app

print("Gestor de tares")

def Menu():
    try:
        print("1-Crear Archivo\n2-Agregar Tareas.\n3-Modificar Tareas.\n4-Leer Tareas.\n5-Eliminar Tareas.\n6-Salir de la app.")
        option = int(input("Ingrese una opcion:"))

        
        if option == 1:
            create_txt()
            Menu()
        elif option == 2:
            add_task()
            Menu()
        elif option == 3:
            update_task()
            Menu()
        elif option == 4:
            reed_task()
            Menu()
        elif option == 5:
            delete_task()
            Menu()
        elif option == 6:
            close_app()
        
        #Manejo de errores.
        if option > 5 or option < 1:
            print("\n=============================================================================================")
            print("Por favor ingrese un numero entre 1 y 5.")
            print("=============================================================================================\n")
            Menu()

    except ValueError:
        print("\n=============================================================================================")
        print("Porfavor ingrese un numero.")
        print("=============================================================================================\n")
        Menu()

Menu()