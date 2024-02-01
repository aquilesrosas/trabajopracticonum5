import json

data = {} 
data ["Alumnos"] = []
data ["Alumnos"].append({
    "Nombre":"sergio",
    "Apellido":"gomez",
    "Edad":26,
    "Importe":20.5
})
data ["Alumnos"].append({
    "Nombre":"chaplin",
    "Apellido":"juarez",
    "Edad":27,
    "Importe":21.5 
    })
data ["Alumnos"].append({
    "Nombre":"guadalupe",
    "Apellido":"rodriguez",
    "Edad":30,
    "Importe":12.50 
    })

with open ("data.json", "w") as file:
    json.dump(data,file, indent=4)

