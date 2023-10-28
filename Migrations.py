import sqlite3

usuarios =  [ 
    "nombre",
    "nombre_usuario",
    "fecha_nacimiento",
    "contrasena",
    "cargo",
    "imagen"
],
administrativos = [
    "id_usuario",
    "cargo"
],
doctores =[
    "id_usuario",
    "cedula",
    "especialidad",
    "experiencia"
]
diagnosticos =[
    "nombre_doctor",
    "nombre_pasiente",
    "fecha_nacimiento",
    "postmortem"
]

tables = {
    "usuarios" : usuarios,
    "administrativos" :administrativos,
}

conexion = sqlite3.connect("MedicApp")
for nombre in tables:
    columnas = ""
    for columna in tables[nombre]:
        columnas+= columna + ","   
    conexion.execute("CREATE TABLE "+ nombre +"("+columnas+")")
    

