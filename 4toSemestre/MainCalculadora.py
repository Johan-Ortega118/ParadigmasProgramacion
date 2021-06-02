#Main
#Johan Paul Ortega Murillo
#S19004894 ISW

from Calculadora import Calculadora

c = Calculadora()

p = str(input("¿Desea empezar?		si/no \n"))

while(p == 'si'):
	print("-------------CALCULADORA-------------")
	n1 = eval(input("\nIngresa el primer numero: "))
	n2 = eval(input("Ingresa el segundo numero: "))
	
	p = str(input("¿Deseas agregar otro numero?		si/no\n"))
	if(p == 'si'):
		n3 = eval(input("\nIngresa otro numero: "))

		print(c.sumar(n1,n2,n3),c.restar(n1,n2,n3),c.multiplicar(n1,n2,n3), c.dividir(n1,n2),c.modulo(n1,n2))
		p= str(input("¿Quieres cambiar el tercer numero?	si/no\n"))
	else:
		print(c.sumar(n1,n2),c.restar(n1,n2),c.multiplicar(n1,n2), c.dividir(n1,n2),c.modulo(n1,n2))
	p = str(input("¿Quieres volver a empezar?	si/no \n"))

