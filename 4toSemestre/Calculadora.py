#Calculadora
#Johan Paul Ortega Murillo
#S19004894 ISW

class Calculadora:
	
	def sumar(self,x,y,z=0):
		print("\nLa suma es:\n",str(x+y+z))

	def restar(self,x,y,z=0):
		print("La resta es:\n",str(x-y-z))

	def multiplicar(self,x,y,z=1):
		print("La multiplicacion es:\n",str(x*y*z))

	def dividir(self,x,y):
		if(x != 0 and y != 0):
			print("La division es:\n",str(x/y))

	def modulo(self,x,y):
		if(x != 0 and y != 0):
			print("El modulo es: \n",str(x%y))

