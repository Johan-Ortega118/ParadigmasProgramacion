
from Linea import Linea
from Punto import Punto

print("==========LINEA==========\n")

p1 = float(input("Valor de p1: "))
p2 = float(input("Valor de p2: "))

puntoA = Punto(p1, p2)


p1=float(input("Valor de p1: "))
p2=float(input("Valor de p2: "))

puntoB=Punto(p1, p2)

l = Linea(puntoA, puntoB)

while(True):
    opc = int(input("¿Que deseas hacer? \n1.-Mover a la Derecha \n2.-Mover a la Izquierda \n3.-Mover Arriba \n4.-Mover abajo \n5.-Ver puntos \n6.-Salir"))
    if opc==1:
        mov=float(input("¿A que posicion desea mover la linea? "))
        l.mueveDerecha(mov)
    elif opc==2:
        mov=float(input("¿A que posicion desea mover la linea? "))
        l.mueveIzquierda(mov)
    elif opc==3:
        mov=float(input("¿A que posicion desea mover la linea? "))
        l.mueveArriba(mov)
    elif opc==4:
        mov=float(input("¿A que posicion desea mover la linea? "))
        l.mueveAbajo(mov)
    elif opc==5:
        l.mostrar()
    elif opc==6:
        break
    else:
        print("No existe")
