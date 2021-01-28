from tkinter import *
from tkinter import ttk
from threading import *
from time import *
from clase_resistencia import *
from clase_fuente import *



class Ventana:
    HOLA = None
    ActivoResistencia = False
    ActivoFuente = False
    ConfiguracionNombreResitencia = None
    ConfiguracionValorResitencia = None
    ConfiguracionNombreFuente = None
    ConfiguracionValorFuente = None
    
    
    
    def __init__(self):
        self.instancia = Tk()
        self.B_Resistencia = None
        self.B_fuente = None
        self.img_resistencia = PhotoImage(file = "Imagenes/resitencia.png")
        self.img_resistenciaV = PhotoImage(file = "Imagenes/resitenciaV.png")
        self.img_fuente = PhotoImage(file = "Imagenes/fuente de poder.png")
        self.img_fuenteV = PhotoImage(file = "Imagenes/fuente de poderV.png")
        self.img_Girar = PhotoImage(file = "Imagenes/girar.png")
        self.img_Eliminar = PhotoImage(file = "Imagenes/eliminar.png")
        self.img_Cerrar = PhotoImage(file = "Imagenes/cerrar.png")
        self.img_Conectar = PhotoImage(file = "Imagenes/conectar.png")
        self.Resistencias = []
        self.Fuentes = []

    def abrirVentana(self):
        self.instancia.title('Menu principal')
        self.instancia.configure(bg= 'black')
        #imagen de fondo
        fondo = PhotoImage(file = "Imagenes/fondo.png")
        self.fon = Canvas(self.instancia , width= 1336, height = 548)
        self.fon.pack(expand = NO, fill = BOTH)
        self.fon.create_image(0,0, image = fondo, anchor = NW)
        '''fon = Label(self.instancia,image = fondo,bg = 'black')    MAE ESTO LO MODIFIQUE PARA DIBUJAR LINEAS   
        fon.place(x=0,y =0)'''
        #boton de resistancia
        self.B_Resistencia = Button(self.instancia,text= 'Resistencia',image = self.img_resistencia,height = 68, width = 80,command = lambda:self.configuracion("resistencia"))
        self.B_Resistencia.place(x= 80,y=450)
        #boton de fuente
        self.B_fuente = Button(self.instancia,text= 'fuente de poder',image = self.img_fuente,height = 68, width = 80, command = lambda:self.configuracion("fuente"))
        self.B_fuente.place(x= 180,y=450)
        self.B_Resistencia.configure()

        self.instancia.bind('<Button-1>', self.motion)

        self.instancia.geometry('1336x548+0+100')
        self.instancia.mainloop()

    def motion(self,event):
        x, y = event.x, event.y
        if x > 102 and y > 68 and y < 376 and x < 1240:      
            if self.ActivoResistencia:
                self.ponerResistencia(x,y)
            elif self.ActivoFuente:
                self.ponerFuente(x,y)

    def configuracion(self, who):
        self.B_Resistencia.configure(state =DISABLED)
        self.B_fuente.configure(state =DISABLED)
        configuracion = Canvas(self.instancia , width= 280, height = 72, bg = "black")
        LabelNombre= Label(configuracion,text = 'Nombre',font= ('Times New Roman',15),bg= 'black',fg= 'white')
        LabelNombre.place(x=5,y=5)
        TextoNombre = Entry(configuracion,width = 20)
        TextoNombre.place(x=5,y=25)
        LabelValor= Label(configuracion,text = 'Valor',font= ('Times New Roman',15),bg= 'black',fg= 'white')
        LabelValor.place(x=155,y=5)
        TextoValor = Entry(configuracion,width = 20)
        TextoValor.place(x=155,y=25)
        btnAceptar = Button(configuracion,text= 'Aceptar',command = lambda:self.AceptarConfiguracion(configuracion,TextoNombre,TextoValor,who))
        btnAceptar.place(x= 5,y=45)
        configuracion.place(x=280, y=450)
    
    def conectar(self, x, y, who, boton):
        boton.configure(state = DISABLED)
        conectar = Canvas(self.instancia, width=200, height=50, bg="black")
        LabelNombre= Label(conectar,text = 'Nombre del componente para conectar',font= ('Times New Roman',8),bg= 'black',fg= 'white')
        LabelNombre.place(x = 5, y = 5)
        TextoNombreConectar = Entry(conectar,width = 18)
        TextoNombreConectar.place(x=5,y=25)
        btnAceptar = Button(conectar,text= 'Aceptar', command = lambda:self.ConectarCon(conectar, TextoNombreConectar.get(), who, boton))
        btnAceptar.place(x = 135, y = 25)
        conectar.place(x = x+130, y = y-45)
        
    def ConectarCon(self, ventana, Nombre, who, boton):
        coordx, coordy = who.getCoords()
        boton.configure(state = NORMAL)
        ventana.destroy()
        for elem in (self.Resistencias):
            if Nombre == elem.getNom() and Nombre != who.getNom():
                self.fon.create_line(coordx, coordy, elem.getCoords(), width=5)
        for elem in (self.Fuentes):
            if Nombre == elem.getNom() and Nombre != who.getNom():
                self.fon.create_line(coordx, coordy, elem.getCoords(), width=5)

    def girarResistencia(self,resistencia,btnResistencia):
        if resistencia.getOrientacion() == "horizontal":
            resistencia.setOrientacion("vertical")
            btnResistencia.configure(image = self.img_resistenciaV,width  = 68,height  = 80)
        else:
            resistencia.setOrientacion("horizontal")
            btnResistencia.configure(image = self.img_resistencia,height  = 68,width   = 80)

    def girarFuente(self,fuente,btnFuente):
        if fuente.getOrientacion() == "horizontal":
            fuente.setOrientacion("vertical")
            btnFuente.configure(image = self.img_fuenteV,width  = 68,height  = 80)
        else:
            fuente.setOrientacion("horizontal")
            btnFuente.configure(image = self.img_fuente,height  = 68,width   = 80)

    def eliminarComponente(self,componente, boton, canvas):
        boton.destroy()
        if componente in self.Fuentes:
            self.Fuentes.remove(componente)
        if componente in self.Resistencias:
            self.Resistencias.remove(componente)
        self.cierraCanvas(componente, canvas)

    def cierraCanvas(self, componente, canvas):
        componente.active = False
        canvas.destroy()
        
    
    def modifica(self,x,y,Componente,boton,who):
        if Componente.active == False and who == "resistencia":
            Componente.active = True
            canvas = Canvas(self.instancia , width= 160, height = 40, bg = "#eeaa02")
            btnGirar = Button(canvas,image = self.img_Girar, command = lambda:self.girarResistencia(Componente,boton))
            btnGirar.place(x= 0,y=0)
            btnEliminar = Button(canvas,image = self.img_Eliminar, command = lambda:self.eliminarComponente(Componente, boton,canvas))
            btnEliminar.place(x= 40,y=0)
            if Componente.conectado == False:
                btnConectar = Button(canvas,image = self.img_Conectar, command = lambda:self.conectar(x, y, Componente, btnConectar))
                btnConectar.place(x= 80,y=0)
            btnCerrar = Button(canvas,image = self.img_Cerrar, command = lambda:self.cierraCanvas(Componente, canvas))
            btnCerrar.place(x= 120,y=0)
            canvas.place(x=x-35, y=y-45)

        elif Componente.active == False and who == "fuente":
            Componente.active = True
            canvas = Canvas(self.instancia , width= 160, height = 40, bg = "#eeaa02")
            btnGirar = Button(canvas,image = self.img_Girar, command = lambda:self.girarFuente(Componente,boton))
            btnGirar.place(x= 0,y=0)
            btnEliminar = Button(canvas,image = self.img_Eliminar, command = lambda:self.eliminarComponente(Componente, boton,canvas))
            btnEliminar.place(x= 40,y=0)
            if Componente.conectado == False:
                btnConectar = Button(canvas,image = self.img_Conectar, command = lambda:self.conectar(x, y, Componente, btnConectar))
                btnConectar.place(x= 80,y=0)
            btnCerrar = Button(canvas,image = self.img_Cerrar, command = lambda:self.cierraCanvas(Componente, canvas))
            btnCerrar.place(x= 120,y=0)
            canvas.place(x=x-40, y=y-45)
        

    def AceptarConfiguracion(self,ventana,textNom,textValor,who):
        if who == "resistencia":
            self.ConfiguracionNombreResitencia = textNom.get()
            self.ConfiguracionValorResitencia = textValor.get()
            self.ActivoResistencia = True
        elif who == "fuente":
            self.ConfiguracionNombreFuente = textNom.get()
            self.ConfiguracionValorFuente = textValor.get()
            self.ActivoFuente = True
        ventana.destroy()    

    def ponerResistencia(self,x2,y2):
        self.B_Resistencia.configure(state = NORMAL)
        self.B_fuente.configure(state = NORMAL)
        Resitenciab = Button(self.instancia,text= 'Resistencia',image = self.img_resistencia,height = 68, width = 80,bg = "#efe4b0", fg = "#efe4b0")
        ResistenciaP = Resistencia(self.ConfiguracionNombreResitencia,self.ConfiguracionValorResitencia,"horizontal",Resitenciab)
        ResistenciaP.setCoords(x2, y2)
        Resitenciab.configure(command = lambda:self.modifica(x2-40,y2-34,ResistenciaP,Resitenciab,"resistencia"))
        Resitenciab.place(x= x2-40,y=y2-34)
        self.Resistencias.append(ResistenciaP)
        self.ActivoResistencia = False
    
    def ponerFuente(self,x2,y2):
        self.B_Resistencia.configure(state = NORMAL)
        self.B_fuente.configure(state = NORMAL)
        Fuenteb = Button(self.instancia,text= 'Fuente',image = self.img_fuente,height = 68, width = 80,bg = "#efe4b0", fg = "#efe4b0")
        FuenteP = Fuente(self.ConfiguracionNombreFuente,self.ConfiguracionValorFuente,"horizontal",Fuenteb)
        FuenteP.setCoords(x2, y2)
        Fuenteb.configure(command = lambda:self.modifica(x2-40,y2-34,FuenteP,Fuenteb,"fuente"))
        Fuenteb.place(x= x2-40,y=y2-34)
        self.Fuentes.append(FuenteP)
        self.ActivoFuente = False
        
    def abrir(self):
        hilo2 = Thread(target= self.abrirVentana())

   


Ventana.HOLA = Ventana()
Ventana.HOLA.abrir()


    



