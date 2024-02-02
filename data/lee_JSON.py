import json, os
script=os.path.dirname(__file__)



def cargar_alumnos():
    try:
        with open(os.path.join(script, "data.json"), "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Alumnos": []}



def guardar_alumnos(alumnos):
    with open(script, "w") as file:
        json.dump(alumnos, file, indent=4)

def agregar_alumno():
    nuevo_alumno = {
        "Nombre": input("Ingrese el nombre del alumno: "),
        "Apellido": input("Ingrese el apellido del alumno: "),
        "DNI":int (input("Ingrese el DNI del alumno: ")),
        "Fecha de nacimiento": input("Ingrese la fecha de nacimiento del alumno: "),
        "Tutor": input("Ingrese el nombre y apellido del tutor del alumno: "),
        "Notas": [],
        "Faltas": 0,
        "amonestaciones": 0
    }

    try:
        with open(script + "/data.json", "r") as file:
            data = json.load(file)
            data["Alumnos"].append(nuevo_alumno)

        with open(script + "/data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("¡Alumno agregado correctamente!")
    except FileNotFoundError:
        print("El archivo 'data.json' no existe o no se puede abrir.")

def modificar_datos_alumno():
    try:
        with open(script + "/data.json", "r") as file:
            data = json.load(file)

        indice_alumno = int(input("Ingrese el índice del alumno que desea modificar (1, 2, 3, ...): ")) - 1

        if 0 <= indice_alumno < len(data["Alumnos"]):
            # Imprimir información del alumno antes de la modificación
            print("\nInformación actual del alumno:")
            for clave, valor in data["Alumnos"][indice_alumno].items():
                print(f"{clave}: {valor}")

            # Solicitar al usuario que ingrese los nuevos datos
            nuevo_nombre = input("Ingrese el nuevo nombre del alumno: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del alumno: ")
            nuevo_dni = input("Ingrese el nuevo DNI del alumno: ")
            nuevo_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del alumno: ")
            nuevo_tutor = input("Ingrese el nuevo nombre y apellido del tutor del alumno: ")

            # Actualizar los datos del alumno
            data["Alumnos"][indice_alumno]["Nombre"] = nuevo_nombre
            data["Alumnos"][indice_alumno]["Apellido"] = nuevo_apellido
            data["Alumnos"][indice_alumno]["DNI"] = nuevo_dni
            data["Alumnos"][indice_alumno]["Fecha de nacimiento"] = nuevo_fecha_nacimiento
            data["Alumnos"][indice_alumno]["Tutor"] = nuevo_tutor

            # Guardar los cambios en el archivo JSON
            with open(script + "/data.json", "w") as file:
                json.dump(data, file, indent=4)

            print("\n¡Datos del alumno modificados correctamente!")
        else:
            print("Índice de alumno no válido.")
    except FileNotFoundError:
        print("El archivo 'data.json' no existe o no se puede abrir.")

def expulsar_alumno():
    dni_expulsar = int(input("Ingrese el DNI del alumno a expulsar: "))

    # Cargar los datos existentes desde el archivo JSON
    alumnos = cargar_alumnos()

    if "Alumnos" in alumnos and isinstance(alumnos["Alumnos"], list):
        # Buscar al alumno por su DNI
        indice_expulsar = next((i for i, alumno in enumerate(alumnos["Alumnos"]) if alumno.get("DNI") == dni_expulsar), None)

        if indice_expulsar is not None:
            # Eliminar al alumno de la lista de alumnos
            alumno_expulsado = alumnos["Alumnos"].pop(indice_expulsar)

            # Guardar los datos actualizados en el archivo JSON
            guardar_alumnos(alumnos)

            print(f"Alumno expulsado exitosamente:\n{alumno_expulsado}")
        else:
            print("No se encontró un alumno con ese DNI.")
    else:
        print("Error en el formato del archivo 'data.json'.")
        




class Alumno:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, tutor):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.tutor = tutor
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def ingresar_nota(self, nota):
        self.notas.append(nota)

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1

    def cambiar_domicilio(self, nuevo_domicilio):
        print(f"Cambiando domicilio de {self.nombre} {self.apellido} a {nuevo_domicilio}")
        self.guardar_en_json()

    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "DNI": self.dni,
            "Fecha de nacimiento": self.fecha_nacimiento,
            "Tutor": self.tutor,
            "Notas": self.notas,
            "Faltas": self.faltas,
            "Amonestaciones": self.amonestaciones
        }

    def guardar_en_json(self):
        with open("data.json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)

def cargar_alumno_desde_json():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return Alumno(**data)
    except FileNotFoundError:
        return None

# Función para ingresar los datos del alumno desde la entrada del usuario
def ingresar_datos_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (formato: dd/mm/yyyy): ")
    tutor = input("Ingrese el nombre y apellido del tutor del alumno: ")

    return Alumno(nombre, apellido, dni, fecha_nacimiento, tutor)

# Programa interactivo
def programa_interactivo():
    alumno = cargar_alumno_desde_json()

    if alumno is None:
        print("No se encontró un alumno en el archivo JSON. Se creará uno nuevo.")
        alumno = ingresar_datos_alumno()

    while True:
        print("\n1. Ingresar nota")
        print("2. Asignar falta")
        print("3. Asignar amonestación")
        print("4. Cambiar domicilio")
        print("5. Guardar y salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nota = float(input("Ingrese la nota: "))
            alumno.ingresar_nota(nota)
            print(f"Nota ingresada: {nota}")
        elif opcion == "2":
            alumno.asignar_falta()
            print("Falta asignada")
        elif opcion == "3":
            alumno.asignar_amonestacion()
            print("Amonestación asignada")
        elif opcion == "4":
            nuevo_domicilio = input("Ingrese el nuevo domicilio: ")
            alumno.cambiar_domicilio(nuevo_domicilio)
            print(f"Domicilio cambiado a: {nuevo_domicilio}")
        elif opcion == "5":
            alumno.guardar_en_json()
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

# Ejecutar el programa interactivo
programa_interactivo()
modificar_datos_alumno()

