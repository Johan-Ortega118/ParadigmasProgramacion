
m = putStrLn "CALCULADORA"

n = putStrLn "Bienvenido..."

k = putStrLn "Ingresa los valores <x> y <y>"

operaciones x y = do
	
	suma <- x + y
	resta <- x - y
	multiplicar <- x * y
	dividir <- x / y

	putStrLn ("La suma es: "++suma)
	putStrLn ("La resta es: "++resta)
	putStrLn ("La multiplicacion es: "++multiplicar)
	putStrLn ("La division es: "++dividir)

