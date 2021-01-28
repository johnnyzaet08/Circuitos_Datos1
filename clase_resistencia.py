
class Resistencia:
    def __init__(self,nom,valor,orientacion,boton):
        self.nom = nom 
        self.valor = valor
        self.orientacion =  orientacion
        self.boton = boton
        self.active = False
        self.conectado = False
        self.coordx, self.coordy = None, None
        self.cablesConectados = []

    def getCablesConectados(self):
        return self.cablesConectados
    def eliminarCablesConectados(self,cable):
        self.cablesConectados.remove(cable)
    def agregarCable(self,cable):
        self.cablesConectados.append(cable)
        
        
        
    def getNom(self):
        return self.nom
    

    def getValor(self):
        return self.valor

    def getOrientacion(self):
        return self.orientacion
    
    def getBoton(self):
        return self.boton
    
    def getCoords(self):
        return self.coordx, self.coordy

    def setNom(self,nomn):
        self.nom = nomn

    def setValor(self,valorn):
        self.valor = valorn

    def setOrientacion(self,orientacionn):
        self.orientacion = orientacionn

    def setBoton(self,botonn):
        self.boton = botonn
    
    def setCoords(self, x, y):
        self.coordx, self.coordy = x, y

    

    

