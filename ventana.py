from tkinter import *
from tkinter import ttk
from threading import *
from time import *
from clase_resistencia import *
from clase_fuente import *
from clase_cable import *
from trazador_de_cables import *
from random import randint
##import pandas as pd



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
        self.Simulacion = []
        self.cables = []
        self.infoNodo =  None
        self.estaSimulando = False
        

    def abrirVentana(self):
        self.instancia.title('Menu principal')
        self.instancia.configure(bg= 'black')
        #imagen de fondo
        fondo = PhotoImage(file = "Imagenes/fondo.png")
        self.fon = Canvas(self.instancia , width= 1336, height = 548)
        self.fon.pack(expand = NO, fill = BOTH)
        self.fon.create_image(0,0, image = fondo, anchor = NW)
        
        voltaje = randint(0,10)
        amperaje = randint(0,10) / 1000
        self.infoNodo = Label(self.fon,text = str(voltaje) + "V\n" + str(amperaje) + "Ω" ,bg = 'Gray')

        #boton de resistancia
        self.B_Resistencia = Button(self.instancia,text= 'Resistencia',image = self.img_resistencia,height = 68, width = 80,command = lambda:self.configuracion("resistencia"))
        self.B_Resistencia.place(x= 80,y=450)
        
        #boton de fuente
        self.B_fuente = Button(self.instancia,text= 'fuente de poder',image = self.img_fuente,height = 68, width = 80, command = lambda:self.configuracion("fuente"))
        self.B_fuente.place(x= 180,y=450)
        self.B_Resistencia.configure()

        #boton de simulacion
        self.B_Simulacion = Button(self.instancia,text= 'Simulacion',height = 4, width = 11,command = lambda:self.simulacion())
        self.B_Simulacion.place(x=1080,y=450)

        #boton de exportar
        self.B_Exportacion = Button(self.instancia,text= 'Exportar',height = 4, width = 11,command = lambda:self.expNombre())
        self.B_Exportacion.place(x=580,y=450)

        #boton de importar
        self.B_Importar = Button(self.instancia,text= 'Importar',height = 4, width = 11,command = lambda:self.impNombre())
        self.B_Importar.place(x=680,y=450)
        
        self.instancia.bind('<Motion>', self.motion2)
        self.instancia.bind('<Button-1>', self.motion)
        self.instancia.geometry('1336x548+0+100')
        self.instancia.mainloop()
    
    def expNombre(self):
        #self.B_Exportacion(state =DISABLED)
        Exportacion = Canvas(self.instancia , width= 150, height = 72, bg = "black")
        LabelNombre= Label(Exportacion,text = 'Nombre del archivo para exportar',font= ('Times New Roman', 7),bg= 'black',fg= 'white')
        LabelNombre.place(x=5,y=5)
        TextoNombre = Entry(Exportacion,width = 20)
        TextoNombre.place(x=5,y=25)

        btnAceptar = Button(Exportacion,text= 'Aceptar',command = lambda:self.exportar(TextoNombre, Exportacion))
        btnAceptar.place(x= 5,y=45)
        Exportacion.place(x=780, y=450)
    
    def impNombre(self):
        #self.B_Exportacion(state =DISABLED)
        Importacion = Canvas(self.instancia , width= 150, height = 72, bg = "black")
        LabelNombre= Label(Importacion,text = 'Nombre del archivo a importar',font= ('Times New Roman', 7),bg= 'black',fg= 'white')
        LabelNombre.place(x=5,y=5)
        TextoNombre = Entry(Importacion,width = 20)
        TextoNombre.place(x=5,y=25)

        btnAceptar = Button(Importacion,text= 'Aceptar',command = lambda:self.importar(TextoNombre, Importacion))
        btnAceptar.place(x= 5,y=45)
        Importacion.place(x=780, y=450)

    def exportar(self, Nombre, Canvas):
        lista = ["nombre", "valor", "posicionx", "posiciony", "conectado", "componente"]
        data = []
        for elem in self.Resistencias:
            data.append([elem.getNom(), elem.getValor(), elem.getCoords()[0], elem.getCoords()[1], elem.getConectadoCon(), "Resistencia"])
        for elem in self.Fuentes:
            data.append([elem.getNom(), elem.getValor(), elem.getCoords()[0], elem.getCoords()[1], elem.getConectadoCon(), "Fuente"])
        df = pd.DataFrame(data, columns = lista)
        nombre = Nombre.get()
        direccion = "Guardados/" + nombre + ".csv"
        df.to_csv(direccion, index=False)
        Canvas.destroy()

    def importar(self, Nombre, Canvas):
        nombre = Nombre.get()
        direccion = "Guardados/" + nombre + ".csv"
        data = []
        try:
            data = pd.read_csv(direccion)
        except:
            pass
        
        contador = len(data)
        while contador != 0:
            if data['componente'][contador-1] == "Resistencia":
                self.ConfiguracionNombreResitencia = data['nombre'][contador-1]
                self.ConfiguracionValorResitencia = data['valor'][contador-1]
                self.ponerResistencia(data['posicionx'][contador-1],data['posiciony'][contador-1])
            elif data['componente'][contador-1] == "Fuente":
                self.ConfiguracionNombreFuente = data['nombre'][contador-1]
                self.ConfiguracionValorFuente = data['valor'][contador-1]
                self.ponerFuente(data['posicionx'][contador-1],data['posiciony'][contador-1])
            contador -= 1
        
        contador1 = len(data)
        while contador1 != 0:
            nombreslist = list(str(data['conectado'][contador1-1]))
            nombres = []
            nombre = ""
            for nom in nombreslist:
                if nom == ",":
                    nombres.append(nombre)
                    nombre = ""
                else:
                    nombre += str(nom)

            if len(nombres) != 0:
                for elem in self.Resistencias:
                    if elem.getNom() == data['nombre'][contador1-1]:
                        for nombr in nombres:
                            self.ConectarCon(nombr, elem)
                for elem in self.Fuentes:
                    if elem.getNom() == data['nombre'][contador1-1]:
                        for nombr in nombres:
                            self.ConectarCon(nombr, elem)
            contador1 -= 1

        Canvas.destroy()

    def motion2(self,event):
        if self.estaSimulando:
            x, y = event.x, event.y
            for elem in (self.cables):
                if elem.colision(x,y):
                    self.infoNodo.place_forget() 
                    self.infoNodo.place(x=x,y=y-12)
        
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

    def simulacion(self):
        self.estaSimulando = True
        for elem in (self.Resistencias):
            LabelNombreValor = Label(self.instancia,text = str(elem.getNom()) + "\n"+ str(elem.getValor()) +"(Ω)",font= ('Times New Roman',15),bg= '#efe4b0',fg= 'black')
            LabelNombreValor.place(x= elem.getCoords()[0]-40,y=elem.getCoords()[1]+50)
            self.Simulacion.append(LabelNombreValor)
        for elem in (self.Fuentes):
            LabelNombreValor = Label(self.instancia,text = str(elem.getNom()) + "\n"+ str(elem.getValor()) +"(V)",font= ('Times New Roman',15),bg= '#efe4b0',fg= 'black')
            LabelNombreValor.place(x= elem.getCoords()[0]-40,y=elem.getCoords()[1]+50)
            self.Simulacion.append(LabelNombreValor)

        #boton de Terminar Simulacion
        self.B_Termina_Simulacion = Button(self.instancia,text= 'Terminar',height = 4, width = 11,command = lambda:self.terminarSimulacion())
        self.B_Termina_Simulacion.place(x=1180,y=450)
        self.Simulacion.append(self.B_Termina_Simulacion)

    def terminarSimulacion(self):
        self.estaSimulando = False
        self.infoNodo.place_forget() 
        for elem in (self.Simulacion):
            elem.destroy()

    def conectar(self, x, y, who, boton):
        boton.configure(state = DISABLED)
        conectar = Canvas(self.instancia, width=200, height=50, bg="black")
        LabelNombre= Label(conectar,text = 'Nombre del componente para conectar',font= ('Times New Roman',8),bg= 'black',fg= 'white')
        LabelNombre.place(x = 5, y = 5)
        TextoNombreConectar = Entry(conectar,width = 18)
        TextoNombreConectar.place(x=5,y=25)
        btnAceptar = Button(conectar,text= 'Aceptar', command = lambda:self.auxConectar(conectar, TextoNombreConectar.get(), who, boton))
        btnAceptar.place(x = 135, y = 25)
        conectar.place(x = x+130, y = y-45)
    
    def auxConectar(self, ventana, nombre, who, boton):
        boton.configure(state = NORMAL)
        ventana.destroy()
        self.ConectarCon(nombre, who)

    def ConectarCon(self, Nombre, who):
        coordx, coordy = who.getCoords()
        for elem in (self.Resistencias):
            if Nombre == elem.getNom() and Nombre != who.getNom():
                who.setConectadoCon(Nombre)
                if elem.getOrientacion() == "horizontal":
                    if elem.getCoords()[0] <= coordx:
                        if who.getOrientacion() == "horizontal":
                            
                            AderechaH_BizquierdaH(elem,who,self.fon,self.cables)
                        else:
                            AderechaV_BizquierdaH(elem,who,self.fon,self.cables)
                            
                            
                    else:
                        if who.getOrientacion() == "horizontal":
                            AizquierdaH_BderechaH(elem,who,self.fon,self.cables)
                            
                        else:
                            AizquierdaV_BderechaH(elem,who,self.fon,self.cables)
                else:
                    if elem.getCoords()[1] >= coordy:
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                AarribaIzquierdaH_BabajoDerechaV(elem,who,self.fon,self.cables)
                                
                            else:
                                
                                AarribaDerechaH_BabajoIzquierdaV(elem,who,self.fon,self.cables)
                                
                        else:
                            AarribaV_BabajoV(elem,who,self.fon,self.cables)
                            
                    else:
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                
                                AabajoIzquierdaH_BarribaDerechaV(elem,who,self.fon,self.cables)
                                
                            else:
                                AabajoDerechaH_BarribaIzquierdaV(elem,who,self.fon,self.cables)
                                
                        else:
                            AabajoV_BarribaV(elem,who,self.fon,self.cables)
                            
        for elem in (self.Fuentes):
            if Nombre == elem.getNom() and Nombre != who.getNom():
                who.setConectadoCon(Nombre)

                if elem.getOrientacion() == "horizontal":
                    if elem.getCoords()[0] <= coordx:
                        if who.getOrientacion() == "horizontal":
                            
                            AderechaH_BizquierdaH(elem,who,self.fon,self.cables)
                        else:
                            AderechaV_BizquierdaH(elem,who,self.fon,self.cables)
                            
                            
                    else:
                        if who.getOrientacion() == "horizontal":
                            AizquierdaH_BderechaH(elem,who,self.fon,self.cables)
                            
                        else:
                            AizquierdaV_BderechaH(elem,who,self.fon,self.cables)
                else:
                    if elem.getCoords()[1] >= coordy:
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                AarribaIzquierdaH_BabajoDerechaV(elem,who,self.fon,self.cables)
                                
                            else:
                                
                                AarribaDerechaH_BabajoIzquierdaV(elem,who,self.fon,self.cables)
                                
                        else:
                            AarribaV_BabajoV(elem,who,self.fon,self.cables)
                            
                    else:
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                
                                AabajoIzquierdaH_BarribaDerechaV(elem,who,self.fon,self.cables)
                                
                            else:
                                AabajoDerechaH_BarribaIzquierdaV(elem,who,self.fon,self.cables)
                                
                        else:
                            AabajoV_BarribaV(elem,who,self.fon,self.cables)

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
        for elem in componente.getCablesConectados():
            for i in elem.getComponentes():
                a = elem.getComponentes().index(i)
                if elem.getDireccion(a) == 3:
                    i.setDerecha(False)
                elif elem.getDireccion(a) == 2:
                    i.setArriba(False)
                elif elem.getDireccion(a) == 1:
                    i.setIzquierda(False)
                elif elem.getDireccion(a) == 4:
                    i.setAbajo(False)
                    
                
            for elem2 in  elem.getUniones():
                self.fon.delete(elem2)
            
            for elem3 in elem.getComponentes():
                elem3.eliminarCablesConectados(elem3)
            self.cables.remove(elem)
                
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
            canvas = Canvas(self.instancia , width= 160, height = 40, bg = "Gray")
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
            canvas = Canvas(self.instancia , width= 160, height = 40, bg = "Gray")
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
        valor = textValor.get()
        nombre = textNom.get()
        pase = False
        if nombre != "" and valor != "":
            if who == "resistencia":
                for nom in self.Resistencias:
                    if nombre == nom.getNom():
                        pase = True
                        break
                if pase == False:
                    self.ConfiguracionNombreResitencia = textNom.get()
                    self.ConfiguracionValorResitencia = textValor.get()
                    self.ActivoResistencia = True
                    ventana.destroy()
            elif who == "fuente":
                for nom in self.Fuentes:
                    if nombre == nom.getNom():
                        pase = True
                        break
                if pase == False:
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


    



