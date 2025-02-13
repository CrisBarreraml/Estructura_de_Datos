import random
import json

def guardar_datos(nombre_archivo, alumnos, materias, matriz):
    datos = {
        "num_alumnos": alumnos,
        "num_materias": materias,
        "calificaciones": matriz
    }
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo)
    print("Datos guardados correctamente.")

def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
        print("Datos cargados correctamente.")
        return datos["num_alumnos"], datos["num_materias"], datos["calificaciones"]
    except FileNotFoundError:
        print("El archivo no existe.")
        return None, None, None

def menu():
    while True:
        print("\nMenú:")
        print("1. Introducir datos")
        print("2. Guardar datos")
        print("3. Cargar datos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            num_alumnos = int(input("Ingrese el número de alumnos: "))
            num_materias = int(input("Ingrese el número de materias: "))
            
            titulos_materias = [f"Materia {i+1}" for i in range(num_materias)]
            matriz = [[random.randint(0, 100) for _ in range(num_materias)] for _ in range(num_alumnos)]
            
            print("\nResultados de Calificaciones:")
            print("Alumno\t" + "\t".join(titulos_materias))
            for i, calificaciones in enumerate(matriz):
                print(f"Alumno {i+1}\t" + "\t".join(map(str, calificaciones)))

        elif opcion == "2":
            nombre_archivo = input("Ingrese el nombre del archivo para guardar: ")
            guardar_datos(nombre_archivo, num_alumnos, num_materias, matriz)

        elif opcion == "3":
            nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")
            num_alumnos, num_materias, matriz = cargar_datos(nombre_archivo)
            if num_alumnos and num_materias:
                print("\nResultados de Calificaciones Cargados:")
                titulos_materias = [f"Materia {i+1}" for i in range(num_materias)]
                print("Alumno\t" + "\t".join(titulos_materias))
                for i, calificaciones in enumerate(matriz):
                    print(f"Alumno {i+1}\t" + "\t".join(map(str, calificaciones)))

        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()

