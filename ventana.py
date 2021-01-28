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
    
    
    
    def __init__(self):
        self.instancia = Tk()
        self.B_Resistencia = None
        self.B_fuente = None
        self.img_resistencia = PhotoImage(file = "Imagenes/resitencia.png")
        self.img_resistenciaV = PhotoImage(file = "Imagenes/resitenciaV.png")
        self.img_fuente = PhotoImage(file = "Imagenes/fuente de poder.png")
        self.img_Girar = PhotoImage(file = "Imagenes/girar.png")
        self.img_Eliminar = PhotoImage(file = "Imagenes/eliminar.png")
        self.img_Cerrar = PhotoImage(file = "Imagenes/cerrar.png")
        self.Resistencias = []
        self.Fuentes = []

    def abrirVentana(self):
        
        self.instancia.title('Menu principal')
        self.instancia.configure(bg= 'black')
        #imagen de fondo
        fondo = PhotoImage(file = "Imagenes/fondo.png")
        fon = Label(self.instancia,image = fondo,bg = 'black')
        fon.place(x=0,y =0)
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

    def girarResistencia(self,resistencia,btnResistencia):
        if resistencia.getOrientacion() == "horizontal":
            resistencia.setOrientacion("vertical")
            btnResistencia.configure(image = self.img_resistenciaV,width  = 68,height  = 80)
        else:
            resistencia.setOrientacion("horizontal")
            btnResistencia.configure(image = self.img_resistencia,height  = 68,width   = 80)

    def eliminarComponente(self,componente,canvas):
        componente.destroy()
        self.cierraCanvas(componente, canvas)

    def cierraCanvas(self, componente, canvas):
        componente.active = False
        canvas.destroy()
        
    
    def modifica(self,x,y,Componente,boton,who):
        if Componente.active == False and who == "resistencia":
            Componente.active = True
            canvas = Canvas(self.instancia , width= 120, height = 40, bg = "#eeaa02")
            btnGirar = Button(canvas,image = self.img_Girar, command = lambda:self.girarResistencia(Componente,boton))
            btnGirar.place(x= 0,y=0)
            btnEliminar = Button(canvas,image = self.img_Eliminar, command = lambda:self.eliminarComponente(boton,canvas))
            btnEliminar.place(x= 40,y=0)
            btnCerrar = Button(canvas,image = self.img_Cerrar, command = lambda:self.cierraCanvas(Componente, canvas))
            btnCerrar.place(x= 80,y=0)
            canvas.place(x=x-10, y=y-45)

        elif Componente.active == False and who == "fuente":
            Componente.active = True
            canvas = Canvas(self.instancia , width= 120, height = 40, bg = "#eeaa02")
            #btnGirar = Button(canvas,image = self.img_Girar, command = lambda:self.girarResistencia(Componente,boton))
            #btnGirar.place(x= 0,y=0)
            btnEliminar = Button(canvas,image = self.img_Eliminar, command = lambda:self.eliminarComponente(boton,canvas))
            btnEliminar.place(x= 40,y=0)
            btnCerrar = Button(canvas,image = self.img_Cerrar, command = lambda:self.cierraCanvas(Componente, canvas))
            btnCerrar.place(x= 80,y=0)
            canvas.place(x=x-10, y=y-45)
        

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
        Resitenciab.configure(command = lambda:self.modifica(x2-40,y2-34,ResistenciaP,Resitenciab,"resistencia"))
        Resitenciab.place(x= x2-40,y=y2-34)
        self.Resistencias.append(ResistenciaP)
        self.ActivoResistencia = False
    
    def ponerFuente(self,x2,y2):
        self.B_Resistencia.configure(state = NORMAL)
        self.B_fuente.configure(state = NORMAL)
        Fuenteb = Button(self.instancia,text= 'Fuente',image = self.img_fuente,height = 68, width = 80,bg = "#efe4b0", fg = "#efe4b0")
        FuenteP = Fuente(self.ConfiguracionNombreFuente,self.ConfiguracionValorFuente,"horizontal",Fuenteb)
        Fuenteb.configure(command = lambda:self.modifica(x2-40,y2-34,FuenteP,Fuenteb,"fuente"))
        Fuenteb.place(x= x2-40,y=y2-34)
        self.Fuentes.append(FuenteP)
        self.ActivoFuente = False
        
    def abrir(self):
        hilo2 = Thread(target= self.abrirVentana())

   


Ventana.HOLA = Ventana()
Ventana.HOLA.abrir()


    



