module Calificaciones where

grado :: Float -> String
grado x = if x < 5 then "SS" else
        if x < 7 then "AP" else
        if x < 9 then "NT" else
        if x == 10 then "SB" else "MH"

aplicarGrado :: [Float] -> [String]
aplicarGrado xs = map grado xs