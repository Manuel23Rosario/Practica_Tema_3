print("Gestor de tares")

def Menu():
    try:
        print("1-Crear Archivo\n 2-Agregar Tareas.\n3-Modificar Tareas.\n4-Leer Tareas.\n5-Eliminar Tareas.\n6-Salir de la app.")
        option = int(input("Ingrese una opcion:"))

        """
        if option == 1:
            create_txt()
        elif option == 2:
            add_task()
        elif option == 3:
            update_task()
        elif option == 4:
            #reed_task()
        elif option == 5:
           # delete_task()
        elif option == 6:
           # Close_app()
        """
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