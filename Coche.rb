require "./Motor"
require "./Rueda"
require "./Ventana"
require "./Puerta"

class Coche

	motor = Motor.new
	rueda = Rueda.new
	puerta = Puerta.new

	print "¿Desea inflar alguna rueda?		(si/no)\n "

	a1 = gets.chomp

	while a1 == "si"

		print "¿Que rueda quiere inflar?\n "
		a2 = gets.chomp.to_i
	
		if a2 == 1
			print "La rueda 1 "
			rueda.inflar
		
		elsif a2 == 2
			print "La rueda 2 "
			rueda.inflar
		
		elsif a2 == 3
			print "La rueda 3 "
			rueda.inflar
		
		elsif a2 == 4
			print "La rueda 4 "
			rueda.inflar

		else
			print "Solo hay 4 ruedas :( "
		end

		print "\n¿Desea inflar otra llanta?	(si/no)\n "
		a1 = gets.chomp
	end
	
	print "------------------------------------------\n"
	print "¿Abrira una puerta?		(si/no)\n "

	a3 = gets.chomp

	while a3 == "si"

		print "¿Cual abrira?		(1 o 2)\n "
		a4 = gets.to_i

		if a4 == 1
			print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
			print "\nLa puerta 1 "
			puerta.abrir
			motor.arrancar
			print "\n\n------YO SOY EL CONDUCTOR------\n"
			print "\nLa puerta 1 "
			puerta.cerrar
			motor.apagar
			print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

		elsif a4 == 2
			print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
			print "\nLa puerta 2 "
			puerta.abrir
			print "\n\n------YO SOY EL COPILOTO------\n"
			print "\nLa puerta 2 "
			puerta.cerrar
			print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

		else
			print "\nSolo hay dos puertas"

		end

		print "\n¿Abrira otra puerta?		(si/no)\n "
		a3 = gets.chomp
	end

end