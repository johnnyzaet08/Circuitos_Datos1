from tkinter import *
from tkinter import ttk
from threading import *
from time import *
from clase_resistencia import *
from clase_fuente import *
from clase_cable import *



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
        

    def abrirVentana(self):
        self.instancia.title('Menu principal')
        self.instancia.configure(bg= 'black')
        #imagen de fondo
        fondo = PhotoImage(file = "Imagenes/fondo.png")
        self.fon = Canvas(self.instancia , width= 1336, height = 548)
        self.fon.pack(expand = NO, fill = BOTH)
        self.fon.create_image(0,0, image = fondo, anchor = NW)

        self.infoNodo = Label(self.fon,text = "Holiiis",bg = 'Gray')
        '''fon = Label(self.instancia,image = fondo,bg = 'black')    MAE ESTO LO MODIFIQUE PARA DIBUJAR LINEAS   
        fon.place(x=0,y =0)'''
        #boton de resistancia
        self.B_Resistencia = Button(self.instancia,text= 'Resistencia',image = self.img_resistencia,height = 68, width = 80,command = lambda:self.configuracion("resistencia"))
        self.B_Resistencia.place(x= 80,y=450)
        
        #boton de fuente
        self.B_fuente = Button(self.instancia,text= 'fuente de poder',image = self.img_fuente,height = 68, width = 80, command = lambda:self.configuracion("fuente"))
        self.B_fuente.place(x= 180,y=450)
        self.B_Resistencia.configure()
        #boton de simulacion
        self.B_Simulacion = Button(self.instancia,text= 'Simulacion',height = 4, width = 11,command = lambda:self.simulacion())
        self.B_Simulacion.place(x=1100,y=450)
        self.instancia.bind('<Motion>', self.motion2)
        self.instancia.bind('<Button-1>', self.motion)

        self.instancia.geometry('1336x548+0+100')
        self.instancia.mainloop()
    def motion2(self,event):#########################################revisar, es el causante de como aparece el self.infoNodo
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
        for elem in (self.Resistencias):
            LabelNombreValor = Label(self.instancia,text = elem.getNom() + "\n"+ elem.getValor() +"(Ω)",font= ('Times New Roman',15),bg= '#efe4b0',fg= 'black')
            LabelNombreValor.place(x= elem.getCoords()[0]-40,y=elem.getCoords()[1]+50)
            self.Simulacion.append(LabelNombreValor)
        for elem in (self.Fuentes):
            LabelNombreValor = Label(self.instancia,text = elem.getNom() + "\n"+ elem.getValor() +"(V)",font= ('Times New Roman',15),bg= '#efe4b0',fg= 'black')
            LabelNombreValor.place(x= elem.getCoords()[0]-40,y=elem.getCoords()[1]+50)
            self.Simulacion.append(LabelNombreValor)
        #boton de Terminar Simulacion
        self.B_Termina_Simulacion = Button(self.instancia,text= 'Terminar',height = 4, width = 11,command = lambda:self.terminarSimulacion())
        self.B_Termina_Simulacion.place(x=1000,y=450)
        self.Simulacion.append(self.B_Termina_Simulacion)
    def terminarSimulacion(self):
        for elem in (self.Simulacion):
            elem.destroy()
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
                if elem.getOrientacion() == "horizontal":
                    if elem.getCoords()[0] <= coordx:
                        if who.getOrientacion() == "horizontal":
                            self.unoa = self.fon.create_line(coordx-48, coordy, coordx,coordy, width=5)
                            self.dosa = self.fon.create_line(coordx-46, coordy,coordx-46, elem.getCoords()[1], width=5)
                            self.tresa =self.fon.create_line(coordx-48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx-48, coordy, coordx,coordy)
                            Cable.agregarUnion(self.dosa,coordx-46,coordy ,coordx-46,  elem.getCoords()[1])
                            Cable.agregarUnion(self.tresa,elem.getCoords()[0], elem.getCoords()[1],coordx-48 ,elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1], width=5)
                            self.dosa =self.fon.create_line(coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, elem.getCoords()[1],coordx, coordy)
                            Cable.agregarUnion(self.dosa,elem.getCoords()[0], elem.getCoords()[1], coordx,elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                            
                    else:
                        if who.getOrientacion() == "horizontal":
                            
                            self.unoa =self.fon.create_line(coordx+53, coordy, coordx,coordy, width=5)
                            self.dosa =self.fon.create_line(coordx+50, coordy,coordx+50, elem.getCoords()[1], width=5)
                            self.tresa =self.fon.create_line(coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, coordy, coordx+53,coordy)
                            Cable.agregarUnion(self.dosa,coordx+50,coordy ,coordx+50,  elem.getCoords()[1])
                            Cable.agregarUnion(self.tresa,coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
                            self.cables.append(Cable)
                            #####
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1], width=5)
                            self.dosa= self.fon.create_line(coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, elem.getCoords()[1],coordx, coordy)
                            Cable.agregarUnion(self.dosa,coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                else:
                    if elem.getCoords()[1] >= coordy:
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                self.unoa =self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
                                self.dosa=self.fon.create_line(coordx+46, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1])
                                Cable.agregarUnion(self.dosa,coordx+46, coordy, elem.getCoords()[0],coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            else:
                                self.unoa = self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
                                self.dosa = self.fon.create_line(coordx-42, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1])
                                Cable.agregarUnion(self.dosa,elem.getCoords()[0], coordy, coordx-42,coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1]-51, width=5)
                            self.dosa = self.fon.create_line(coordx, elem.getCoords()[1]-53, elem.getCoords()[0],elem.getCoords()[1]-53, width=5)
                            self.tresa =self.fon.create_line(elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, coordy,coordx, elem.getCoords()[1]-51)
                            Cable.agregarUnion(self.dosa,elem.getCoords()[0], elem.getCoords()[1]-53, coordx,elem.getCoords()[1]-53)
                            Cable.agregarUnion(self.tresa,elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                    else:
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                self.unoa = self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1]+51, width=5)
                                self.dosa = self.fon.create_line(coordx+46, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0],elem.getCoords()[1]+51 ,elem.getCoords()[0],coordy )
                                Cable.agregarUnion(self.dosa,coordx+46, coordy, elem.getCoords()[0],coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            else:
                                self.unoa =self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1]+51, width=5)
                                self.dosa =self.fon.create_line(coordx-42, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0], elem.getCoords()[1]+51 ,elem.getCoords()[0],coordy )
                                Cable.agregarUnion(self.dosa,elem.getCoords()[0], coordy, coordx-42,coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1]+51, width=5)
                            self.dosa = self.fon.create_line(coordx, elem.getCoords()[1]+53, elem.getCoords()[0],elem.getCoords()[1]+53, width=5)
                            if coordx >= elem.getCoords()[0]: 
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,coordx,elem.getCoords()[1]+51 ,coordx, coordy )
                                Cable.agregarUnion(self.dosa,elem.getCoords()[0], elem.getCoords()[1]+53, coordx,elem.getCoords()[1]+53)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            else:
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,coordx,elem.getCoords()[1]+51 ,coordx,  coordy )
                                Cable.agregarUnion(self.dosa,coordx, elem.getCoords()[1]+53, elem.getCoords()[0],elem.getCoords()[1]+53)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            
        for elem in (self.Fuentes):
            if Nombre == elem.getNom() and Nombre != who.getNom():
                if elem.getOrientacion() == "horizontal":
                    if elem.getCoords()[0] <= coordx:
                        if who.getOrientacion() == "horizontal":
                            self.unoa = self.fon.create_line(coordx-48, coordy, coordx,coordy, width=5)
                            self.dosa = self.fon.create_line(coordx-46, coordy,coordx-46, elem.getCoords()[1], width=5)
                            self.tresa =self.fon.create_line(coordx-48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx-48, coordy, coordx,coordy)
                            Cable.agregarUnion(self.dosa,coordx-46,elem.getCoords()[1] ,coordx-46, coordy)
                            Cable.agregarUnion(self.tresa,elem.getCoords()[0], elem.getCoords()[1],coordx-48 ,elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1], width=5)
                            self.dosa =self.fon.create_line(coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, elem.getCoords()[1],coordx, coordy)
                            Cable.agregarUnion(self.dosa,elem.getCoords()[0], elem.getCoords()[1], coordx,elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                            
                    else:
                        if who.getOrientacion() == "horizontal":
                            self.unoa =self.fon.create_line(coordx+53, coordy, coordx,coordy, width=5)
                            self.dosa =self.fon.create_line(coordx+50, coordy,coordx+50, elem.getCoords()[1], width=5)
                            self.tresa =self.fon.create_line(coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, coordy, coordx+53,coordy)
                            Cable.agregarUnion(self.dosa,coordx+50,coordy ,coordx+50,  elem.getCoords()[1])
                            Cable.agregarUnion(self.tresa,coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1], width=5)
                            self.dosa= self.fon.create_line(coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, elem.getCoords()[1],coordx, coordy)
                            Cable.agregarUnion(self.dosa,coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                else:
                    if elem.getCoords()[1] >= coordy:
                        if who.getOrientacion() == "horizontal":
                            
                            if elem.getCoords()[0] >= coordx:
                                self.unoa =self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
                                self.dosa=self.fon.create_line(coordx+46, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1])
                                Cable.agregarUnion(self.dosa,coordx+46, coordy, elem.getCoords()[0],coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            else:
                                self.unoa = self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
                                self.dosa = self.fon.create_line(coordx-42, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1])
                                Cable.agregarUnion(self.dosa,elem.getCoords()[0], coordy, coordx-42,coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1]-51, width=5)
                            self.dosa = self.fon.create_line(coordx, elem.getCoords()[1]-53, elem.getCoords()[0],elem.getCoords()[1]-53, width=5)
                            self.tresa =self.fon.create_line(elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1], width=5)
                            Cable = Cables()
                            Cable.agregarUnion(self.unoa,coordx, coordy,coordx, elem.getCoords()[1]-51)
                            Cable.agregarUnion(self.dosa,elem.getCoords()[0], elem.getCoords()[1]-53, coordx,elem.getCoords()[1]-53)
                            Cable.agregarUnion(self.tresa,elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1])
                            self.cables.append(Cable)
                            #
                            who.agregarCable(Cable)
                            elem.agregarCable(Cable)
                            Cable.agregarComponentes(who)
                            Cable.agregarComponentes(elem)
                    else:###
                        if who.getOrientacion() == "horizontal":
                            if elem.getCoords()[0] >= coordx:
                                self.unoa = self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1]+51, width=5)
                                self.dosa = self.fon.create_line(coordx+46, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0],elem.getCoords()[1]+51 ,elem.getCoords()[0],coordy )
                                Cable.agregarUnion(self.dosa,coordx+46, coordy, elem.getCoords()[0],coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            else:
                                self.unoa =self.fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1]+51, width=5)
                                self.dosa =self.fon.create_line(coordx-42, coordy, elem.getCoords()[0],coordy, width=5)
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,elem.getCoords()[0], elem.getCoords()[1]+51 ,elem.getCoords()[0],coordy )
                                Cable.agregarUnion(self.dosa,elem.getCoords()[0], coordy, coordx-42,coordy)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                        else:
                            self.unoa = self.fon.create_line(coordx, coordy,coordx, elem.getCoords()[1]+51, width=5)
                            self.dosa = self.fon.create_line(coordx, elem.getCoords()[1]+53, elem.getCoords()[0],elem.getCoords()[1]+53, width=5)
                            if coordx >= elem.getCoords()[0]: 
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,coordx,elem.getCoords()[1]+51 ,coordx, coordy )
                                Cable.agregarUnion(self.dosa,elem.getCoords()[0], elem.getCoords()[1]+53, coordx,elem.getCoords()[1]+53)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)
                            else:
                                Cable = Cables()
                                Cable.agregarUnion(self.unoa,coordx,elem.getCoords()[1]+51 ,coordx,  coordy )
                                Cable.agregarUnion(self.dosa,coordx, elem.getCoords()[1]+53, elem.getCoords()[0],elem.getCoords()[1]+53)
                                self.cables.append(Cable)
                                #
                                who.agregarCable(Cable)
                                elem.agregarCable(Cable)
                                Cable.agregarComponentes(who)
                                Cable.agregarComponentes(elem)

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
        while componente.getCablesConectados() != []:
            print(len( componente.getCablesConectados()))
            for elem2 in  componente.getCablesConectados()[0].getUniones():
                self.fon.delete(elem2)
            print(componente.getCablesConectados()[0].getComponentes()[0])
            eliminar = componente.getCablesConectados()[0]
            componente.getCablesConectados()[0].getComponentes()[0].eliminarCablesConectados(eliminar)
            componente.getCablesConectados()[0].getComponentes()[1].eliminarCablesConectados(eliminar)
            
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


    



