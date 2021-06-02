
from Punto import Punto

class Linea:

    def __init__(self,puntoA,puntoB):
        self.puntoA = puntoA
        self.puntoB = puntoB

    def mueveDerecha(self,mov):
        self.puntoA.x = self.puntoA.x + mov
        self.puntoB.x = self.puntoB.x + mov

    def mueveIzquierda(self,mov):
        self.puntoA.x = self.puntoA.x - mov
        self.puntoB.x = self.puntoB.x - mov

    def mueveArriba(self,mov):
        self.puntoA.y = self.puntoA.y + mov
        self.puntoB.y = self.puntoB.y + mov

    def mueveAbajo(self,mov):
        self.puntoA.y = self.puntoA.y - mov
        self.puntoB.y = self.puntoB.y - mov

    def mostrar(self):
        print(self.puntoA, self.puntoB)
