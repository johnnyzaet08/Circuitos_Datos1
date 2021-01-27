

class Resistencia:
    def __init__(self,nom,valor,orientacion,boton):
        self.nom = nom 
        self.valor = valor
        self.orientacion =  orientacion
        self.boton = boton
    def getNom(self):
        return self.nom

    def getValor(self):
        return self.valor

    def getOrientacion(self):
        return self.orientacion
    
    def getBoton(self):
        return self.boton

    def setNom(self,nomn):
        self.nom = nomn

    def setValor(self,valorn):
        self.valor = valorn

    def setOrientacion(self,orientacionn):
        self.orientacion = orientacionn

    def setBoton(self,botonn):
        self.boton = botonn

    

    

