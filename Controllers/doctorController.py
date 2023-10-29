from .Controller import Controller
from .usuarioController import usuarioController

class doctorController(Controller):
    database = "MedicApp"
    table = "doctores"
    columns = [ 
        "id",
        "id_usuario",
        "cedula",
        "especialidad",
        "experiencia"
    ]
    columns_string = ""
    for column in columns:
        columns_string += column
        if (columns[-1] != column):
            columns_string += ","
            
    def create(self,dataUsuario, datadoctor):
        usuario = usuarioController()
        usuario.insert(dataUsuario)
        id_usuario = usuario.getid(dataUsuario).fetchone()[0]
        data = [str(id_usuario)]
        for d in datadoctor:
            data.append(d)
        self.insert(data)
    
    