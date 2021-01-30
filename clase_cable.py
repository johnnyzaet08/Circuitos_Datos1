class Cables:
    def __init__(self):
        self.uniones = []
        self.coords = []
        self.componentes = []
        self.direcciones = []
    def agregarUnion(self,union,x1,y1,x2,y2):
      self.uniones.append(union)
      self.coords.append([x1,y1,x2,y2])
    def colision(self,x,y):
        choca = False
        xmenor = None
        ymenor = None
        xmayor= None
        ymayor = None 
        
        for i in self.coords:
            if i[0] <= i[2]:
                xmenor = i[0]
                xmayor = i[2]
            else:
                xmenor = i[2]
                xmayor = i[0]
            if i[1] <= i[3]:
                ymenor = i[1]
                ymayor = i[3]
            else:
                ymenor = i[3]
                ymayor = i[2]
            if xmenor<= x and  xmayor+5 >= x and ymenor <= y and  ymayor+5 >= y:
                choca = True
                break
                
        return choca
    def getUniones(self):
        return self.uniones
    def agregarComponentes(self,componente,direccion):
      self.componentes.append(componente)
      self.direcciones.append(direccion)
    def getComponentes(self):
      return self.componentes
    def eliminarDireccion(self,direccion):
        self.direcciones.remove(direccion)

    def getDireccion(self,indice):
        return self.direcciones[indice]
            
            
    
        
        
