from tkinter import *
from Screen import Screen
from Controllers.usuarioController import usuarioController

class Login(Screen):
    controller = usuarioController()
    def init (self):
        self.Titulo = Label(self.window,
                            text="MedicApp",
                            fg="blue",    # Foreground
                            # bg="green",   # Background
                            justify='center',
                            # underline = True,
                            font=("Arial",32))
        self.NUsuario = Entry(self.window,
                              width=45,
                              justify=CENTER,
                              font=("Arial",20),)
        self.CUsuario = Entry(self.window,
                              width=45,
                              justify=CENTER,
                              show="*",                            
                              font=("Arial",20),)
        # Boleano
        self.Show = BooleanVar(self.window)
        # Conversiones
        self.CheckShow = Checkbutton(self.window,
                                     text="Mostrar contraseña",
                                     variable=self.Show,
                                    #  command=lambda:ActivarLetras(1)
                                     )
        
        self.Registrar = Button(self.window,
                                text="Registarse",
                                justify=CENTER,
                                font="Arial 20 underline",
                                # state="disabled"
                                )
        self.Iniciar = Button(self.window,
                                text="Iniaciar sesion",
                                justify=CENTER,
                                font="Arial 20 bold",
                                # state="disabled"
                                command=self.Iniciar
                                )
        
        # mpaquetar los elementos
        self.window.grid_slaves(row=5,column=5)
        self.Titulo.grid(row=1,column=3)
        self.NUsuario.grid(row=2,column=3)
        self.CUsuario.grid(row=3,column=3)
        self.CheckShow.grid(row=3,column=4)
        self.Registrar.grid(row=4,column=3)
        self.Iniciar.grid(row=5,column=3)
        
    def Iniciar(self):
        print(self.controller.where(
            ['nombre_usuario', 'contrasena'],
            [self.NUsuario.get(), self.CUsuario.get()]
            ).fetchone())#si te sale None es que no existe ese usuario