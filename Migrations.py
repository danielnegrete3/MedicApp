import sqlite3

usuarios =  [ 
    "nombre",
    "nombre_usuario",
    "fecha_nacimiento",
    "contrasena",
    "cargo",
    "imagen"
]
administrativos = [
    "id_usuario",
    "cargo"
]
doctores =[
    "id_usuario",
    "cedula",
    "especialidad",
    "experiencia"
]
diagnosticos =[
    "id_doctor",
    "nombre_pasiente",
    "fecha_nacimiento",
    "postmortem",
    "signos",
    "sintomas",
    "examenes",
    "enfermedad",
]
enfermedades = [
    "nombre",
    "signos",
    "sintomas",
    "examenes",
]
signos_sintomas= [
    "nombre",
    "tipo", #signo o sintoma
    "descripcion", 
]
examenes = [
     "nombre",
     "tipo", #rango, boleano, cualquier otro
     "valor" #valor positivo o rango positivo
]
examenes_diagnosticos =[
    "id_examen",
    "id_diagnostico",
    "valor_diagnostico"
]

tables = {
    "usuarios" : usuarios,
    "administrativos" :administrativos,
    "doctores" : doctores,
    "diagnosticos" : diagnosticos,
    "enfermedades" : enfermedades,
    "signos_sintomas" : signos_sintomas,
    "examenes": examenes,
    "examenes_diagnosticos":examenes_diagnosticos
}

conexion = sqlite3.connect("MedicApp")
for nombre in tables:
    columnas = ""
    for columna in tables[nombre]:
        columnas+= columna
        if(tables[nombre][-1] != columna):
            columnas+= ","
    conexion.execute("CREATE TABLE "+ nombre +"("+columnas+")")
    

