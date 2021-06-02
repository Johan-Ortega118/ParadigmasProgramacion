require "./Ventana"

class Puerta

	ventana = Ventana.new
	ventana.class

	def abrir
		print "se ha abierto..."
	end

	def cerrar
		print "se ha cerrado..."
	end
end