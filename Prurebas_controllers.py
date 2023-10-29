from Controllers.Controller import Controller
from Controllers.usuarioController import usuarioController
from Controllers.doctorController import doctorController

# usuarioController
# usuario = usuarioController()

# usuario.insert([
#     "prueba",
#     "prueba",
#     "12/8",
#     "s",
#     "s",
#     "s"
# ])

# for row in usuario.getid([
#     "prueba",
#     "prueba",
#     "12/8",
#     "s",
#     "s",
#     "s"
# ]):
#     print(row)

# print(usuario.getid([
#     "prueba",
#     "prueba",
#     "12/8",
#     "s",
#     "s",
#     "s"
# ]).fetchone()[0])

# doctorcontroller.
controller = doctorController()
controller.create([
    "prueba",
    "prueba",
    "12/8",
    "s",
    "s",
    "s"
],[
    "cedula",
    "especialidad",
    "experiencia"
])

print(controller.all().fetchall())