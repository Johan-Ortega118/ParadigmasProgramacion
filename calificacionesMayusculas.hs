module CalificacionesMayusculas where

notas2 :: Float -> String
notas2 x | x < 5 = "SS"
                   | x < 7 = "AP"
                   | x < 9 = "NT"
                   | x < 10 = "SB"
                   | otherwise = "MH"

notasAlumno ::  Map [Char] String
notasAlumno = M.map notas2 (fromList [("Matemáticas",6.5),("Física",5),("Economía",3.4)])
