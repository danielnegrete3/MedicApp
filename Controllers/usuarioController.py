from .Controller import Controller

class usuarioController(Controller):
    database = "MedicApp"
    table = "usuarios"
    columns = [ 
        "id",
        "nombre",
        "nombre_usuario",
        "fecha_nacimiento",
        "contrasena",
        "cargo",
        "imagen"
    ]
    columns_string = ""
    for column in columns:
        columns_string += column
        if (columns[-1] != column):
            columns_string += ","