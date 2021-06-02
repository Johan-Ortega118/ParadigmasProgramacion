#Empleados
#Johan Paul Ortega Murillo
#S19004894	ISW

class Empleado:

	def __init__(self,nombre,salario):
		self.nombre = nombre
		self.salario = salario

	def __str__(self):
		return self.nombre,self.salario

	def getTipoSalario(self,tipo):
		
		tipo = ('Obrero','Administrador','Intendente')
		
		if tipo == 'O'
			return tipo[0]
		
		elif tipo == 'A'
			return tipo[1]
		
		elif tipo == 'I'
			return tipo[2]
		
		else:
			return "Inexistente"

	'''def Obrero(self,nombre,salario):
		nombre = input("\nIngrese el nombre del obrero: ")
		salario = float("\nIngrese el salario basico de un obrero: ")
	'''

class Obrero (Empleado):
	
