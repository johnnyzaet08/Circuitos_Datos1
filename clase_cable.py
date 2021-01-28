class Cables:
    def __init__(self):
        self.uniones = []
        self.coords = []
        self.componentes = []
    def agregarUnion(self,union,x1,y1,x2,y2):
      self.uniones.append(union)
      self.coords.append([x1,y1,x2,y2])
    def colision(self,x,y):
        choca = False
        x2 = 0
        y2=0
        for i in self.coords:
            if i[0] <= x and  i[2]+5 >= x and i[1] <= y and  i[3]+5 >= y:
                choca = True
                break
        return choca
    def getUniones(self):
        return self.uniones
    def agregarComponentes(self,componente):
      self.componentes.append(componente)
    def getComponentes(self):
      return self.componentes
            
            
    
        
        
