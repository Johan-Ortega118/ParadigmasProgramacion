#Practica1
#Johan Paul Ortega Murillo
#S19004894 ISW

class Persona:
	
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad
	
	def mostrar(self):
		return self.nombre, self.edad


class Empleado(Persona):
	
	def __init__(self,sueldoBruto):
		self.sueldoBruto = sueldoBruto
	
	def mostrar(self):
		print(self.nombre,self.edad,self.sueldoBruto, self.salarioNeto)
	
	def calcularSalarioNeto(self,salarioNeto):
		self.salarioNeto = salarioNeto
		salarioNeto = sueldoBruto*0.7


class Cliente(Persona):
	
	def __init__(self,nombreCliente,telefonoContacto):
		self.nombreCliente = nombreCliente
		self.telefonoContacto = telefonoContacto
	
	def mostrar(self):
		print(self.nombre,self,edad,self.nombreCliente, self.telefonoContacto)


class Directivo:
	
	def __init__(self,categoria):
		self.categoria = "Privada"
	
	def mostrar(self):
		print(self.nombre,self.edad,self.categoria)


class Empresa:
	
	def __init__(self,nombre):
		self.nombre = "Walmart"

pers = Persona("Paul",27)
cli = Cliente("KFC","2714457291")
emp = Empleado(3500)

print("La persona ", pers.nombre, " tiene ", pers.edad, " años de edad")
print("Esta persona es un cliente ", cli.nombreCliente, " con numero de telefono ", cli.telefonoContacto)
print("Un empleado de Walmart gana $", emp.sueldoBruto, " quincenales")