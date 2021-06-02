#Calculadora Funcional
#Johan Paul Ortega Murillo
#S19004894 ISW

def numeros():
	global a, b

	a = int(input("Ingrese el primer numero: \n"))
	b = int (input("Ingrese el segundo numero: \n"))

def suma():
	print("El resultado es: ", a+b)

def resta():
	print("El resultado es: ", a-b)

def multiplicacion():
	print("El resultado es: ", a*b)

def division():
	if(b == 0):
		print("No se puede dividir en 0")
	else:
		print("El resultado es: ", a/b, " y su modulo es: ", a%b)


while(True):
	print ("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n")

	op = int(input("Ingrese una opcion: "))

	if(op == 1):
		numeros()
		suma()
	elif(op == 2):
		numeros()
		resta()
	elif(op == 3):
		numeros()
		multiplicacion()
	elif(op == 4):
		numeros()
		division()
	elif(op == 5):
		break

