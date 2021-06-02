
from Vertices import Vertice

class Rectangulo:

	def __init__(self,v1,v2,v3,v4):
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.v4 = v4
		self.base = abs(v1.x - v2.x)
		self.altura = abs(v1.y - v3.y)

	@classmethod
	def bh(cls,base,altura):
		v1=Vertice(0, 0)
		v2=Vertice(base, 0)
		v3=Vertice(0, altura)
		v4=Vertice(altura, base)
		return cls(v1, v2, v3, v4)

	def superficie(self):				
		return self.base * self.altura

	def mueveDerecha(self,m):
		self.v1.x = (self.v1.x+m)
		self.v2.x = (self.v2.x+m)
		self.v3.x = (self.v3.x+m)
		self.v4.x = (self.v4.x+m)

	def mueveIzquierda(self,m):
		self.v1.x = (self.v1.x-m)
		self.v2.x = (self.v2.x-m)
		self.v3.x = (self.v3.x-m)
		self.v4.x = (self.v4.x-m)

	def mueveArriba(self,m):
		self.v1.y = (self.v1.y+m)
		self.v2.y = (self.v2.y+m)
		self.v3.y = (self.v3.y+m)
		self.v4.y = (self.v4.y+m)

	def mueveAbajo(self,m):
		self.v1.y = (self.v1.y-m)
		self.v2.y = (self.v2.y-m)
		self.v3.y = (self.v3.y-m)
		self.v4.y = (self.v4.y-m)

	def mostrar(self):
		print("\n",self.v1, self.v2, "\n", self.v3, self.v4)
