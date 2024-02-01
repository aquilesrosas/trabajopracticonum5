# 1) Hacer un programa que gestiones datos para una escuela.
# El programa tiene que ser capaz de:
# a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, 
# Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las 
# notas, cantidad de faltas, cantidad de amonestaciones recibidas.
# Recomendación: Para llevar un registro de estos dato se puede 
# utilizar un diccionario estructurado de la siguiente manera:
# {
# “Alumnos” : [alumno1,alumno2,alumno3 ]
# }
# Donde cada alumno es otro diccionario estructurado de la 
# siguiente forma:
# {
# “Nombre”: nombre de alumno,
# “Apellido” : apellido de alumno,
# “DNI” : DNI de alumno
# “Fecha de nacimiento”, fecha de nacimiento de alumno,
# “Tutor” : nombre y apellido de tutor,
# “Notas” : todas las notas del alumno,
# “Faltas” : cantidad de faltas,
# “amonestaciones” : cantidad de amonestaciones
# }
# En esta estructura:
# Datos = {
# “Alumnos” : [alumno1,alumno2,alumno3 ]
# }
# Para acceder por ejemplo al numero de DNI del tercer alumno 
# podríamos hacer algo así:
# Datos[“Alumnos”][2][“DNI”]
# Este es un ejemplo de estructura, se puede cambiar 
# completamente o hacer algunos cambios sobre el para mejorar el 
# orden (si lo consideran necesario)
# b) Mostrar los datos de cada alumno
# c) Modificar los datos de los alumnos
# d) Agregar alumnos
# e) Expulsar alumnos
# RECOMEDACIONN GENERAL:
# El programa es extenso, hacer por partes.
# Llevará mucho tiempo, la paciencia es importante.
# Internet es una gran ayuda.
# La prolijidad es fundamental
# Las funciones tendrán que recibir como parámetros los diccionarios que 
# representan a los alumnos.


import json
archivo_alumnos =  "data.json"

def cargar_alumnos():
    try:
        with open(archivo_alumnos, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_alumnos(alumnos):
    with open(archivo_alumnos, "w") as file:
        json.dump(alumnos, file, indent=4)

def agregar_alumno():
# Solicitar datos al usuario
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (formato: dd/mm/yyyy): ")
    tutor = input("Ingrese el nombre y apellido del tutor del alumno: ")
    notas = input("Ingrese las notas del alumno separadas por comas (ejemplo: 8,7,9): ").split(',')
    faltas = int(input("Ingrese la cantidad de faltas del alumno: "))
    amonestaciones = int(input("Ingrese la cantidad de amonestaciones del alumno: "))
        # Cargar datos existentes desde el archivo JSON

    try:
        with open("datosalumnos.json", "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
# Si el archivo no existe, crear una estructura inicial
alumno={"Alumnos": []}
nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [int(nota) for nota in notas],
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
 # Agregar el nuevo alumno a la lista de alumnos
data["Alumnos"].append(nuevo_alumno)
 # Guardar los datos actualizados en el archivo JSON
with open("datosalumnos.json", "w") as file:
        json.dump(data, file)

print("Alumno agregado exitosamente.")