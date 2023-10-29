from .Controller import Controller
from .usuarioController import usuarioController

class doctorController(Controller):
    database = "MedicApp"
    table = "administrativos"
    columns = [ 
        "id",
        "id_usuario",
        "cargo"
    ]
    columns_string = ""
    for column in columns:
        columns_string += column
        if (columns[-1] != column):
            columns_string += ","
            
    def create(self,dataUsuario, dataadministrativo):
        usuario = usuarioController()
        usuario.insert(dataUsuario)
        id_usuario = usuario.getid(dataUsuario).fetchone()[0]
        data = [str(id_usuario)]
        for d in dataadministrativo:
            data.append(d)
        self.insert(data)