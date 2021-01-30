from clase_resistencia import *
from clase_fuente import *
from clase_cable import *
#indicaiones
#A = componente que empieza = who
#B = componente que termina = elem


def AderechaH_BizquierdaH(elem,who,fon,cables):
    if who.getIzquierda()  and elem.getDerecha() == False and who.getDerecha() == False :
        
        coordx, coordy = who.getCoords()
        unoa =fon.create_line(coordx+53, coordy, coordx,coordy, width=5)
        dosa =fon.create_line(coordx+50, coordy,coordx+50, elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx, coordy, coordx+53,coordy)
        Cable.agregarUnion(dosa,coordx+50,elem.getCoords()[1] ,coordx+50,   coordy)
        Cable.agregarUnion(tresa,elem.getCoords()[0] , elem.getCoords()[1],coordx+48 ,elem.getCoords()[1])
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,3)
        elem.setDerecha(True)
        who.setDerecha(True)
        
        
    elif who.getIzquierda() and elem.getDerecha() and elem.getIzquierda() == False and who.getDerecha() == False:
        
        coordx, coordy = who.getCoords()
        unoa =fon.create_line(elem.getCoords()[0]-42, elem.getCoords()[1],elem.getCoords()[0]-42,elem.getCoords()[1]-60, width=5)
        dosa =fon.create_line(elem.getCoords()[0]-42, elem.getCoords()[1]-60,coordx+48, elem.getCoords()[1]-60, width=5)
        tresa =fon.create_line(coordx+48, coordy, coordx+48,elem.getCoords()[1]-60, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]-42, elem.getCoords()[1]-60,elem.getCoords()[0]-42,elem.getCoords()[1])
        Cable.agregarUnion(dosa,elem.getCoords()[0]-42, elem.getCoords()[1]-60,coordx+48, elem.getCoords()[1]-60)
        Cable.agregarUnion(tresa,coordx+48, elem.getCoords()[1]-60, coordx+48, coordy)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,1)
        who.setDerecha(True)
        elem.setIzquierda(True)
        
    elif who.getIzquierda() == False and elem.getDerecha() and elem.getIzquierda() == False:
        
        coordx, coordy = who.getCoords()
        unoa =fon.create_line(elem.getCoords()[0]-42, elem.getCoords()[1],elem.getCoords()[0]-42,elem.getCoords()[1]-60, width=5)
        dosa =fon.create_line(elem.getCoords()[0]-42, elem.getCoords()[1]-60,coordx-42, elem.getCoords()[1]-60, width=5)
        tresa =fon.create_line(coordx-42, coordy, coordx-42,elem.getCoords()[1]-60, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]-42, elem.getCoords()[1]-60,elem.getCoords()[0]-42,elem.getCoords()[1])
        Cable.agregarUnion(dosa,elem.getCoords()[0]-42, elem.getCoords()[1]-60,coordx-42, elem.getCoords()[1]-60)
        Cable.agregarUnion(tresa,coordx-42,elem.getCoords()[1]-60 , coordx-42,coordy)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,1)
        elem.setIzquierda(True)
        who.setIzquierda(True)
        
    elif who.getIzquierda() == False and elem.getDerecha() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(coordx-48, coordy, coordx,coordy, width=5)
        dosa = fon.create_line(coordx-46, coordy,coordx-46, elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx-48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx-48, coordy, coordx,coordy)
        Cable.agregarUnion(dosa,coordx-46,elem.getCoords()[1] ,coordx-46,   coordy)
        Cable.agregarUnion(tresa,elem.getCoords()[0], elem.getCoords()[1],coordx-48 ,elem.getCoords()[1])
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,3)
        who.setIzquierda(True)
        elem.setDerecha(True)
        
def AderechaV_BizquierdaH(elem,who,fon,cables):
    if elem.getDerecha() == False and who.getAbajo() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(coordx, coordy,coordx, elem.getCoords()[1], width=5)
        dosa = fon.create_line(coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx,coordy ,coordx,elem.getCoords()[1])
        Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1], coordx,elem.getCoords()[1])
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,3)
        elem.setDerecha(True)
        who.setAbajo(True)
        
    elif elem.getDerecha() == False and who.getAbajo() and who.getArriba() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(elem.getCoords()[0]+48,coordy-37 ,elem.getCoords()[0]+48, elem.getCoords()[1], width=5)
        dosa = fon.create_line(elem.getCoords()[0]+48, coordy-37, coordx,coordy-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]+48,coordy-37 ,elem.getCoords()[0]+48, elem.getCoords()[1])
        Cable.agregarUnion(dosa,elem.getCoords()[0]+48, coordy-37, coordx,coordy-37)
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,3)
        who.setArriba(True)
        elem.setDerecha(True)
        
    elif elem.getDerecha() and elem.getIzquierda() == False and who.getAbajo() and who.getArriba() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(elem.getCoords()[0]-43,coordy-37 ,elem.getCoords()[0]-43, elem.getCoords()[1], width=5)
        dosa = fon.create_line(elem.getCoords()[0]-43, coordy-37, coordx,coordy-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]-43,coordy-37 ,elem.getCoords()[0]-43, elem.getCoords()[1])
        Cable.agregarUnion(dosa,elem.getCoords()[0]-43, coordy-37, coordx,coordy-37)
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,1)
        elem.setIzquierda(True)
        who.setArriba(True)
        
    elif elem.getDerecha() and elem.getIzquierda() == False and who.getAbajo() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(elem.getCoords()[0]-43,coordy+54 ,elem.getCoords()[0]-43, elem.getCoords()[1], width=5)
        dosa = fon.create_line(elem.getCoords()[0]-43, coordy+54, coordx,coordy+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]-43,coordy+54 ,elem.getCoords()[0]-43, elem.getCoords()[1])
        Cable.agregarUnion(dosa,elem.getCoords()[0]-43, coordy+54, coordx,coordy+54)
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,3)
        who.setAbajo(True)
        elem.setDerecha(True)

def AizquierdaH_BderechaH(elem,who,fon,cables):
    if who.getDerecha() == False and elem.getIzquierda() ==False:
        coordx, coordy = who.getCoords()
        unoa =fon.create_line(coordx+53, coordy, coordx,coordy, width=5)
        dosa =fon.create_line(coordx+50, coordy,coordx+50, elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx, coordy, coordx+53,coordy)
        Cable.agregarUnion(dosa,coordx+50,coordy ,coordx+50,  elem.getCoords()[1])
        Cable.agregarUnion(tresa,coordx+48, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,1)
        who.setDerecha(True)
        elem.setIzquierda(True)
        
    elif who.getDerecha() and who.getIzquierda() == False and elem.getIzquierda() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43,coordy ,coordx-43,  elem.getCoords()[1])
        Cable.agregarUnion(tresa,coordx-43, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,1)
        elem.setIzquierda(True)
        who.setIzquierda(True)
        
    elif who.getDerecha() == False and elem.getIzquierda() and elem.getDerecha() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(elem.getCoords()[0]+48, coordy,elem.getCoords()[0]+48, elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx+45, coordy, elem.getCoords()[0]+48,coordy, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,elem.getCoords()[0]+48, coordy,elem.getCoords()[0]+48, elem.getCoords()[1])
        Cable.agregarUnion(tresa,coordx+45, coordy, elem.getCoords()[0]+48,coordy)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,3)
        who.setDerecha(True)
        elem.setDerecha(True)

    elif who.getDerecha() and who.getIzquierda() == False and elem.getIzquierda() and elem.getDerecha() ==False:
        coordx, coordy = who.getCoords()
        unoa =fon.create_line(coordx-42, coordy,coordx-42,elem.getCoords()[1]-60, width=5)
        dosa =fon.create_line(elem.getCoords()[0]+48, elem.getCoords()[1]-60,elem.getCoords()[0]+48, elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx-42, elem.getCoords()[1]-60, elem.getCoords()[0]+48,elem.getCoords()[1]-60, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx-42, coordy,coordx-42,elem.getCoords()[1]-60)
        Cable.agregarUnion(dosa,elem.getCoords()[0]+48, elem.getCoords()[1]-60,elem.getCoords()[0]+48, elem.getCoords()[1])
        Cable.agregarUnion(tresa,coordx-42, elem.getCoords()[1]-60, elem.getCoords()[0]+48,elem.getCoords()[1]-60)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,3)
        elem.setDerecha(True)
        who.setIzquierda(True)


def AizquierdaV_BderechaH(elem,who,fon,cables):
    if elem.getIzquierda() == False and who.getAbajo() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(coordx, coordy,coordx, elem.getCoords()[1], width=5)
        dosa = fon.create_line(coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx,coordy ,coordx,elem.getCoords()[1])
        Cable.agregarUnion(dosa,coordx, elem.getCoords()[1], elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,1)
        elem.setIzquierda(True)
        who.setAbajo(True)
        
    elif elem.getIzquierda() and elem.getDerecha() == False and who.getAbajo() and who.getArriba() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(elem.getCoords()[0]+48,coordy-37 ,elem.getCoords()[0]+48, elem.getCoords()[1], width=5)
        dosa = fon.create_line(elem.getCoords()[0]+48, coordy-37, coordx,coordy-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]+48,coordy-37 ,elem.getCoords()[0]+48, elem.getCoords()[1])
        Cable.agregarUnion(dosa,coordx, coordy-37,elem.getCoords()[0]+48 ,coordy-37)
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,3)
        who.setArriba(True)
        elem.setDerecha(True)
        
    elif elem.getIzquierda() == False and who.getAbajo() and who.getArriba() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(elem.getCoords()[0]-43,coordy-37 ,elem.getCoords()[0]-43, elem.getCoords()[1], width=5)
        dosa = fon.create_line(elem.getCoords()[0]-43, coordy-37, coordx,coordy-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]-43,coordy-37 ,elem.getCoords()[0]-43, elem.getCoords()[1])
        Cable.agregarUnion(dosa,coordx, coordy-37,elem.getCoords()[0]-43 ,coordy-37)
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,1)
        who.setArriba(True)
        elem.setIzquierda(True)


    elif elem.getDerecha()  == False and elem.getIzquierda() and who.getAbajo() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(elem.getCoords()[0]+48,coordy+54 ,elem.getCoords()[0]+48, elem.getCoords()[1], width=5)
        dosa = fon.create_line(coordx, coordy+54,elem.getCoords()[0]+48 ,coordy+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,elem.getCoords()[0]+48,coordy+54 ,elem.getCoords()[0]+48, elem.getCoords()[1])
        Cable.agregarUnion(dosa,coordx, coordy+54,elem.getCoords()[0]+48 ,coordy+54)
        cables.append(Cable)
        #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,3)
        elem.setDerecha(True)
        who.setAbajo(True)


def AarribaIzquierdaH_BabajoDerechaV(elem,who,fon,cables):
    if who.getDerecha() == False and elem.getArriba() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx+48, coordy, elem.getCoords()[0],coordy, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1])
        Cable.agregarUnion(tresa,coordx+48, coordy, elem.getCoords()[0],coordy)
        cables.append(Cable)
        #####
        
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,2)
        who.setDerecha(True)
        elem.setArriba(True)
        
    elif who.getDerecha() and who.getIzquierda() == False and elem.getArriba() ==False:
        
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1]-37, width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43,coordy ,coordx-43,  elem.getCoords()[1])
        Cable.agregarUnion(tresa,coordx-43, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,2)
        who.setIzquierda(True)
        elem.setArriba(True)
    elif who.getDerecha() == False and elem.getArriba() and elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx+48, coordy,coordx+48, elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx+48, coordy,coordx+48, elem.getCoords()[1]+54)
        Cable.agregarUnion(tresa,coordx+48, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,4)
        elem.setAbajo(True)
        who.setDerecha(True)
        

    elif who.getDerecha() and who.getIzquierda() == False and elem.getArriba() and elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43, coordy,coordx+-43, elem.getCoords()[1]+54)
        Cable.agregarUnion(tresa,coordx-43, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,4)
        who.setIzquierda(True)
        elem.setAbajo(True)
    
def AarribaDerechaH_BabajoIzquierdaV(elem,who,fon,cables):
    if who.getIzquierda() == False and elem.getArriba() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx-43, coordy, elem.getCoords()[0],coordy, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1])
        Cable.agregarUnion(tresa,elem.getCoords()[0], coordy, coordx-43,coordy)
        cables.append(Cable)
        #####
        
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,2)
        elem.setArriba(True)
        who.setIzquierda(True)
        
        
    elif who.getDerecha() == False and who.getIzquierda() and elem.getArriba() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx+48, coordy,coordx+48, elem.getCoords()[1]-37, width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx+48,coordy ,coordx+48,  elem.getCoords()[1])
        Cable.agregarUnion(tresa,elem.getCoords()[0] , elem.getCoords()[1]-37, coordx+48,elem.getCoords()[1]-37)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,2)
        who.setDerecha(True)
        elem.setArriba(True)
        
    elif who.getIzquierda() and who.getDerecha() == False and elem.getArriba() and elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx+48, coordy,coordx+48, elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx+48, coordy,coordx+48, elem.getCoords()[1]+54)
        Cable.agregarUnion(tresa,coordx+48, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,4)
        who.setDerecha(True)
        elem.setAbajo(True)
    elif  who.getIzquierda() == False and elem.getArriba() and elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43, coordy,coordx+-43, elem.getCoords()[1]+54)
        Cable.agregarUnion(tresa,coordx-43, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,4)
        elem.setAbajo(True)
        who.setIzquierda(True)



        
def AarribaV_BabajoV(elem,who,fon,cables):
    if who.getAbajo() == False and elem.getArriba() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(coordx, coordy,coordx, elem.getCoords()[1]-51, width=5)
        dosa = fon.create_line(coordx, elem.getCoords()[1]-53, elem.getCoords()[0],elem.getCoords()[1]-53, width=5)
        tresa =fon.create_line(elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx, coordy,coordx, elem.getCoords()[1]-51)
        if elem.getCoords()[0] <= coordx: 
            Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1]-53, coordx,elem.getCoords()[1]-53)
        else:
            Cable.agregarUnion(dosa,coordx, elem.getCoords()[1]-53,  elem.getCoords()[0],elem.getCoords()[1]-53)        
        Cable.agregarUnion(tresa,elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,2)
        who.setAbajo(True)
        elem.setArriba(True)
    elif who.getAbajo() == False and elem.getArriba() and elem.getAbajo() == False:
        coordx, coordy = who.getCoords()
        dosa = fon.create_line(coordx, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx, coordy, coordx,elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        if elem.getCoords()[0] <= coordx: 
            Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1]+54, coordx,elem.getCoords()[1]+54)
        else:
            Cable.agregarUnion(dosa,coordx, elem.getCoords()[1]+54,  elem.getCoords()[0],elem.getCoords()[1]+54)        
        Cable.agregarUnion(tresa,coordx,coordy , coordx,elem.getCoords()[1]+54)
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,4)
        who.setAbajo(True)
        elem.setAbajo(True)
    elif who.getArriba() == False and who.getAbajo() and elem.getArriba() == False:
        coordx, coordy = who.getCoords()
        dosa = fon.create_line(coordx, coordy-37, elem.getCoords()[0],coordy-37, width=5)
        tresa =fon.create_line(elem.getCoords()[0], coordy-37, elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        if elem.getCoords()[0] <= coordx: 
            Cable.agregarUnion(dosa,elem.getCoords()[0],coordy-37, coordx,coordy-37)
        else:
            Cable.agregarUnion(dosa,coordx, coordy-37,  elem.getCoords()[0],coordy-37)        
        Cable.agregarUnion(tresa,elem.getCoords()[0],coordy-37 , elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,2)
        elem.setArriba(True)
        who.setArriba(True)
        
    elif who.getAbajo() and who.getArriba() == False and elem.getArriba() and elem.getAbajo() == False:
        coordx, coordy = who.getCoords()
        
        Cable = Cables()
        if elem.getCoords()[0] <= coordx: 
            unoa = fon.create_line(coordx-60, coordy-37,coordx, coordy-37, width=5)
            dosa = fon.create_line(coordx-60, elem.getCoords()[1]+54,coordx-60,  coordy-37, width=5)
            tresa =fon.create_line(elem.getCoords()[0], elem.getCoords()[1]+54, coordx-60,elem.getCoords()[1]+54, width=5)
            Cable.agregarUnion(dosa,coordx-60,coordy-37 ,coordx-60, elem.getCoords()[1]+54 )
            Cable.agregarUnion(unoa,coordx-60, coordy-37,coordx, coordy-37)
            Cable.agregarUnion(tresa,elem.getCoords()[0], elem.getCoords()[1]+54, coordx-60,elem.getCoords()[1]+54)
        else:
            unoa = fon.create_line(coordx, coordy-37,coordx+60, coordy-37, width=5)
            dosa = fon.create_line(coordx+60, elem.getCoords()[1]+54,coordx+60,  coordy-37, width=5)
            tresa =fon.create_line(coordx+60, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
            Cable.agregarUnion(unoa,coordx, coordy-37,coordx+60, coordy-37)
            Cable.agregarUnion(dosa,coordx+60,coordy-37 ,coordx+60, elem.getCoords()[1]+54 )
            Cable.agregarUnion(tresa,coordx+60, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,4)
        who.setArriba(True)
        elem.setAbajo(True)

def AabajoIzquierdaH_BarribaDerechaV(elem,who,fon,cables):
    if who.getDerecha() == False and elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx+48, coordy, elem.getCoords()[0],coordy, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1] ,elem.getCoords()[0],coordy)
        Cable.agregarUnion(tresa,coordx+48, coordy, elem.getCoords()[0],coordy)
        cables.append(Cable)
        #####
        
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,4)
        who.setDerecha(True)
        elem.setAbajo(True)
    elif who.getDerecha() and who.getIzquierda() == False and elem.getAbajo() and elem.getArriba() ==False:
        
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1]-37, width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43,elem.getCoords()[1]  ,coordx-43, coordy  )
        Cable.agregarUnion(tresa,coordx-43, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,2)
        who.setIzquierda(True)
        elem.setArriba(True)
    elif who.getDerecha() == False and elem.getAbajo() and elem.getArriba() ==False:
        
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx+48,elem.getCoords()[1]-37 ,coordx+48, coordy, width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx+48, elem.getCoords()[1]-37 ,coordx+48,coordy)
        Cable.agregarUnion(tresa,coordx+48, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,2)
        elem.setArriba(True)
        who.setDerecha(True)
        
    elif who.getDerecha() and who.getIzquierda() == False and  elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43,elem.getCoords()[1]+54 ,coordx+-43, coordy)
        Cable.agregarUnion(tresa,coordx-43, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,4)
        who.setIzquierda(True)
        elem.setAbajo(True)
        
        

        
    
def AabajoDerechaH_BarribaIzquierdaV(elem,who,fon,cables):
    who.setIzquierda(True)

    if who.getIzquierda() == False and elem.getAbajo() ==False:
        
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(elem.getCoords()[0], coordy,elem.getCoords()[0], elem.getCoords()[1], width=5)
        tresa =fon.create_line(coordx-43, coordy, elem.getCoords()[0],coordy, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1] ,elem.getCoords()[0],coordy)
        Cable.agregarUnion(tresa,elem.getCoords()[0], coordy,  coordx-43,coordy)
        cables.append(Cable)
        #####
        
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,4)
        elem.setAbajo(True)
        who.setIzquierda(True)
    elif who.getIzquierda()  == False  and elem.getAbajo() and elem.getArriba() ==False:
        
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx-43, coordy,coordx-43, elem.getCoords()[1]-37, width=5)
        tresa =fon.create_line(coordx-43, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx-43,elem.getCoords()[1]  ,coordx-43, coordy  )
        Cable.agregarUnion(tresa,elem.getCoords()[0] , elem.getCoords()[1]-37, coordx-43,elem.getCoords()[1]-37)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,1)
        Cable.agregarComponentes(elem,2)
        who.setIzquierda(True)
        elem.setArriba(True)
        
    elif who.getIzquierda() and who.getDerecha() == False and elem.getAbajo() and elem.getArriba() ==False:
        
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx+48,elem.getCoords()[1]-37 ,coordx+48, coordy, width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1]-37, elem.getCoords()[0],elem.getCoords()[1]-37, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx+48, elem.getCoords()[1]-37 ,coordx+48,coordy)
        Cable.agregarUnion(tresa,elem.getCoords()[0], elem.getCoords()[1]-37,  coordx+48,elem.getCoords()[1]-37)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,2)
        elem.setArriba(True)
        who.setDerecha(True)
        
    elif who.getDerecha() == False and who.getIzquierda()  and  elem.getAbajo() ==False:
        coordx, coordy = who.getCoords()
        dosa =fon.create_line(coordx+48, coordy,coordx+48, elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx+48, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        Cable.agregarUnion(dosa,coordx+48,elem.getCoords()[1]+54 ,coordx+48, coordy)
        Cable.agregarUnion(tresa,elem.getCoords()[0] , elem.getCoords()[1]+54,coordx+48 ,elem.getCoords()[1]+54)
        cables.append(Cable)
        #####
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,3)
        Cable.agregarComponentes(elem,4)
        who.setDerecha(True)
        elem.setAbajo(True)
        
        



#El who y el elem esta arrevez
def AabajoV_BarribaV(who,elem,fon,cables):
    
    if who.getAbajo() == False and elem.getArriba() == False:
        coordx, coordy = who.getCoords()
        unoa = fon.create_line(coordx, coordy,coordx, elem.getCoords()[1]-51, width=5)
        dosa = fon.create_line(coordx, elem.getCoords()[1]-53, elem.getCoords()[0],elem.getCoords()[1]-53, width=5)
        tresa =fon.create_line(elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        Cable.agregarUnion(unoa,coordx, coordy,coordx, elem.getCoords()[1]-51)
        if elem.getCoords()[0] <= coordx: 
            Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1]-53, coordx,elem.getCoords()[1]-53)
        else:
            Cable.agregarUnion(dosa,coordx, elem.getCoords()[1]-53,  elem.getCoords()[0],elem.getCoords()[1]-53)        
        Cable.agregarUnion(tresa,elem.getCoords()[0], elem.getCoords()[1]-55, elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,2)
        who.setAbajo(True)
        elem.setArriba(True)
        
    elif who.getAbajo() == False and elem.getArriba() and elem.getAbajo() == False:
        
        coordx, coordy = who.getCoords()
        dosa = fon.create_line(coordx, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
        tresa =fon.create_line(coordx, coordy, coordx,elem.getCoords()[1]+54, width=5)
        Cable = Cables()
        if elem.getCoords()[0] <= coordx: 
            Cable.agregarUnion(dosa,elem.getCoords()[0], elem.getCoords()[1]+54, coordx,elem.getCoords()[1]+54)
        else:
            Cable.agregarUnion(dosa,coordx, elem.getCoords()[1]+54,  elem.getCoords()[0],elem.getCoords()[1]+54)        
        Cable.agregarUnion(tresa,coordx,coordy , coordx,elem.getCoords()[1]+54)
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,4)
        Cable.agregarComponentes(elem,4)
        elem.setAbajo(True)
        who.setAbajo(True)
    elif who.getArriba() == False and who.getAbajo() and elem.getArriba() == False:
        
        coordx, coordy = who.getCoords()
        dosa = fon.create_line(coordx, coordy-37, elem.getCoords()[0],coordy-37, width=5)
        tresa =fon.create_line(elem.getCoords()[0], coordy-37, elem.getCoords()[0],elem.getCoords()[1], width=5)
        Cable = Cables()
        if elem.getCoords()[0] <= coordx: 
            Cable.agregarUnion(dosa,elem.getCoords()[0],coordy-37, coordx,coordy-37)
        else:
            Cable.agregarUnion(dosa,coordx, coordy-37,  elem.getCoords()[0],coordy-37)        
        Cable.agregarUnion(tresa,elem.getCoords()[0],coordy-37 , elem.getCoords()[0],elem.getCoords()[1])
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,2)
        who.setArriba(True)
        elem.setArriba(True)
        
    elif who.getAbajo() and who.getArriba() == False and elem.getArriba() and elem.getAbajo() == False:
        coordx, coordy = who.getCoords()
        Cable = Cables()
        if elem.getCoords()[0] <= coordx: 
            unoa = fon.create_line(coordx-60, coordy-37,coordx, coordy-37, width=5)
            dosa = fon.create_line(coordx-60, elem.getCoords()[1]+54,coordx-60,  coordy-37, width=5)
            tresa =fon.create_line(elem.getCoords()[0], elem.getCoords()[1]+54, coordx-60,elem.getCoords()[1]+54, width=5)
            Cable.agregarUnion(dosa,coordx-60,coordy-37 ,coordx-60, elem.getCoords()[1]+54 )
            Cable.agregarUnion(unoa,coordx-60, coordy-37,coordx, coordy-37)
            Cable.agregarUnion(tresa,elem.getCoords()[0], elem.getCoords()[1]+54, coordx-60,elem.getCoords()[1]+54)
        else:
            unoa = fon.create_line(coordx, coordy-37,coordx+60, coordy-37, width=5)
            dosa = fon.create_line(coordx+60, elem.getCoords()[1]+54,coordx+60,  coordy-37, width=5)
            tresa =fon.create_line(coordx+60, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54, width=5)
            Cable.agregarUnion(unoa,coordx, coordy-37,coordx+60, coordy-37)
            Cable.agregarUnion(dosa,coordx+60,coordy-37 ,coordx+60, elem.getCoords()[1]+54 )
            Cable.agregarUnion(tresa,coordx+60, elem.getCoords()[1]+54, elem.getCoords()[0],elem.getCoords()[1]+54)
        cables.append(Cable)
                                #
        who.agregarCable(Cable)
        elem.agregarCable(Cable)
        Cable.agregarComponentes(who,2)
        Cable.agregarComponentes(elem,4)
        who.setArriba(True)
        elem.setAbajo(True)
        
        


    
