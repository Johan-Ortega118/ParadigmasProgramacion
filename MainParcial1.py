
from Parcial1 import Rectangulo
from Vertices import Vertice

from Linea import Linea
from Punto import Punto

print("\n==========RECTANGULO==========\n")
print("\n<<<<<<<<<<PUNTO 1>>>>>>>>>>\n")
x=float(input("Valor de x1: "))
y=float(input("Valor de y1: "))

v1=Vertice(x, y)

print("\n<<<<<<<<<<PUNTO 2>>>>>>>>>>\n")
x=float(input("Valor de x2: "))
y=float(input("Valor de y2: "))

v2=Vertice(x, y)

print("\n<<<<<<<<<<PUNTO 3>>>>>>>>>>\n")
x=float(input("Valor de x3: "))
y=float(input("Valor de y3: "))

v3=Vertice(x, y)

print("\n<<<<<<<<<<PUNTO 4>>>>>>>>>>\n")
x=float(input("Valor de x4: "))
y=float(input("Valor de y4: "))

v4=Vertice(x, y)

r = Rectangulo(v1,v2,v3,v4)

while(True):
    print("\n¿Que deseas hacer?\n1.-Mover a la Derecha\n2.-Mover a la Izquierda\n3.-Mover Arriba\n4.-Mover abajo\n5.-Ver puntos\n6.-Superficie\n7.-Salir\n")
    opc=int(input())
    if opc==1:
        mov=float(input("\n¿A cuantas posiciones desea mover el rectangulo? "))
        r.mueveDerecha(mov)
    elif opc==2:
        mov=float(input("\n¿A cuantas posiciones desea mover el rectangulo? "))
        r.mueveIzquierda(mov)
    elif opc==3:
        mov=float(input("\n¿A cuantas posiciones desea mover el rectangulo? "))
        r.mueveArriba(mov)
    elif opc==4:
        mov=float(input("\n¿A cuantas posiciones desea mover el rectangulo? "))
        r.mueveAbajo(mov)
    elif opc==5:
        r.mostrar()
    elif opc==6:
        print("\nLa superficie es: ", r.superficie())
    elif opc==7:
        break
    else:
        print("No existe")


print("\n\n==========LINEA==========\n")

print("\n<<<<<<<<<<PUNTO A>>>>>>>>>>\n")
p1 = float(input("Valor de x1: "))
p2 = float(input("Valor de y1: "))

puntoA = Punto(p1, p2)

print("\n<<<<<<<<<<PUNTO B>>>>>>>>>>\n")
p1=float(input("Valor de x2: "))
p2=float(input("Valor de y2: "))

puntoB=Punto(p1, p2)

l = Linea(puntoA, puntoB)

while(True):
    opc = int(input("\n¿Que deseas hacer? \n1.-Mover a la Derecha \n2.-Mover a la Izquierda \n3.-Mover Arriba \n4.-Mover abajo \n5.-Ver puntos \n6.-Salir\n"))
    if opc==1:
        mov=float(input("\n¿A cuantas posiciones desea mover la linea? "))
        l.mueveDerecha(mov)
    elif opc==2:
        mov=float(input("\n¿A cuantas posiciones desea mover la linea? "))
        l.mueveIzquierda(mov)
    elif opc==3:
        mov=float(input("\n¿A cuantas posiciones desea mover la linea? "))
        l.mueveArriba(mov)
    elif opc==4:
        mov=float(input("\n¿A cuantas posiciones desea mover la linea? "))
        l.mueveAbajo(mov)
    elif opc==5:
        l.mostrar()
    elif opc==6:
        break
    else:
        print("No existe")
